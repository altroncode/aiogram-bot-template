import aiogram.types

from responses import base


class HelpResponse(base.BaseResponse):
    def __init__(self, message: aiogram.types.Message):
        self.__message = message

    async def _send_response(self):
        await self.__message.answer(
            'Commands:'
            '/start - Start bot\n'
            '/help - This message'
        )
