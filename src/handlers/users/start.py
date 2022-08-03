from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from responses import start
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await start.StartResponse(message)
