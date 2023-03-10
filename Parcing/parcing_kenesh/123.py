import requests
from bs4 import BeautifulSoup as bs
import csv

def html():
  url = "https://vesti.kg/"
  return url

def get_html(html):
  responce = requests.get(html)
  return responce.text

def soup(get_html):
  soup = BeautifulSoup(html, "html")
  return soup

def main():
  return get_html(html())

print(main())

# url = "https://vesti.kg/"
# responce = requests.get(url).text
# soup = bs(responce, "lxml")
# div1lvl = soup.find("div", class_="itemListView")
# # div2lvl = div1lvl.find("div", class_="itemImageBlock").find(
# #     title="").get("alt")
# # print(div2lvl)
# div2lvl = div1lvl.find_all("div", class_="itemImageBlock")
# # print(div2lvl)
# list_ = []
# for x in div2lvl:
#     b = x.find(title="").get("alt").strip()
#     list_.append(b)
# print(list_)

# div3lvl = div3lvl.find
