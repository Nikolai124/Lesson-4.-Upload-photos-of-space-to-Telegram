from dotenv import load_dotenv
from urllib.parse import urlparse
import os 
import argparse
import requests
from pathlib import Path
from download_image import download_image


def get_nasa_apod_images(nasa_image, image_number, path):
    link = nasa_image['url'] 
    link_expansion = receive_expansion(link) 
    filename = f"nasa_apod_{image_number}{link_expansion}"
    file_path = os.path.join(path, filename)
    download_image(link, file_path) 


def receive_expansion(link): 
    link_path = urlparse(link).path 
    expansion = os.path.splitext(link_path)[1] 
    return expansion 


def get_nasa_apod(count, api_key):
    url = "https://api.nasa.gov/planetary/apod"
    params = { 
        "api_key": api_key, 
        "count": count
    }
    response = requests.get(url, params=params) 
    response.raise_for_status()
    return response.json()


def main(): 
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description='загрузка nasa_apod изображений'
    )
    parser.add_argument('--count', help='количество загружаемых изображений',  default = 30, type=int) 
    parser.add_argument('--path', help='путь к файлу', default="images") 
    args = parser.parse_args()
    Path(args.path).mkdir(parents=True, exist_ok=True) 
    nasa_apod_images = get_nasa_apod(args.count, api_key)
    for image_number, nasa_image in enumerate(nasa_apod_images):
        if not nasa_image['media_type'] == 'image':
            continue
        get_nasa_apod_images(nasa_image, image_number, args.path)


if __name__ == "__main__":
    main()