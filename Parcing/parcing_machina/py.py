from bs4 import BeautifulSoup
import requests
import csv
BASE_URL = f"https://www.mashina.kg/search/all/"
response = requests.get(BASE_URL)
soup = BeautifulSoup(response, "lxml")
print(soup)
