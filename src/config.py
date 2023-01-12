import pydantic


class BotConfig(pydantic.BaseSettings):
    token: str = pydantic.Field(env='BOT_TOKEN')


class DatabaseConfig(pydantic.BaseSettings):
    uri: str = pydantic.Field(env='DATABASE_URI')
