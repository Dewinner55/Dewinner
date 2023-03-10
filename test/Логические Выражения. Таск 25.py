# Задание 25

# Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом. Программа должна вывести YES, либо NO
# Вводить в порядке x1, y1, x2, y2


# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2):
#     print('YES')
# else:
#     print('NO')


# Задание 24

# Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.
# Вводить в порядке x1, y1, x2, y2

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if x1 == x2 and y1 != y2 and x1 != 0 and x2 !=0 and y1 != 0 and y2 != 0:
#     print("YES")
# elif y1 == y2 and x1 != x2 and x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0:
#     print("YES")
# else:
#     print("NO")

# Задание 23

# На уроке физкультуры тренер говорит «на первый-второй рассчитайтесь». Запросите у пользователя номер человека. Что он скажет, «первый» или «второй»?

# рассчитайтесь = int(input("на первый-второй рассчитайтесь: "))

# if рассчитайтесь % 2 != 0:
#     print("Первый")
# else:
#     print("Второй")

# Задание 22

# Для данного числа n(input, < 100) закончите фразу “На лугу пасется...” одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

# Task 24

# Даны две переменные string1 = "America" и string2 = "Japan".

# Выведите новую строку в который будут записаны первый, средний и последний элемент двух переменных.

# Необходимо использовать срезы.

# Вывод: "AJrpan".

# string1 = "America"
# string2 = "Japan"
# string3 = string1[0:1] + string2[0:1]
# string4 = string1[-1] + string2[-1]
# # # string5 = string1[int((len(string1)/2))]
# # # string6 = string2[int((len(string2)/2))]
# print(string3 + string1[int((len(string1)/2))] + string2[int((len(string2)/2))] + string4)
# # # print(string3 + string5 + string6 + string4)


# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# ls = []

# for i in colors:
#     ls.append(i[::-1])
#     ls = sorted(ls, key=len)
# print(ls)

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# ls = []

# for i in colors:
#     ls.append(i[::-1])
#     ls = sorted(ls)
# print(ls)

# dict_ = {'Bootcamp': 8, 'Makers': 8, 'coding': 6, 'hello': 5}
# max_ = max(dict_.values())
# for k in dict_.keys():
#     if dict_[k] == max_:
#         print(k)

# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# list_ = [v["likes"] for k,v in dict_.items() if v['rating'] > 3]
# print(sum(list_))


# dict_ = {'Dasha': {'likes': 15,'comments': [{'id': 1, 'text': 'some text'},{'id': 2, 'text': 'some text'},],'rating': 2},
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# list_ = [v2["id"] for v in dict_.values()
#          for v2 in v["comments"] if len(v["comments"]) > 3]
# print(list_)


# list_ = [z["id"] for x,v,z in dict_.items() if z["comments"] > 3]


# Задание 22

# Для данного числа n(input, < 100) закончите фразу “На лугу пасется...” одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

# n = int(input("Введите число: "))

# if n < 100:
#     if n == 1 and n == 21 and n == 31
# print(n)

# n = int(input())

# if n >= 11 and n <= 14:
#     print(f'На лугу пасется {n} коров')
# else:
#     temp = n % 10
#     if temp == 0 or (temp >= 5 and temp <= 9):
#         print(f'На лугу пасется {n} коров')
# if temp == 1:
#     print(f'На лугу пасется {n} корова')
# if temp >= 2 and temp <= 4:
#     print(f'На лугу пасется {n} коровы')

# n = int(input())
# if n >= 11 and n <= 14:
#     print(f'На лугу пасется {n} коров')
#     else:
#         temp = n % 10
#         if temp == 0 or (temp >= 5 and temp <= 9):
#         print(f'На лугу пасется {n} коров')
#     if temp == 1: print(f'На лугу пасется {n} корова')
#     if temp >=2 and temp <=4:
#         print(f'На лугу пасется {n} коровы')

# n = int(input())
# if n >= 11 and n <= 14:
#     print(f'На лугу пасется {n} коров')


# a1, b1, c1 = int(input()), int(input()), int(input())
# c = max(a1, b1, c1)
# b = min(a1, b1, c1)
# a = sum([a1, b1, c1]) - min(a1, b1, c1) - max(a1, b1, c1)
# if c >= a + b: print('impossible')
# elif c**2 == a**2 + b**2: print('rectangular')
# elif c**2 < a**2 + b**2: print('acute')
# elif c**2 > a**2 + b**2: print('obtuse')
