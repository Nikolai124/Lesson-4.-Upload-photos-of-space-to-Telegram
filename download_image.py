import requests


def download_image (url, filename, params = ""):
    response = requests.get(url, params = params)
    response.raise_for_status() 
    with open(filename, 'wb') as file: 
        file.write(response.content) 

