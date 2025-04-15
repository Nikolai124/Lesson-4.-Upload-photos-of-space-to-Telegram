from dotenv import load_dotenv
from urllib.parse import urlparse
import os 
import argparse
import requests
from download_image import download_image


def receive_expansion(link): 
    link_path = urlparse(link).path 
    expansion = os.path.splitext(link_path)[1] 
    return expansion 


def main(): 
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='загрузка nasa_apod изображений'
    )
    parser.add_argument('--count', help='количество загружаемых изображений',  default = 30, type=int) 
    args = parser.parse_args()
    api_key = os.getenv("NASA_API_KEY")
    url = "https://api.nasa.gov/planetary/apod"
    params = { 
        "api_key": api_key, 
        "count": args.count
    }
    response = requests.get(url, params=params) 
    response.raise_for_status()
    for image_number, nasa_image in enumerate(response.json()):
        link = nasa_image['url'] 
        link_expansion = receive_expansion(link) 
        filename = f"images/nasa_apod_{image_number}{link_expansion}"
        download_image(link, filename) 




if __name__ == "__main__":
    main()