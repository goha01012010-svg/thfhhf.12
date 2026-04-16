import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Включаем логирование для отслеживания ошибок
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Получаем токен из переменной окружения (БЕЗОПАСНО!)
TOKEN = '8534815900:AAHxGeuG6_SnOzIXwFTmaKoaMFiHsDX4b7E'

if not TOKEN:
    raise ValueError("Переменная окружения TELEGRAM_BOT_TOKEN не установлена!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет приветственное сообщение на команду /start"""
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! 👋\n"
        f"Я простой бот, который отвечает на /start.\n"
        f"Твой ID: {user.id}"
    )

def main():
    """Запускает бота"""
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()
    
    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Запускаем бота (для вебхуков на хостинге или polling локально)
    # Используем polling - работает везде
    print("Бот запущен и слушает команды...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()