import logging
from config import Config
from aiogram import Bot, Dispatcher, executor, types
import asyncio


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

bot = Bot(token=Config.API_TOKEN)

loop_ = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop_)


@dp.message_handler()
async def text_handler(message: types.Message):
    await message.answer(message.text)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    await message.reply('start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
