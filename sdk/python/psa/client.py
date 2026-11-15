from __future__ import annotations
import os
import time
import http.client
import ssl
import socket
import json
from typing import List, Optional


class PSAError(Exception):
    def __init__(self, status: int, message: str):
        self.status = status
        super().__init__(f"PSA API error {status}: {message}")


class PSAClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = 10,
        max_retries: int = 3,
    ):
        self.api_key = api_key or os.environ.get("PSA_API_KEY", "")
        self.base_url = (base_url or os.environ.get("PSA_BASE_URL", "https://splabs.io")).rstrip("/")
        self.timeout = int(os.environ.get("PSA_TIMEOUT", timeout))
        self.max_retries = int(os.environ.get("PSA_MAX_RETRIES", max_retries))

        if not self.api_key:
            raise ValueError("PSA_API_KEY is required: set env var or pass api_key=")

        parsed = self._parse_url(self.base_url)
        self._host = parsed["host"]
        self._port = parsed["port"]
        self._scheme = parsed["scheme"]

    def _parse_url(self, url: str) -> dict:
        url = url.replace("https://", "").replace("http://", "")
        scheme = "https" if "https" in self.base_url else "http"
        if ":" in url:
            host, port = url.rsplit(":", 1)
        else:
            host = url
            port = 443 if scheme == "https" else 80
        return {"host": host, "port": int(port), "scheme": scheme}

    def _request(self, method: str, path: str, body: Optional[dict] = None) -> dict:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Host": self._host,
        }
        encoded = json.dumps(body).encode() if body else b""

        last_error = None
        for attempt in range(self.max_retries):
            try:
                if self._scheme == "https":
                    ctx = ssl.create_default_context()
                    ctx.check_hostname = False
                    ctx.verify_mode = ssl.CERT_NONE
                    sock = socket.create_connection((self._host, self._port), timeout=self.timeout)
                    ssl_sock = ctx.wrap_socket(sock, server_hostname=self._host)
                    conn = http.client.HTTPSConnection(self._host, context=ctx)
                    conn.sock = ssl_sock
                else:
                    conn = http.client.HTTPConnection(self._host, self._port, timeout=self.timeout)

                conn.request(method, path, body=encoded, headers=headers)
                r = conn.getresponse()
                raw = r.read().decode()

                if r.status == 503 and attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                if r.status >= 400:
                    raise PSAError(r.status, raw)

                return json.loads(raw) if raw else {}

            except PSAError:
                raise
            except Exception as e:
                last_error = e
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)

        raise PSAError(0, f"Request failed after {self.max_retries} attempts: {last_error}")

    def analyze(
        self,
        response_text: str,
        session_name: Optional[str] = None,
        session_id: Optional[str] = None,
        user_text: Optional[str] = None,
        turn: Optional[int] = None,
        dry_run: bool = False,
    ) -> dict:
        """Call POST /api/v2/psa/analyze: returns the raw response dict."""
        payload: dict = {"response_text": response_text}
        if session_name:
            payload["session_name"] = session_name
        if session_id:
            payload["session_id"] = session_id
        if user_text:
            payload["user_text"] = user_text
        if turn is not None:
            payload["turn"] = turn
        if dry_run:
            payload["dry_run"] = True
        return self._request("POST", "/api/v2/psa/analyze", payload)

