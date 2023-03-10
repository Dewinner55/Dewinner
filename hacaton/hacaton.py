import requests
from bs4 import BeautifulSoup
import csv
import time

while True:

    url = "https://enter.kg/computers/noutbuki_bishkek"

    responce = requests.get(url).text

    soup = BeautifulSoup(responce, "lxml")

    data = soup.find_all("div", class_="row")

    list_ = []
    for i in data:
        name = i.find("span", class_="prouct_name").text.strip()
        price = i.find("span", class_="price").text.strip()
        img = "https://enter.kg/computers/noutbuki_bishkek" + i.find(
            "img").get("src")

        list_.append({"Марка": name, "Цена": price, "Фото": img})

    with open("Noutbuki.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Марка", "Цена", "Фото"])

    with open("Noutbuki.csv", "a") as file:
        writer = csv.writer(file)
        for product in list_:
            writer.writerow(
                [product['Марка'], product['Цена'], product['Фото']])
            print(f"\n{product['Марка']} - parsed!\n")
        print("Обновляется каждые 60 минут")

    time.sleep(60*60)
