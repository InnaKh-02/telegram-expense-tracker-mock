from __future__ import annotations

import os


def _try_load_dotenv() -> None:
    try:
        from dotenv import load_dotenv  # type: ignore
    except Exception:
        return
    load_dotenv()


def get_bot_token() -> str:
    _try_load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        raise RuntimeError(
            "Missing TELEGRAM_BOT_TOKEN. Set it in your environment (or in a .env file)."
        )
    return token
