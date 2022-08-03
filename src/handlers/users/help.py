from aiogram.dispatcher import filters
import aiogram.types

from loader import dp
import responses.help


@dp.message_handler(filters.CommandHelp())
async def bot_help(message: aiogram.types.Message):
    await responses.help.HelpResponse(message)
