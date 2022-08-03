from aiogram.dispatcher import filters
import aiogram.types

import responses.start
from loader import dp


@dp.message_handler(filters.CommandStart())
async def start(message: aiogram.types.Message):
    await responses.start.StartResponse(message)
