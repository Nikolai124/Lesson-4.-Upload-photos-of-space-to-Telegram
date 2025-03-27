from dotenv import load_dotenv
from urllib.parse import urlparse
import os 
from pathlib import Path
import requests
from datetime import datetime


def main(): 
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True) 




if __name__ == "__main__":
    main()


