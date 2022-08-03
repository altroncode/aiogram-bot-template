from aiogram.dispatcher import filters
import aiogram.types

from loader import dp


@dp.message_handler(filters.CommandHelp())
async def bot_help(message: aiogram.types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")
    
    await message.answer("\n".join(text))
