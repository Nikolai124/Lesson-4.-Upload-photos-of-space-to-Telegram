import requests
import argparse
from download_image import download_image


def main(): 
    parser = argparse.ArgumentParser(
        description='загрузка spacex изображений'
    )
    parser.add_argument('--id', help='id запуска',  default = '5eb87d47ffd86e000604b38a') 
    args = parser.parse_args()
    url = f"https://api.spacexdata.com/v5/launches/{args.id}"
    response = requests.get(url) 
    response.raise_for_status() 
    for image_number, link in enumerate(response.json()["links"]["flickr"]["original"]): 
        filename = "images/spacex_{}.jpg".format(image_number) 
        download_image (link, filename) 




if __name__ == "__main__":
    main()