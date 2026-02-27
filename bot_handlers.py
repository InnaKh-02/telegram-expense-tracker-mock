from __future__ import annotations

import logging

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from services.summary import get_mocked_summary

logger = logging.getLogger(__name__)


WELCOME_TEXT = (
    "Hi! This is a demo expense tracker bot.\n"
    "\n"
    "Available commands:\n"
    "- /start — Show welcome message and buttons\n"
    "- /help — Show all commands and how to use the bot\n"
    "\n"
    "You can also tap the buttons below instead of typing the commands.\n"
    "\n"
    "This bot does not store real data. It always replies with the same example summary."
)


HELP_TEXT = (
    "Commands:\n"
    "- /start — Welcome message and buttons\n"
    "- /help — Show this help text\n"
    "- /end — End the demo session\n"
    "\n"
    "How to use:\n"
    "- Send an expense message (e.g., \"Lunch $12\" or \"Taxi $8\").\n"
    "- The bot will reply with an example summary grouped by day and category.\n"
    "\n"
    "Note: This is a local demo; responses are mocked and always the same."
)


def _default_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [["Start", "Help"], ["End"]],
        resize_keyboard=True,
        one_time_keyboard=False,
    )


async def end_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["ended"] = True
    if update.effective_message:
        await update.effective_message.reply_text(
            "Demo session ended. You can close this chat or send /start to begin again.",
            reply_markup=_default_keyboard(),
        )


async def menu_button_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if not update.effective_message or not update.effective_message.text:
        return

    text = update.effective_message.text.strip().lower()
    if text == "start":
        await start_handler(update, context)
    elif text == "help":
        await help_handler(update, context)
    elif text == "end":
        await end_handler(update, context)
    else:
        # Fallback to normal expense behavior for any other text.
        await expense_message_handler(update, context)


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["ended"] = False
    if update.effective_message:
        await update.effective_message.reply_text(
            WELCOME_TEXT,
            reply_markup=_default_keyboard(),
        )


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_message:
        await update.effective_message.reply_text(
            HELP_TEXT,
            reply_markup=_default_keyboard(),
        )


async def expense_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if not update.effective_message:
        return

    if context.user_data.get("ended"):
        await update.effective_message.reply_text(
            "This demo session has ended. Send /start to begin again."
        )
        return

    # Ignore actual content intentionally (mock-only behavior).
    try:
        summary = get_mocked_summary()
    except Exception:
        logger.exception("Failed to build mocked summary")
        await update.effective_message.reply_text(
            "Sorry—something went wrong generating the summary."
        )
        return

    await update.effective_message.reply_text(summary)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.exception("Unhandled exception in bot", exc_info=context.error)

    try:
        update_obj = update if isinstance(update, Update) else None
        if update_obj and update_obj.effective_message:
            await update_obj.effective_message.reply_text(
                "Sorry—an unexpected error occurred."
            )
    except Exception:
        # Never let the error handler raise.
        pass
