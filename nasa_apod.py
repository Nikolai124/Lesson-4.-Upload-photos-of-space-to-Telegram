from dotenv import load_dotenv
from urllib.parse import urlparse
import os 
import requests
from download_image import download_image


def receive_expansion(link): 
    link_path = urlparse(link).path 
    expansion = os.path.splitext(link_path)[1] 
    return expansion 


def main(): 
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://api.nasa.gov/planetary/apod"
    params = { 
        "api_key": api_key, 
        "count": 30 
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