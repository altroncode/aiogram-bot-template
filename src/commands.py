import aiogram
from aiogram.types import bot_command


async def set_default_commands(dispatcher: aiogram.Dispatcher):
    await dispatcher.bot.set_my_commands(
        [
            bot_command.BotCommand("start", "Запустить бота"),
            bot_command.BotCommand("help", "Вывести справку"),
        ]
    )
