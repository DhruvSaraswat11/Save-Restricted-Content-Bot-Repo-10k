#Join me at telegram @dev_gagan

from pyrogram import Client
from pyromod import listen
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "26648769"
API_HASH = "7db725993c3f365f1062ab837e55fd1d"
BOT_TOKEN = "7584466845:AAGOLQYdFUb1XOz_EkAhTWezXpDwUQYUzUI"
SESSION = "BQGWoMEAZYabiyFrWwQO3RyiGD-JLy1s4iSNTdYjnHwZ1WugtrLo0R7f95viT5XXBLZzRSDtlKIADcyt2jc0ACXMxowwAf7nZF5eSVpjXrMdjAbgL1DT2-yxtwfZK3Ne_LmmFBbQAFTp6zY9xTMI8U9rpMZU1Uzapk0nfOr4IWxQz5VH68jk02TN3TiBepc0sFo3IXw7sYG470ukaoAMUsU8htOv4Efo4751mjTqcKedrlnKk-105mHeaci8gwl75AVbGVgy7RNTbrw6mywXXa5EXHanjaTs_A8hJCezipZW1YYiW2lcDlHBYzwRkimpniIIytC8pFDdmTVz3gyyytKzasfaAQAAAAGTxNFHAA" 
FORCESUB = "saverestrictedcontent12"
AUTH = "6774116679"
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
