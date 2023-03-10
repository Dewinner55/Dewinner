import csv
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from datetime import datetime

def get_html(url): # сначало надо получить html разметку
    response = requests.get(url) # request помогает нам получить html разметку
    return response.text # получаем html разметку в формате текста

def get_deps_links(html): # получить ссылки дедпутатов
    links = []
    soup = BeautifulSoup(html, "lxml") # при помощью парсера "lxml"
    catalog = soup.find("div", class_ = "grid-deputs") # находим где хранятся все карточки депутатов
    items = catalog.find_all("div", class_ = "dep-item") # находим личные кабинеты карточек депутатов
    for item in items: #  проходимся по каждой карточке депутата
        a = item.find("a").get("href")
        print(a)
        link = "http://kenesh.kg" + a
        links.append(link)
    return links

def get_all_links(): # проходим по всем страницам
    result = []
    for i in range(1,6):
        url = f"http://kenesh.kg/ru/deputy/list/35?page={i}"
        html = get_html(url)
        dep_links = get_deps_links(html)
        result.extend(dep_links)
    return result

def get_deps_data(link):
    html = get_html(link)
    soup = BeautifulSoup(html, "lxml")
    try:
        name = soup.find("div", class_ ="deput-name").text
    except:
        name = "Нет имени!"

    info = soup.find("div", class_ = "deput-info").text.strip()
    info = info.split()
    dep_info = " ".join(info)
    bio = soup.find("div", class_ = "tab-content").text.strip()
    data = {"name": name, "info": info, "bio": bio, "link": link}
    return data

def prepare_csv():
    with open("deputaty.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["ФИО", "Информация", "Биография", "Сыллка на страницу"])

def write_to_csv(data):
    with open("deputaty.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([data["name"], data["info"], data["bio"], data["link"]])
        print(f"{data['name']} - parsed!")

def make_all(link):
    data = get_deps_data(link)
    write_to_csv(data)


def main():
    prepare_csv()
    links = get_all_links()
    # for link in links:
    #     data = get_deps_data(link)
    #     write_to_csv(data)
    with Pool(20) as pool:
        pool.map(make_all, links)

if __name__ == "__main__":
    start = datetime.now()
    main()
    finish = datetime.now()
    print(f"Парсинг занял: {finish - start}")


url = "http://kenesh.kg/ru/deputy/show/196/abdaliev-meykinbek-akimovich"

get_deps_data(url)

