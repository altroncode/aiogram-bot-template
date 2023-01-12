import functools

from aiogram.utils import callback_data

from utils import writing_style_converting


__all__ = ('CallbackFactory', 'TestCallbackFactory')


class CallbackFactory(callback_data.CallbackData):
    _prefix: str | None = None

    def __init__(self, separator: str = ':') -> None:
        class_name = self.__class__.__name__
        if not self._prefix:
            self._prefix = writing_style_converting.convert_class_name_to_snake_case(class_name)
            self._prefix = self._prefix.removesuffix('_callback_factory').rstrip('_')
        super().__init__(self._prefix, *self.__annotations__, sep=separator)

    def get_prefix(self) -> str | None:
        return self._prefix


class TestCallbackFactory(CallbackFactory):
    id: str
    action: str
