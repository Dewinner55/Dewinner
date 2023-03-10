import requests
from bs4 import BeautifulSoup as bs
import csv
import json


def get_html(url):
    responce = requests.get(url)
    return responce.text


def main():
    url = "https://vk.com/aviatravel55"
    return get_data(get_html(url))


def get_data(html):
    soup = bs(html, "lxml")
    print(soup)
    div1lvl = soup.find("div", class_="wi_body")
    text = div1lvl.find("div", class_="pi_text")
    # print(text)
    img = div1lvl.find_all("img")
    list_img = []
    for x in img:
        x = x.get("alt")
        list_img.append(x)
    # print(list_img)
    video = "https://vk.com" + \
        div1lvl.find("a", class_="thumb_link").get("href")

    # return f"\n{text}\n\n{video}\n"


# if __name__ == "__main__":
print(main())

1)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
"""
