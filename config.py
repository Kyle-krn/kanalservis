from environs import Env

env = Env()
env.read_env()

SHEETS_URL=env.str("SHEETS_URL")
BOT_TOKEN=env.str("BOT_TOKEN")
CHANEL_ID=env.str("CHANEL_ID")