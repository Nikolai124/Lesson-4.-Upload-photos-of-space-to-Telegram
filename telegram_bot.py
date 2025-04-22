from dotenv import load_dotenv
import telegram
import os
import argparse
import random
import time


def main(): 
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='отправка изображений в телеграм'
    )
    parser.add_argument('--delay', help='задержка отправки изображений в телеграм',  default = 14400, type=int) 
    args = parser.parse_args()
    telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=telegram_api_token)
    while True: 
        for dirpath, dirs, filenames in os.walk('images'):
            random.shuffle(filenames)
            for filename in filenames:
                with open(os.path.join('images', filename), 'rb') as file:
                    bot.send_document(chat_id=chat_id, document=file)
        time.sleep(args.delay)


if __name__ == "__main__":
    main()