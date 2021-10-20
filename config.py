
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2060448777:AAENMgEcw3_BT-YUlBRUB8vnRc_H8sYHEgY")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "8781954"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "35f780f99081d3440542aca16796c7b6")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQC7DFCOK4TTIC_sciXCp2JTB5rjmvZOFwVI4U51dp1IyhAOLemGf-mc2YxVc-hzgMNvtjh9xw7uxbiRWkRg6kf8wfpVuzAH9rsi8_SehQy7MxyQCEOdWO1HbdxrZsQT1FHblKtvRk64Ql2MzaYhaj0l7hCch3bUz0i9eVjqNr--D4Dh1zEYtAQHQ_4Z8LQQQF7Igb1sxPuOM0koNDNGkrgP05M0puSTnCRhHovXyYIzajLqqszEXRWgubs6hReap7DG2tCKITRR-0cmFXwHfWJP6QVbeMyJoMT1QUJtjF6CMnkOZe2dCpT0fYTeq23GavIdxrmeV0D06JAmLncGnh7Md9hnsAA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Gamy_Gamin:Anusha@cluster0.wujnj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "2010671024").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "yes").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()

# Subtitle Text
SUB_TEXT = os.environ.get("SUB_TEXT", "𝕊𝕦𝕓𝕥𝕚𝕥𝕝𝕖 ❗️ ")

# Channel 1
CHANNEL_ONE = os.environ.get("CHANNEL_ONE", "-1001505653053")

# Channel 2
CHANNEL_TWO = os.environ.get("CHANNEL_TWO", "-1001577630215")

# Bots UserName
BOT_URL = os.environ.get("BOT_URL", "Rule_Breakers_assistant2bot").lower()

# Custum Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
