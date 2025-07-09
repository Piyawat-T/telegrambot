#!/usr/bin/env python3
"""
Simple Telegram Bot

This bot demonstrates basic functionality including:
- Responding to /start and /help commands
- Echoing user messages
- Basic error handling
"""

import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}!\n\n"
        f"Welcome to this Telegram bot! 🤖\n\n"
        f"Here's what I can do:\n"
        f"• Send me any message and I'll echo it back\n"
        f"• Use /help to see available commands\n\n"
        f"Feel free to start chatting!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
🤖 *Bot Commands:*

/start - Start the bot and see welcome message
/help - Show this help message

*Other features:*
• Send me any text message and I'll echo it back
• Send me photos, stickers, or other media and I'll respond

Just start typing to try it out!
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    user_message = update.message.text
    user_name = update.effective_user.first_name
    
    response = f"Hi {user_name}! You said: '{user_message}'"
    await update.message.reply_text(response)


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle photo messages."""
    await update.message.reply_text("Nice photo! 📸 I can see you sent me an image.")


async def handle_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle sticker messages."""
    await update.message.reply_text("Cool sticker! 😄")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)


def main() -> None:
    """Start the bot."""
    # Get the bot token from environment variables
    token = os.getenv('BOT_TOKEN')
    
    if not token:
        logger.error("BOT_TOKEN not found! Please set it in your .env file or environment variables.")
        return
    
    # Create the Application
    application = Application.builder().token(token).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.Sticker.ALL, handle_sticker))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    # Run the bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()