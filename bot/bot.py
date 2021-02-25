import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm SongHelperBot!\nTo get started, send your mood with a text message.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
