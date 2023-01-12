import typing

from aiogram.dispatcher import handler
from aiogram.dispatcher import middlewares
from aiogram.types import callback_query

from models import callback_data_dto


__all__ = ('CallbackDataDTOInjectMiddleware',)


class CallbackDataDTOInjectMiddleware(middlewares.BaseMiddleware):

    @staticmethod
    def on_process_callback_query(query: callback_query.CallbackQuery, data: dict[str, typing.Any]):
        del query  # Unused
        for _, arg_type in handler.current_handler.get().__annotations__:
            if issubclass(arg_type, callback_data_dto.CallbackDataDTO):
                data['callback_data'] = arg_type(data['callback_data'])
