# Космический Телеграм

Данный проект служит для загрузки в Telegram фотографий космоса. Загружая изображения на пк и отправляя каждые 4 часа одно изображение.

### Как установить

Для работы программы нужны 2 ключа. 1 ключ для API его можно получить на сайте NASA. (https://api.nasa.gov/) - сайт NASA
2 ключ для телеграм бота его можно получить при регистрация бота в Telegram. (https://way23.ru/регистрация-бота-в-telegram.html) - ссылка на пошаговую инструкцию.

Создайте файл под названием '.env' и впишите в него свои ключи. (https://www.geeksforgeeks.org/how-to-create-and-use-env-files-in-python/) - ссылка на инструкцию по создании .env файла

Затем в файле 'nasa_apod.py' на 22 строке в скобках напишите название своего ключа для загрузки изображений nasa_apod.
Тоже самое сделайте в файле 'telegram_bot.py' на 9 строке в скобках напишите название своего ключа для отправки изображений в телеграм канал.

Незабудте написать свой chat_id на 15 строке в файле "telegram_bot.py". (https://lumpics.ru/how-find-out-chat-id-in-telegram/)  - ссылка на инструкцию по поиску chat_id.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить проект

Для загрузки изображения 'nasa_apod' нужно запустить файл "nasa_apod.py". Изображения 'nasa_apod' можно скачать по дефолтному количеству изображений и по своему количеству изображений. Дефолтный вариант запуска:
```
python nasa_apod.py
```
Вариант запуска по своему количеству изображений:
```
python nasa_apod.py --count своё количество изображений
```
Для загрузки изображения 'spacex' нужно запустить файл "fetch_spacex_images.py". Изображения 'spacex' можно скачать по дефолтному id и по своему id. Дефолтный вариант запуска:
```
python fetch_spacex_images.py
```
Вариант запуска по своему id:
```
python fetch_spacex_images.py --id
```
Для отправки изображений в телеграм канал нужно запустить файл "telegram_bot.py":
```
python telegram_bot.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).