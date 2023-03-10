import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
TUTORIAL = "https://t.me/joinchat/q4xMr02fvA9jNzQ1"
# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
๐คฉ **Hi {}  , I'm [แดษดแดษชส_าษชสแดแดสแตแตแต](https://t.me/On_air_Filter_bot) you can call me as Auto-Filter Bot**
"""
START_MSG = environ.get('START_MSG', default_start_msg)
IMDB_TEMPLATE = "<b><a href={url}>{title}</a>๐คบษชแดแดส</b>\n\n <b>โโโโโโ/yแดแดส: {year}\n โ |สแดแดษชษดษขโโโโโ: {rating}/10โโโโ \n โ\ษขแดษดสแด: #{genres}</b> \n\n     <b>[๐๐๐ 1](https://t.me/+PBGW_EV3ldY5YjJl)โฎ[๐๐๐ 2](https://t.me/+eDjzTT2Ua6kwMTI1)</b>"
IMDB_TEMPLATEE = "๐ฌ๐ฝ๐ฐ๐ผ๐ด: {title} {year}\n ๐คตโโ๏ธ๐ณ๐ธ๐๐ด๐ฒ๐๐พ๐: #{director}\n ๐๐๐๐ธ๐๐ด๐: #{writer}\n ๐ฅแดแด๊ฑแด: #{cast}"

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "โญ๏ธ๐ฒ๐๐๐๐๐๐ @on_air_movies๐๐ผ๐๐๐๐ searching ๐๐๐๐๐๐")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
