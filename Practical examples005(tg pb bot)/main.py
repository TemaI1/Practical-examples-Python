from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5685039227:AAE9aEI-4Fa61vNRTxRqHst3yN_PQaMshaM").build()

app.add_handler(CommandHandler("open_book", open_command))
app.add_handler(CommandHandler("add_contact", add_command))
app.add_handler(CommandHandler("rewrite_contact", rewrite_command))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()