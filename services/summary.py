from __future__ import annotations

import logging
from typing import Optional
from google import genai
from config import get_gemini_api_key

logger = logging.getLogger(__name__)

try:
    client = genai.Client(api_key=get_gemini_api_key())
except Exception as e:
    logger.error(f"Failed to initialize Gemini client: {e}")
    client = None

def get_summary(user_message:str, chat_history:Optional[str] = None) -> str:
    if not client:
        return "Error: Gemini client is not initialized. Please check the logs for details."
    try:
        system_instructions = """
        Ти - розумний асистент для трекінгу особистих витрат.
        Користувач надсилає повідомлення про витрати (наприклад: "Обід 250 грн", "Таксі 180", "Купив каву 65").
        Твоє завдання:
        1. Розпізнати дату (якщо не вказано - сьогодні).
        2. Витягти категорію (Їжа, Транспорт, Розваги тощо).
        3. Витягти суму та валюту.
        4. Зробити красивий, структурований summary за днями та категоріями.

        Відповідай тільки готовим summary, без зайвих пояснень. 
        """
        full_prompt = f"{system_instructions}\n\nUser: {user_message}"

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=full_prompt,
        )
        return response.text.strip()
    except Exception as e:
        logger.exception("Gemini API error")
        return f"Sorry, I couldn't generate the summary due to an error: {str(e)[:200]}"


def get_mocked_summary() -> str:
    return (
        "Expense summary (example data)\n"
        "\n"
        "2025-01-01\n"
        "- Food: $25 (Lunch $12, Dinner $13)\n"
        "- Transport: $8 (Taxi $8)\n"
        "- Total: $33\n"
        "\n"
        "2025-01-02\n"
        "- Food: $9 (Coffee $4, Snack $5)\n"
        "- Other: $15 (Movie $15)\n"
        "- Total: $24\n"
    )
