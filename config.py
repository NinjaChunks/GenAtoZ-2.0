import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
PASTEBIN_DEV_KEY = os.getenv("PASTEBIN_DEV_KEY")
PASTEBIN_USER_NAME = os.getenv("PASTEBIN_USER_NAME")
PASTEBIN_USER_PASSWORD = os.getenv("PASTEBIN_USER_PASSWORD")
MAX_FILE_SIZE = 2e8
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")