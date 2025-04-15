import requests
from urllib.parse import urlparse
from pathlib import Path

def download_image (url, filename, params = ""):
    Path("images").mkdir(parents=True, exist_ok=True) 
    response = requests.get(url, params = params)
    response.raise_for_status() 
    with open(filename, 'wb') as file: 
        file.write(response.content) 


