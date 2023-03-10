# встроенные функции

# map
# filter
# lambda
# enumerate
# zip,all,any
# (reduce)

# Анонимные функции:
# lambda() - (такие же функции только без названия)
# lambda функции могут принимать сколько-угодно аргументов ,но всегда возвращюат одно выражение

# def sum_of_args(a, b, c):
#     res = a+b
#     return res


# print(sum_of_args(1, 2, 3))

# a = sum_of_args
# print(a(5, 15, 30))

# sum_of_args2 = lambda a, b, c: sum([a+b+c])
# print(sum_of_args2(5,15,20))

# x = lambda a,b,c: (a * b) % c
# print(x(11,5,10))

# get_last = lambda ls: ls[-1]
# ls = [1,2,3,4,5,6, True, False, [123], "last"]
# print(get_last(ls))

# def my_func(n):
#     return lambda a: a * n


# my_doubler = my_func(2)
# my_triple = my_func(3)
# print(my_doubler(100))
# print(my_doubler(50))
# print(my_triple(55))


# dict_ = {"John": 50_000, "Sultan": 5, "Jamie": 1000, "Aigerim": 1_000_000}
# result = dict(sorted(dict_.items(), key=lambda x: x[1], reverse=True))
# res = dict(map(lambda x: (x[0], str(x[1])), result.items()))
# result2 = sorted(dict_.items(), key=lambda x: x[1])
# print(result)
# print(result2)
# print(res)


# dict_ = {"John": {"adress": "moskva", "cash": 50_000},
#         "Sultan": {"adress": "piter", "cash" 5},
#         "Jamie": {"adress": "omsk", "cash": 1000},
#          "Aigerim": {"adress": "bishek" "cash": 1_000_000}}

# print()


# map(function, iterable) применяет фукнцию к каждому элементу из последовательности и возвращает mapobject(итератор) c результатом

# ls = ["one", "two", "three", "four"]

# for i in range(0, len(ls)):
#     ls[i] = ls[i].upper()

# print(ls)


# ls = ["one", "two", "three", "four"]
# res = list(map(str.upper, ls))
# print(type(res))
# print(res)


names = ["john", "sultan", "jamie", "raychel"]

res = list(map(lambda name: f"Hello mr/mrs {name}", names))

print(type(res))
print(res)

# dict_ = {1: 2, 3: 4, 5: 6, 7: 8}

# for key in dict_:
#     dict_[key] = str(dict_[key])

# print(dict_)

# res = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(res)


# filter(function, iterable) - применяет ко всем элдементам iterable функцию которую мы передали и возвращает итератор с теми элементами для которых функция вернула True

# ls = ["one", "two", "", "list", "100", "john", "1"]
# res = []

# for x in ls:
#     if x.isdigit():
#         res.append(x)
# print(res)

# result = list(filter(str.isdigit, res))
# print(result)

# ls = ["john", "makers", "sultan", "ono", "py26"]
# res = list(filter(lambda stroka: len(stroka) > 5, ls))
# print(res)

# res2 = []
# for x in ls:
#     print(x)
#     if len(x) > 5:
#         res2.append(x)
# print(res2)


# ls = [
#     {"name": "Python", "point": 10},
#     {"name": "C++", "point": 6},
#     {"name": "JS", "point": 8}
# ]

# res = list(filter(lambda dict_: dict_["point"] >= 7, ls))
# print(res)

# users = [
#     {"username": "john", "comments": ["I love you", "Really good"]},
#     {"username": "Raychel", "comments": []}
# ]

# inactive_users = list(filter(lambda dict_obj: not dict_obj["comments"], users))
# print(f"\n Все пользователи {users}")
# print(f"\n Не активные пользователи: {inactive_users}")

# names = ["Raychel", "Sultan", "Aigerim", "John", "Kira", "Bob"]
# new_names = list(
#     map(lambda name: f"Your name is {name}!", filter(lambda x: len(x) > 4, names)))

# print(new_names)

# from functools import reduce

# ls = [1, 2, 3, 4, 5, 6]
# sum_ = reduce(lambda a, b: a+b, ls)
# print(sum_)


# ls = ["john", "sultan", "katana"]
# for x, v in enumerate(ls):
#     print(f"\v{type(x)}")
#     print(x, v)
#     print(type(v))
# for x in enumerate(ls):
#     print(x)
# for x in ls:
#     print(x)


# import string as s
# import random


# def generate_rand_str():
#     # Храняться символы в верхнем и нижмем регистре
#     symbols = s.ascii_letters + s.digits
#     result = "".join(random.choice(symbols) for i in range(1, 11))
#     return result


# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())


# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symbols = "_()$!%+-@#"
# q_pass = int(input("Vvedite kol-vo password: "))

# result = {
#     f(choices(ascii_letters, k=10), choices(digits, k=5), choices(symbols, k=2))
#     for f in repeat(lambda x, y, z: "".join(set(x+y+z)), q_pass)
# }

# print(result)
# print(f"Quantity of wasswords: {len(result)}")

# from statistics import mean

# dlina = [len(x) for x in result]
# print(f"Average len: {mean(dlina)}")

a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)
