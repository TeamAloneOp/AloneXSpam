import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 33603336
API_HASH = "c9683a8ec3b886c18219f650fc8ed429"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("8565641545:AAFhiVi8tniZbu1S4OafKxLWQbbr-hzGRmk", default=None)
BOT_TOKEN2 = getenv("8614712128:AAEcs7OcLM8DEKUd3gl_iNhRppBis1LqR_4", default=None)
BOT_TOKEN3 = getenv("8632280042:AAEZcLMxNtO-aBJlQ5JEEGY4ns5F3HtHB2c", default=None)
BOT_TOKEN4 = getenv("7809825568:AAHYCYgel8EiKIm-zDzjsQvAxMSyj66mpQg", default=None)
BOT_TOKEN5 = getenv("8795767972:AAGdBR-s1ZvY8Afh0zKJUFg6olQwBBFMqAk", default=None)
BOT_TOKEN6 = getenv("8687100196:AAFwoX22dmcKDSTZ_h4LJczNkMFMWolJ7dM", default=None)
BOT_TOKEN7 = getenv("8762340783:AAFZ99tg6K5a5eDQlxsYl9jr_-zQeuteBHY", default=None)
BOT_TOKEN8 = getenv("8745619380:AAGjM8E4t8-PHREU73_MXz0gFr2tK3uz1RM", default=None)
BOT_TOKEN9 = getenv("8600705453:AAHWLZ_jgFNQihbYlKRrpNWIvZyk2HUaOZI", default=None)
BOT_TOKEN10 = getenv("8619853701:AAFEdz90PpDmUDlElO_h9tEjc7IjsxpF13U", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7724452546").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6079943111"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

