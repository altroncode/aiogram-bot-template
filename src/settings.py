import environs


env = environs.Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
