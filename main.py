from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token = "5820311353:AAGsVItBrpxE4fkvBssjEXkC3W13DFP_n0o")

dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("отвечаю на команду /start")

@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.reply("Я бот.Я умею дублировать твои сообщения и отвечать на команду start!")



if __name__ == "__main__":
    executor.start_polling(dp)
