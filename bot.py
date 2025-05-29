from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("7001997590:AAF_cm25-932echJtVw172XhYpFMor488KI")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Добро пожаловать в Appbooster Telegram Bot!\n"
        "Пожалуйста, ознакомьтесь с нашей политикой конфиденциальности:\n"
        "https://example.com/privacy\n\n"
        "Продолжая, вы соглашаетесь с её условиями."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Бот запущен. Ждёт команду /start...")
app.run_polling()