from dotenv import load_dotenv
import telegram
import os
import requests
import argparse
import random
import time


def collect_files(path):
    for dirpath, dirs, filenames in os.walk(path):
        random.shuffle(filenames)
    return filenames

def send_images(filename, bot, chat_id, path):
    with open(os.path.join(path, filename), 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)

def main(): 
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='отправка изображений в телеграм'
    )
    parser.add_argument('--delay', help='задержка отправки изображений в телеграм',  default = 14400, type=int) 
    parser.add_argument('--path', help='путь к файлу', default="images") 
    args = parser.parse_args()
    telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=telegram_api_token)
    while True: 
        try:
            filenames = collect_files(args.path)
            for filename in filenames:
                send_images(filename, bot, chat_id, args.path)
                time.sleep(5)
            time.sleep(args.delay)
        except telegram.error.NetworkError:
            print("Потеряно соединение c интернетом! Следующая отправка будет через пять секунд.")
            time.sleep(5)


if __name__ == "__main__":
    main()