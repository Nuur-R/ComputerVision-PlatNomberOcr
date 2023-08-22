API_KEY = '6453080762:AAFk3CWyEoXAcckSDqk-tx4bGMt-lCewhyQ'
CHAT_ID = 5119690404

import asyncio
from telegram import Bot
from telegram import InputFile

# Ganti dengan token bot Telegram Anda
BOT_TOKEN = API_KEY

async def send_text_message(chat_id, text):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=text)

async def send_photo_to_user(token, chat_id, photo_path, caption=None):
    bot = Bot(token=token)
    await bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'), caption=caption)



def sendToTelegram(text, photo_path):
    try:
        loop = asyncio.get_event_loop()
        # loop.run_until_complete(send_photo_to_user(API_KEY, CHAT_ID, photo_path, text))
        loop.run_until_complete(send_text_message(CHAT_ID, text))
        print('Pesan foto berhasil dikirim ke obrolan dengan ID:', CHAT_ID)
        
    except Exception as e:
        print("Terjadi kesalahan:", e)
# sendToTelegram('test', 'test_plate/A.jpg')