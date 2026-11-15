export { PSAClient, PSAError } from './client';
export type { PSAClientConfig } from './client';
export type { AnalyzeOptions, Reading, AlertLevel } from './models';

import { PSAClient } from './client';
import type { AnalyzeOptions, Reading } from './models';

let _default: PSAClient | null = null;

function getDefault(): PSAClient {
  if (!_default) _default = new PSAClient();
  return _default;
}

export function analyze(options: AnalyzeOptions): Promise<Reading> {
  return getDefault().analyze(options);
}
