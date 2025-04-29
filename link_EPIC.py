from dotenv import load_dotenv
import os 
import requests
from pathlib import Path
import argparse
from download_image import download_image


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
    url = "https://api.nasa.gov/EPIC/api/natural/images" 
    params = { 
        "api_key": api_key,
        "count": args.count
    }
    response = requests.get(url, params=params) 
    response.raise_for_status()
    for image_number, epic_image in enumerate(response.json()): 
        date = epic_image['date']
        name = epic_image['image'] 
        a = date.split(' ')[0] 
        b = a.split('-') 
        download_link_epic = f"https://api.nasa.gov/EPIC/archive/natural/{b[0]}/{b[1]}/{b[2]}/png/{name}.png" 
        filename = f"EPIC_{image_number}.png"
        file_path = os.path.join(args.path, filename)
        download_image(download_link_epic, file_path, params) 


if __name__ == "__main__":
    main()

