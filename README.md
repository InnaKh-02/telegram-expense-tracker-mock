# Telegram Expense Tracker Bot (Mock)

Local-only Telegram bot demo for expense tracking. The bot **does not store any real data** and always replies with the same **mocked summary**.

## Prerequisites

- Python 3.10+
- A Telegram bot token from BotFather

## Setup

Set your bot token (PowerShell):

```powershell
$env:TELEGRAM_BOT_TOKEN="YOUR_TOKEN_HERE"
```

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:TELEGRAM_BOT_TOKEN="YOUR_TOKEN_HERE"
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

The bot will always reply with the same example summary while the session is active.
After you use **End**, any text will just say that the demo session has ended until you send `/start` again.

## Tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```
