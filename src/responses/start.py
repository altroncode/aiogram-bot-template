import aiogram.types

from responses import base


class StartResponse(base.BaseResponse):
    def __init__(self, message: aiogram.types.Message):
        self.__message = message

    async def _send_response(self):
        full_name = self.__message.from_user.full_name
        await self.__message.answer(f'Привет, {full_name}!')
