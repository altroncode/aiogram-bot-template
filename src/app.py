import aiogram
import aiogram.contrib.fsm_storage.memory
from aiogram import executor
from aiogram.contrib import fsm_storage
import dotenv

import commands
import config
import handlers
import middlewares


async def on_startup(dispatcher: aiogram.Dispatcher):
    dotenv.load_dotenv()
    await commands.set_default_commands(dispatcher)
    handlers.register_handlers(dispatcher)
    dispatcher.setup_middleware(middlewares.CallbackDataDTOInjectMiddleware())


def main():
    bot = aiogram.Bot(config.BotConfig().token, parse_mode=aiogram.types.ParseMode.HTML)
    dispatcher = aiogram.Dispatcher(bot, storage=fsm_storage.memory.MemoryStorage())
    executor.start_polling(dispatcher, on_startup=on_startup, skip_updates=True)


if __name__ == '__main__':
    main()
