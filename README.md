# Telegram Expense Tracker Bot (Mock)

Local-only Telegram bot demo for expense tracking. The bot **does not store any real data**.

## Prerequisites

- Python 3.10+
- A Telegram bot token from BotFather
- A Gemini API key from Google AI Studio 

## Setup (cmd)

Open .env and enter your data
- TELEGRAM_BOT_TOKEN="YOUR_TOKEN_HERE"
- GEMINI_API_KEY="YOUR_API_KEY_HERE"

```
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## Usage

- Use the **buttons** at the bottom of the chat:
  - `Start` – same as `/start`, shows welcome text and buttons
  - `Help` – same as `/help`, shows all commands and how to use the bot
  - `End` – same as `/end`, ends the current demo session
- Or type the commands manually: `/start`, `/help`, `/end`.
- While the session is active, send any message like:
  - `Lunch $12`
  - `Taxi $8`

The bot will always reply with generated summary while the session is active.
After you use **End**, any text will just say that the demo session has ended until you send `/start` again.

## Tests

```
.\.venv\Scripts\python.exe -m pytest -q
```
