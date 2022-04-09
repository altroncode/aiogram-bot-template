import os
import environs


env = environs.Env()
environs.read_env()

BOT_TOKEN = env("BOT_TOKEN")
