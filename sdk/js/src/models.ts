export type AlertLevel = 'green' | 'yellow' | 'red' | 'critical';

export interface AnalyzeOptions {
  /** The model reply to read. */
  responseText: string;
  /** The user turn (or incoming message) the reply answered, read as context. */
  userText?: string;
  sessionName?: string;
  sessionId?: string;
  turn?: number;
  /** Default true: read without storing the turn. */
  dryRun?: boolean;
}

/** The /analyze response: postures per classifier (c0-c4, ca), bhs, alert and the other fields
 *  documented at https://splabs.io/docs/api. */
export interface Reading {
  alert: AlertLevel;
  bhs?: number;
  [field: string]: unknown;
}
