# def func15(users):
#     r = []
#     for i in users:
#         if i['work'].startswith('IT'):
#             r.append(f"{i['name']}, скидки в магазине компьютерной техники!\n")
#             h = ''.join(r)
#     # return r
#     return h
#     # print(func15(users))


# users = [
#     {'name': 'Jack', 'age': 35, 'work': 'IT-backend developer'},
#     {'name': 'Helen', 'age': 35, 'work': 'Nurse'},
#     {'name': 'Bob', 'age': 35, 'work': 'Driver'},
#     {'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer'},
#     {'name': 'Helga', 'age': 35, 'work': 'IT-HR'}
# ]
# # func15()
# print(func15(users))


# # r = []
# for i in users:
#     if i['work'].startswith('IT'):
#         r.append(f"{i['name']}, скидки в магазине компьютерной техники!\n")
#         h = ''.join(i for i in r)
# print(h)


# def func16(km, toplivo):
#     n = toplivo / km * 100
#     return f"На {km}км было расходовано {n}л горючего"


# func16(1200, 333)

# def func16(name, overTime):
#     new_list = {"overTime": overTime}
#     for x in list_new:
#         if x["name"] == name:
#             x.update(new_list)
#             # print(type(x))
#             return x


# def func17():
#     for x in employees:
#         x["salary"] = x["salary"] + (x["overTime"] * 200)
#         x.pop("overTime")
#         print(x)
#     return x


# list_new = [
#     {'name': 'Jack', 'salary': 10000},
#     {'name': 'Tom', 'salary': 15000},
#     {'name': 'Jessica', 'salary': 20000},
#     {'name': 'Helen', 'salary': 25000},
#     {'name': 'Peter', 'salary': 30000}
# ]

# func16("Jack", 4)
# func16("Tom", 3)
# func16("Jessica", 9)
# func16("Helen", 2)
# func16("Peter", 7)

# employees = list(list_new)

# print(func17())

# def func17():
#     list_new = []
#     for x in list_:
#         x["salary"] = x["salary"] + (x["overTime"] * 200)
#         x.pop("overTime")
#         list_new.append(x)
#     print(list_new)
#     return x


# employees = [
#     {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#     {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#     {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#     {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#     {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]

# list_ = employees.copy()
# print(list_)
# print("")
# print((employees))
# print("")
# print(id(func17()))
# print("")
# print((employees))
# print("")
# print(list_)


# def func17(lsofdict: dict):
#     for x in lsofdict:
#         if 'overTime' in x:
#             x['salary'] += x['overTime']*200
#         x.pop('overTime')
#     return lsofdict


# print(func17(employees))


# def func17(list_: dict):
#     list_new = []
#     for x in list_:
#         x["salary"] = x["salary"] + (x["overTime"] * 200)
#         x.pop("overTime")
#         list_new.append(x)
#     print(list_new)
#     return list_new


# employees = [
#     {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#     {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#     {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#     {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#     {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]

# print(func17(employees))

# def func18(argument):
#     list_str = []
#     list_int = []
#     for x in argument:
#         if type(x) == int:
#             list_int.append(x)
#         if str == type(x):
#             list_str.append(x)
#     return  list_int, list_str


# list_ = [4, 'dfs', '', 234, 'sdsda', 7, 'sdf']
# func18(list_)
# print(func18(list_))


# def func18(gax):
# str_list = [x for x in gax if str == type(x)]
# num_list = [x for x in gax if int == type(x)]
# return num_list, str_list


# students = [
#     {'student': 'Jack', 'marks': 43},
#     {'student': 'Tom', 'marks': 92},
#     {'student': 'Helen', 'marks': 85},
#     {'student': 'Peter', 'marks': 58},
#     {'student': 'Jessica', 'marks': 78}
# ]


# def func19(list_: list):
#     list_.sort(key=lambda x: x['marks'], reverse=True)
#     return list_


# print(func19(students))


# with open('task1.txt', 'r+') as file:
#     print(file.read())

# with open('task1.txt', 'r') as file:
#     for l in file.readlines():
#         print(l)

import requests
url = "https://stackoverflow.com/questions"
source = requests.get(url).status_code
print(source)
