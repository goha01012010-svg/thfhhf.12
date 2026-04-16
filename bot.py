import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Получаем токен
TOKEN = '8534815900:AAHxGeuG6_SnOzIXwFTmaKoaMFiHsDX4b7E'

if not TOKEN:
    logger.error("Токен не найден! Проверьте файл .env")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет приветственное сообщение"""
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! 👋\n"
        f"Я бот, который работает в Docker контейнере.\n"
        f"Твой ID: {user.id}"
    )

def main():
    """Запуск бота"""
    try:
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        logger.info("Бот успешно запущен!")
        app.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"Ошибка при запуске: {e}")
        exit(1)

if __name__ == '__main__':
    main()
