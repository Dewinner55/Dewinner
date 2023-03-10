import json

# TASK1
# with open("task1.json") as file1:
#     python_obj = json.loads(file1.read())
# with open("task1.py", "w") as file2:
#     file2.write(str(python_obj))

# import json
# file1 = open('task1.json')
# python_obj = json.loads(file1.read())
# file1.close()
# with open('task1.py', 'w') as file2:
#     file2.write(str(python_obj))

# TASK4
# json_obj = "null"
# python_obj = json.loads(json_obj)
# print(python_obj)

# TASK5

# users = [
#     {
#         'name': 'John',
#         'last_name': 'Snow',
#         'age': 26,
#         'has_car': True,
#     },
#     {
#         'name': 'Sam',
#         'last_name': 'Bolt',
#         'age': 4,
#         'has_car': False,
#     }
# ]

# json_users = json.dumps(users)
# print(json_users)

# # TASK 6
# json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'
# print(type(json_products))
# print(json_products)
# print("----------------------------")
# python_obj = json.loads(json_products)
# print(type(python_obj))
# # print(python_obj[0]["rating"])
# list_new = [python_obj[0]["rating"] > 4 if x for x in python_obj else :
#     print(python_obj)
# else:
# print(python_obj)

# list_ = [1, [2, 3, 4, {5: 6, "7": 8}], 9]
# print(list_[1][3]["7"])

import requests
from bs4 import BeautifulSoup
import csv


responce = requests.get("http://www.example.com/").text
my_page = BeautifulSoup(responce, "lxml")

block = my_page.find("h1")
block1 = my_page.find("p")
block2 = my_page.find("a").get("href")
print(block, block1, block2)
