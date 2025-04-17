from dotenv import load_dotenv
import telegram
import os
import random
import time


load_dotenv()
telegram_api_token = os.getenv("")
bot = telegram.Bot(token=telegram_api_token)
while True: 
    for dirpath, dirs, filenames in os.walk('images'):
        random.shuffle(filenames)
        for filename in filenames:
            bot.send_document(chat_id='', document=open(os.path.join('images', filename), 'rb'))
    time.sleep(14400)

