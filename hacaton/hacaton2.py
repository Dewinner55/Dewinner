import requests
from bs4 import BeautifulSoup
import csv

url = "https://cars.kg/offers"

responce = requests.get(url).text

soup = BeautifulSoup(responce, "lxml")

modely_all = soup.find_all("select", id="m_search_vendor").strip()
print(modely_all)
