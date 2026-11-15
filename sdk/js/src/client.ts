import type { AnalyzeOptions, Reading } from './models';

export interface PSAClientConfig {
  apiKey?: string;
  baseUrl?: string;
  timeout?: number;
  maxRetries?: number;
}

export class PSAError extends Error {
  constructor(public status: number, message: string) {
    super(`PSA API error ${status}: ${message}`);
  }
}

export class PSAClient {
  private apiKey: string;
  private baseUrl: string;
  private timeout: number;
  private maxRetries: number;

  constructor(config: PSAClientConfig = {}) {
    this.apiKey = config.apiKey ?? process.env.PSA_API_KEY ?? '';
    this.baseUrl = (config.baseUrl ?? process.env.PSA_BASE_URL ?? 'https://splabs.io').replace(/\/$/, '');
    this.timeout = config.timeout ?? parseInt(process.env.PSA_TIMEOUT ?? '10', 10) * 1000;
    this.maxRetries = config.maxRetries ?? parseInt(process.env.PSA_MAX_RETRIES ?? '3', 10);

    if (!this.apiKey) throw new Error('PSA_API_KEY is required');
  }

  private async request<T>(method: string, path: string, body?: unknown): Promise<T> {
    const url = `${this.baseUrl}${path}`;
    const headers: Record<string, string> = {
      Authorization: `Bearer ${this.apiKey}`,
      'Content-Type': 'application/json',
    };

    let lastError: Error | null = null;
    for (let attempt = 0; attempt < this.maxRetries; attempt++) {
      try {
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), this.timeout);

        const res = await fetch(url, {
          method,
          headers,
          body: body ? JSON.stringify(body) : undefined,
          signal: controller.signal,
        });
        clearTimeout(timer);

        if (res.status === 503 && attempt < this.maxRetries - 1) {
          await new Promise(r => setTimeout(r, 2 ** attempt * 1000));
          continue;
        }
        if (!res.ok) {
          throw new PSAError(res.status, await res.text());
        }
        const text = await res.text();
        return text ? JSON.parse(text) : ({} as T);
      } catch (e) {
        if (e instanceof PSAError) throw e;
        lastError = e as Error;
        if (attempt < this.maxRetries - 1) {
          await new Promise(r => setTimeout(r, 2 ** attempt * 1000));
        }
      }
    }
    throw new PSAError(0, `Request failed after ${this.maxRetries} attempts: ${lastError?.message}`);
  }

  /** POST /api/v2/psa/analyze: the behavioral reading of one model reply. */
  async analyze(options: AnalyzeOptions): Promise<Reading> {
    const body: Record<string, unknown> = { response_text: options.responseText };
    if (options.userText) body.user_text = options.userText;
    if (options.sessionName) body.session_name = options.sessionName;
    if (options.sessionId) body.session_id = options.sessionId;
    if (options.turn !== undefined) body.turn = options.turn;
    body.dry_run = options.dryRun ?? true;
    return this.request<Reading>('POST', '/api/v2/psa/analyze', body);
  }
}
