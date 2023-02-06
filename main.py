import logging
import time

from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def ftime(update, context):
    user = update.effective_user
    await update.message.reply_text(time.asctime().split()[3])


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    time_handler = CommandHandler('time', ftime)
    application.add_handler(time_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
