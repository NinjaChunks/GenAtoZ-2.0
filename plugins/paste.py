import os
import requests
from pyrogram import Client, filters
from config import PASTEBIN_DEV_KEY, PASTEBIN_USER_NAME, PASTEBIN_USER_PASSWORD

def generate_user_key():
    login_data = {
        'api_dev_key': PASTEBIN_DEV_KEY,
        'api_user_name': PASTEBIN_USER_NAME,
        'api_user_password': PASTEBIN_USER_PASSWORD
    }
    login = requests.post(
        "https://pastebin.com/api/api_login.php", data=login_data)
    if login.status_code != 200:
        raise ValueError("Failed to generate user key")
    return login.text

def paste(message, title="GenAtoZBot"):
    user_key = generate_user_key()
    data = {
        'api_option': 'paste',
        'api_dev_key': PASTEBIN_DEV_KEY,
        'api_paste_code': message,
        'api_paste_name': title,
        'api_user_key': user_key
    }
    r = requests.post("https://pastebin.com/api/api_post.php", data=data)
    if r.status_code != 200:
        raise ValueError("Failed to paste text")
    return r.text

@Client.on_message(filters.text & filters.private)
async def paste_text(client, message):
    try:
        paste_url = paste(message.text)
        await message.reply_text(f"Paste created: {paste_url}", quote=True)
    except ValueError as e:
        await message.reply_text(f"Failed to paste text: {str(e)}", quote=True)
