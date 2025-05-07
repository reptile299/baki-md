from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "8080230764:AAHYWRdQn2cNL5Xg_xLM7Y-g3Xcw-kNRw5g"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot. Type /help to see available commands.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("""
Available Commands:
/start - Initializes the bot
/help - Lists available commands
/about - Shows information about the bot
/settings - Opens user settings
/feedback - Allows users to send feedback
""")

def about(update: Update, context: CallbackContext):
    update.message.reply_text("I am a Telegram bot created to assist users.")

def settings(update: Update, context: CallbackContext):
    update.message.reply_text("Settings are currently under development.")

def feedback(update: Update, context: CallbackContext):
    update.message.reply_text("You can send your feedback by replying to this message.")

# Admin Commands
def ban(update: Update, context: CallbackContext):
    update.message.reply_text("Ban command is only available for admins.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("settings", settings))
    dp.add_handler(CommandHandler("feedback", feedback))
    dp.add_handler(CommandHandler("ban", ban))

    updater.start_polling()
    updater.idle()

if _name_ == "_main_":
    main()
