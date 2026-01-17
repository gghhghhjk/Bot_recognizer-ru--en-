# Bot_translator-ru--en-
Telegram bot that Recognizing your text fastly.
Goal: Provide a simple tool for quickly translating Russian text into English directly in Telegram.


Benefits:
 - Helps you quickly translate phrases, messages, and short texts.
 - Convenient for communicating with foreigners and drafting letters/comments in English.
 - Easy integration into private chats and groups (in private mode or for moderators).


Main functions:
 - /start - greeting and short instructions.
 - Automatic translation of any regular text message (rus → eng).


Requirements:
 - Python 3.8+
 - Telegram bot token (BotFather)
 - Steps:
 1. Clone the repository or save the bot.py file.
 2. Create a .env file next to bot.py and add:
 TOKEN=your_token
 3. Install the dependencies:
 pip install python-dotenv pyTelegramBotAPI googletrans
 4. Run:
 python bot.py
 - Usage:
 - Open a conversation with the bot in Telegram, send /start, then any Russian text, and get a translation.


The project is a compact tool for everyday translation in Telegram: 
it is easy to install, use, and expand. It is suitable for both personal use and
as a basis for more complex bots (multilingual support, integration with a translation database, etc.).
It is recommended to start with the basic version and add features (validation, cache, and support for long texts) as needed.

Credits: Matvey K.
