from pyrogram import Client
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
import re
from config import API_ID, API_HASH

def extract_sticker_name(url):
    match = re.search(r'addstickers/(.+)$', url)
    if match:
        return match.group(1)
    return None

def get_user_id(sticker_set_id):
    return sticker_set_id >> 32

# Initialize client
app = Client("my_account", API_ID, API_HASH)

# Request sticker pack URL from user
sticker_url = input("Enter sticker pack URL: ")
sticker_set_name = extract_sticker_name(sticker_url)

if not sticker_set_name:
    print("Invalid URL format")
    exit()

# Get sticker pack information
with app:
    sticker_set = app.invoke(
        GetStickerSet(
            stickerset=InputStickerSetShortName(short_name=sticker_set_name),
            hash=0
        )
    )
    
    sticker_set_id = sticker_set.set.id
    user_id = get_user_id(sticker_set_id)
    
    print(f"Sticker pack ID: {sticker_set_id}")
    print(f"User ID: {user_id}")
