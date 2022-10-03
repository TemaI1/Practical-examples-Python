from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5522461893:AAG6FhecWqyJjDyx9qBunvu2wkqQJEd7NDg").build()

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("weather", weather_command))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()