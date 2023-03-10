# Процесс Десериализации
import json

# Использование json.loads()
# with open("new.json", "r") as file:
#     json_data = file.read()
#     print(type(json_data))
#     print(json_data)
#     print("----------------------")
#     dict_ = json.loads(json_data)
#     print(type(dict_))
#     print(dict_)


# Использование json.load()
# with open("new.json") as file:
#     dict_ = json.load(file)
#     print(type(dict_))
#     print(dict_)
json_obj = "null"
python_obj = json.loads(json_obj)
print(python_obj)

# from urllib.request import urlopen
# import json

# url = "https://randomuser.me/api"
# json_data = urlopen(url)

# print(json_data)
# print(dir(json_data))
# print(type(json_data))
# print(json_data.read())

# print("------------------------")

# dict_ = json.load(json_data)
# print(type(dict_))
# print(dict_)
