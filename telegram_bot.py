import telegram
bot = telegram.Bot(token='7710345710:AAHjeBShi6f-4D0idj39aW5_uWRJQF9UzRc')
bot.send_message(chat_id='@erg3i', text="I'm sorry Dave I'm afraid I can't do that.")
bot.send_document(chat_id='@erg3i', document=open('images/EPIC_0.png', 'rb'))