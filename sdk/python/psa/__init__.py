from .client import PSAClient, PSAError

_default_client: PSAClient | None = None


def _get_client() -> PSAClient:
    global _default_client
    if _default_client is None:
        _default_client = PSAClient()
    return _default_client


def analyze(
    response_text: str,
    user_text: str | None = None,
    session_name: str | None = None,
    dry_run: bool = True,
) -> dict:
    return _get_client().analyze(
        response_text=response_text,
        user_text=user_text,
        session_name=session_name,
        dry_run=dry_run,
    )


__all__ = ["PSAClient", "PSAError", "analyze"]
