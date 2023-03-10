# Процесс Сериализцаии

import json

# Использование json.dumps()
dict_ = {
    "name": "John",
    "last_name": "Snow",
    "status": True,
    "age": 24,
    "wife": False,
    "childre": None
}
# print(type(dict_))
# print(dict_)

json_text = json.dumps(dict_)
# print("--------------------- ")
# print(type(json_text))
print(json_text)

# Использование json.dump()
# dict_ = {
#     "name": "John",
#     "last_name": "Snow",
#     "status": True,
#     "age": 24,
#     "wife": False,
#     "childre": None
# }
# print(type(dict_))
# print(dict_)
# print(" ")

# with open("new.json", "w") as file:
#     json.dump(dict_, file)

# with open("new.json", "r") as file:
#     data = file.read()
#     print(data)

users = {
    "name": "John",
    "last_name": "Snow",
    "status": True,
    "age": 24,
    "wife": False,
    "childre": None
}

json_obj = json.dumps(users)
print(json_obj)
