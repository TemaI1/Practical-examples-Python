from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def open_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Содержимое книги:\n')
    book = open('phone book.txt', 'r')
    await update.message.reply_text(book.read())
    book.close()

async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    name = str(items[1])
    age = str(items[2])
    placement = str(items[3])
    telephone = str(items[4])
    file = open('phone book.txt', 'a')
    file.write(f'name: {name} age: {age}, placement: {placement}, telephone: {telephone}\n')
    file.close
    await update.message.reply_text(f'Добавлена запись:\nname: {name}, age: {age}, placement: {placement}, telephone: {telephone}')

async def rewrite_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    name = str(items[1])
    age = str(items[2])
    placement = str(items[3])
    telephone = str(items[4])
    file = open('phone book.txt', 'w')
    file.write(f'name: {name}, age: {age}, placement: {placement}, telephone: {telephone}\n')
    file.close
    await update.message.reply_text(f'Файл перезаписан, добавлена запись:\nname: {name}, age: {age}, placement: {placement}, telephone: {telephone}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Введите интересующую команду:\n/open_book\n/add_contact name age placement telephone\n/rewrite_contact name age placement telephone\n/help')