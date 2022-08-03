from aiogram.dispatcher import filters
import aiogram.types

from responses import start
from loader import dp


@dp.message_handler(filters.CommandStart())
async def bot_start(message: aiogram.types.Message):
    await start.StartResponse(message)
