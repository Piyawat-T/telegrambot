# Telegram Bot

A simple yet functional Telegram bot built with Python that demonstrates core bot functionality including command handling, message processing, and media interaction.

## Features

- 🤖 **Command Handling**: Responds to `/start` and `/help` commands
- 💬 **Message Echo**: Echoes back user text messages
- 📸 **Media Support**: Handles photos and stickers
- 🛡️ **Error Handling**: Robust error handling and logging
- ⚙️ **Environment Configuration**: Secure token management

## Setup

### Prerequisites

- Python 3.7 or higher
- A Telegram bot token (get one from [@BotFather](https://t.me/botfather))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Piyawat-T/telegrambot.git
   cd telegrambot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your bot token:
   ```
   BOT_TOKEN=your_actual_bot_token_here
   ```

### Getting a Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Start a chat and send `/newbot`
3. Follow the instructions to create your bot
4. Copy the token and add it to your `.env` file

## Usage

### Running the Bot

```bash
python bot.py
```

The bot will start and begin polling for messages. You should see:
```
INFO - Starting bot...
```

### Bot Commands

- `/start` - Welcome message and bot introduction
- `/help` - Display available commands and features

### Interacting with the Bot

1. **Text Messages**: Send any text message and the bot will echo it back
2. **Photos**: Send a photo and get a response acknowledging the image
3. **Stickers**: Send stickers for a fun response

## Project Structure

```
telegrambot/
├── bot.py              # Main bot script
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Dependencies

- `python-telegram-bot` - Official Python wrapper for Telegram Bot API
- `python-dotenv` - Environment variable management

## Development

### Adding New Features

The bot is structured to make adding new features easy:

1. **New Commands**: Add command handlers in the `main()` function
2. **Message Types**: Add handlers for different message types (audio, video, etc.)
3. **Custom Logic**: Implement your business logic in separate handler functions

### Example: Adding a New Command

```python
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /custom command."""
    await update.message.reply_text("This is a custom command!")

# In main():
application.add_handler(CommandHandler("custom", custom_command))
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
