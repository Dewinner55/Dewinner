from bs4 import BeautifulSoup
import requests
import csv

BASE_URL = f"https://www.mashina.kg/search/all/"


def get_html(url: str) -> str:
    "Получает код определенного сайта"
    response = requests.get(url)
    return response.text


def get_last_page(html: str) -> int:
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.find("ul", class_="pagination").find_all(
        "a", class_="page-link")
    last_page = pages[-1].get("data-page")
    return int(last_page)


def get_data(html: str) -> list:
    "Функция парсер, получает все данные с сайта"
    result = []
    soup = BeautifulSoup(html, "html.parser")
    catalog = soup.find("div", class_="table-view-list")
    cars = catalog.find_all("div", class_="list-item")
    for car in cars:
        name = car.find("h2", class_="name").text.strip()
        try:
            img = car.find("img", class_="lazy-image").get("data-src")
        except:
            img = "Нет картинки"
        price = car.find("p").find("strong").text
        desc1 = car.find("p", class_="year-miles").text.strip()
        desc2 = car.find("p", class_="body-type").text.strip()
        desc3 = car.find("p", class_="volume").text.strip()
        description = f"{desc1} {desc2} {desc3}"
        # print(name, price, description)
        # print(img)
        # print()
        data = {"name": name, "price": price,
                "description": description, "image": img}
        result.append(data)

    return result


count = 0


def write_to_csv(data: dict) -> None:
    "Функция для записи всех данных в csv файл"
    with open("cars.csv", "a") as file:
        fieldnames = ["Name", "Price", "Description", "Image"]
        writer = csv.DictWriter(file, fieldnames)
        global count
        writer.writerow({"№": "№",
                         "Name": "Name",
                         "Price": "Price",
                         "Description": "Description",
                         "Image": "Image"})
        for x in data:
            count += 1
            writer.writerow({
                "№": count,
                "Name": x["name"],
                "Price": x["price"],
                "Description": x["description"],
                "Image": x["image"]
            })


def prepare_csv() -> None:
    "Функция которая подготавливает csv файл"
    with open("cars.csv") as file:
        fieldnames = ["Name", "Price", "Description", "Image"]
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            "№": "№",
            "Name": "name",
                    "Price": "price",
                    "Description": "description",
                    "Image": "image"
        })


def main():
    i = 1
    prepare_csv()
    while True:
        url = f"https://www.mashina.kg/search/all/?page={i}"
        html = get_html(url)
        last_page = get_last_page(html)
        data = get_data(html)
        write_to_csv(data)
        print("Спарсили {i} страницу!")
        if i == 15:
            break
        i += 1


main()

html = get_html(BASE_URL)
data = get_data(html)
write_to_csv(data)
