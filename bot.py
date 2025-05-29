import os

# Печатаем токен в логах Render для отладки
print("DEBUG: BOT_TOKEN =", os.getenv("BOT_TOKEN"))

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Добро пожаловать в Appbooster Telegram Bot!\n"
        "Пожалуйста, ознакомьтесь с нашей политикой конфиденциальности:\n"
        "https://example.com/privacy\n\n"
        "Продолжая, вы соглашаетесь с её условиями."
    )

# Создаём приложение Telegram-бота
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Бот запущен.")
app.run_polling()