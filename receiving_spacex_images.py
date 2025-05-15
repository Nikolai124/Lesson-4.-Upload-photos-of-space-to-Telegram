import requests
import argparse
from pathlib import Path
import os
from download_image import download_image


def get_spacex_images(spacex_images_id):
    url = f"https://api.spacexdata.com/v5/launches/{spacex_images_id}"
    response = requests.get(url) 
    response.raise_for_status() 
    return response.json()["links"]["flickr"]["original"]

def main(): 
    parser = argparse.ArgumentParser(
        description='загрузка spacex изображений'
    )
    parser.add_argument('--id', help='id запуска',  default = '5eb87d47ffd86e000604b38a') 
    parser.add_argument('--path', help='путь к файлу', default="images") 
    args = parser.parse_args()
    Path(args.path).mkdir(parents=True, exist_ok=True) 
    spacex_images = get_spacex_images(args.id)
    for image_number, link in enumerate(spacex_images): 
        filename = f"spacex_{image_number}.jpg"
        file_path = os.path.join(args.path, filename)
        download_image (link, file_path) 


if __name__ == "__main__":
    main()