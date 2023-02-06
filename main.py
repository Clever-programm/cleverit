import logging
import time

from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import BOT_TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)
reply_keyboard = [['/time', '/phone'],
                  ['/close', '/work_time']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def start(update, context):
    await update.message.reply_text(
        "Я бот-CleverIT. Какая информация вам нужна?",
        reply_markup=markup
    )


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def ftime(update, context):
    await update.message.reply_text(time.asctime().split()[3])


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    start_handler = CommandHandler('start', start)
    time_handler = CommandHandler('time', ftime)
    close_handler = CommandHandler('close', close_keyboard)
    application.add_handler(start_handler)
    application.add_handler(time_handler)
    application.add_handler(close_handler)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
