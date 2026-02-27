from __future__ import annotations

import logging

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot_handlers import (
    error_handler,
    expense_message_handler,
    help_handler,
    end_handler,
    menu_button_handler,
    start_handler,
)
from config import get_bot_token


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )

    token = get_bot_token()

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(CommandHandler("end", end_handler))

    # First, handle texts coming from our menu buttons.
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, menu_button_handler)
    )

    # Fallback: any remaining text is treated as an expense message.
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, expense_message_handler)
    )
    application.add_error_handler(error_handler)

    application.run_polling(allowed_updates=["message"])


if __name__ == "__main__":
    main()
