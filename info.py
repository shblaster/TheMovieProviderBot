import re
from os import environ, getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/b6ae7205a9de7369ac42f.jpg https://telegra.ph/file/cd95258ac6d77c5e82854.jpg https://telegra.ph/file/4281fa620c989610be53a.jpg https://telegra.ph/file/bd8814f412cfa4638b7e7.jpg https://telegra.ph/file/7a559089f10fd2045c148.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/7b334ca625c9a995ec3d6.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/e5468266c677761b05bae.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://telegra.ph/file/af9db066e220f13dc731b.jpg'))
CODE = (environ.get('CODE', 'https://telegra.ph/file/044e29c96899f670d9c6c.jpg'))

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'ziplinker.net'))
STREAM_API = (environ.get('STREAM_API', 'edad27b3c1e52fa0b8ce835b2c7af9fe3ceba76b'))
STREAMHTO = (environ.get('STREAMHTO', 'https://t.me/Howto_openthislink/8'))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()] #Channel id for auto indexing ( make sure bot is admin )
auth_users = environ.get('AUTH_USERS', '')
if auth_users:
    AUTH_USERS = [int(admin) if id_pattern.search(admin) else admin for admin in auth_users.split()]
else:
    AUTH_USERS = []
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', ''))
authusers = environ.get('AUTH_USERS', '')
AUTH_USERS = [int(user) if id_pattern.search(user) else user for user in authusers.split()]

# IMDB
IMDB = is_enabled(environ.get('IMDB', 'True'), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get('LONG_IMDB_DESCRIPTION', 'True'), True)
SPELL_CHECK_REPLY = is_enabled(environ.get('SPELL_CHECK_REPLY', 'True'), True)
MAX_LIST_ELM = int(environ.get('MAX_LIST_ELM', 10))
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "Title: {title} \n Year: {year} \n Rating: {rating} \n Genres: {genres} \n Runtime: {runtime} \n Overview: {overview}")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
USE_ASYNC = is_enabled(environ.get('USE_ASYNC', 'True'), True)
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
BOT_OWNER = environ.get('BOT_OWNER', 'LazyBot')
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "https://{}/".format(FQDN)

# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', ''))

LOG_STR = "Current Cusomized Configurations are:\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
