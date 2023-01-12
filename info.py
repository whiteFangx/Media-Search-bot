import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = 'LeoMediaSearchBot'
USER_SESSION = 'User_Bot'
API_ID = 4639219
API_HASH = '8aa6ff17490134bf275616030f46e29e'
BOT_TOKEN = '5131802526:AAHS1NLVo1Qyxo3kT1t1L1NX-spo7a7SHJA'

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = ['@Hitesh0007']
CHANNELS = [-1001538461400]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = -1001531025479
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = "mongodb+srv://jns4638:jns4638@cluster0.qyh3o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = 'cinee'
COLLECTION_NAME = 'channel_files'

# Messages
default_start_msg = """
**Hi, I'm Media Search Bot or ypu can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = "cca8a5e"
CUSTOM_FILE_CAPTION = None if FILE_CAPTION.strip() == "" else FILE_CAPTION
API_KEY = OMDB_API_KEY if OMDB_API_KEY.strip() else None
