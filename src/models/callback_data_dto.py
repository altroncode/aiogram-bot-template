import pydantic


class CallbackDataDTO(pydantic.BaseModel):
    pass


class TestCallbackDataDTO(CallbackDataDTO):
    id: int
    action: str
