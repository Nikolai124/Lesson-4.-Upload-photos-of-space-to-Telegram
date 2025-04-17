from dotenv import load_dotenv
import os 
import requests
from download_image import download_image


def main(): 
    load_dotenv()
    api_key = os.environ['']
    url = "https://api.nasa.gov/EPIC/api/natural/images" 
    params = { 
        "api_key": api_key,
        "count": 5 
    }
    response = requests.get(url, params=params) 
    response.raise_for_status()
    for image_number, epic_image in enumerate(response.json()): 
        date = epic_image['date']
        name = epic_image['image'] 
        a = date.split(' ')[0] 
        b = a.split('-') 
        download_link_epic = f"https://api.nasa.gov/EPIC/archive/natural/{b[0]}/{b[1]}/{b[2]}/png/{name}.png" 
        filename = "images/EPIC_{}.png".format(image_number)
        download_image(download_link_epic, filename, params) 




if __name__ == "__main__":
    main()

