from dotenv import load_dotenv
import telegram
import os
import argparse
import random
import time


load_dotenv()
parser = argparse.ArgumentParser(
        description='отправка изображений в телеграм'
    )
parser.add_argument('--delay', help='задержка отправки изображений в телеграм',  default = '14400') 
args = parser.parse_args()
telegram_api_token = os.environ['']
bot = telegram.Bot(token=telegram_api_token)
while True: 
    for dirpath, dirs, filenames in os.walk('images'):
        random.shuffle(filenames)
        for filename in filenames:
            bot.send_document(chat_id='', document=open(os.path.join('images', filename), 'rb'))
    time.sleep(args.delay)

