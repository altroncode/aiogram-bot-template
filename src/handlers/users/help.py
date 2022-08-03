from aiogram.dispatcher import filters
import aiogram.types

from loader import dp
import responses.help


@dp.message_handler(filters.CommandHelp())
async def help_message(message: aiogram.types.Message):
    await responses.help.HelpResponse(message)
