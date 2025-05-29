import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ Согласен", callback_data="agree")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Привет! Добро пожаловать в Appbooster Telegram Bot!\n\n"
        "Перед началом, пожалуйста, ознакомьтесь с нашей политикой конфиденциальности:\n"
        "https://example.com/privacy\n\n"
        "Нажмите кнопку ниже, если вы согласны с условиями.",
        reply_markup=reply_markup
    )

# Обработка нажатий на кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # обязательно подтверждаем нажатие
    if query.data == "agree":
        await query.edit_message_text("✅ Спасибо! Вы дали согласие на обработку персональных данных.")

# Запускаем приложение
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("✅ Бот запущен.")
app.run_polling()