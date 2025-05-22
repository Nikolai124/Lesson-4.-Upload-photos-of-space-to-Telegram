from dotenv import load_dotenv
from datetime import datetime 
from pathlib import Path
from download_image import download_image
import os 
import requests
import argparse


def get_link_EPIC(params):
    url = "https://api.nasa.gov/EPIC/api/natural/images" 
    response = requests.get(url, params=params) 
    response.raise_for_status()
    return response.json()

def main(): 
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='загрузка EPIC изображений'
    )
    parser.add_argument('--count', help='количество изображений которое будет загружено на пк',  default = 5, type=int) 
    parser.add_argument('--path', help='путь к файлу', default="images") 
    args = parser.parse_args()
    Path(args.path).mkdir(parents=True, exist_ok=True) 
    api_key = os.environ['NASA_API_KEY']
    params = { 
        "api_key": api_key,
        "count": args.count
    }
    link_EPIC_images = get_link_EPIC(params=params)
    for image_number, epic_image in enumerate(link_EPIC_images): 
        date = epic_image['date']
        name = epic_image['image'] 
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        formatted_date = date.strftime("%Y/%m/%d")
        download_link_EPIC_images = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{name}.png" 
        filename = f"EPIC_{image_number}.png"
        file_path = os.path.join(args.path, filename)
        download_image(download_link_EPIC_images, file_path, params) 


if __name__ == "__main__":
    main()

