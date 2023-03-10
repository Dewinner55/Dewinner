# sСоздайте словарь a, где ключами будут названия товаров, а значениями их цены, затем пройдитесь циклом по нему и поменяйте все значения элементов, разделив их на 5.

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# c = {}
# for k, v in a.items():
#     x = v / 5
#     c.setdefault(k, x)
# print(c)

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# c = {}
# for k, v in a.items():
#     b = v / 5
#     c.setdefault(k, b)
# print(c)


# Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным(специальным методом) и распечатайте результат.

# a = {'apple': 2, 'orange': 5, 'banana': 10}
# new_dict = {}
# # a.pop("apple"), a.pop("orange")

# for k, v in a.items():
#     if v % 2 == 0:
#         a.pop(k, v)
# else:
#     print(a)

# print(a)

# a = {'apple': 2, 'orange': 5, 'banana': 10}
# for v in a.values:
#     if v % 2 == 0:
#

# list_ = []

# name1 = input("Введите имя и фамилию: ")
# name2 = input("Введите имя и фамилию: ")
# name3 = input("Введите имя и фамилию: ")
# name4 = input("Введите имя и фамилию: ")
# name5 = input("Введите имя и фамилию: ")

# list_.append(name1)
# list_.append(name2)
# list_.append(name3)
# list_.append(name4)
# list_.append(name5)

# target = " "
# surnames = []

# for x in list_:
#     t = x.find(target)
#     v = x.rfind(target)
#     if x.count(target) > 1:
#         surnames.append(x[v+1:])
#     else:
#         surnames.append(x[t+1:])

# print(sorted(surnames))


# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# str_ = []
# int_ = []

# for x in list_:
#     if type(x) == str:
#         str_.append(x)
#     else:
#         int_.append(x)

# str_ = str(str_)

# for y in str_:
#     if y.isdigit():
#         int_.append(int(y))

# summ = 0

# for t in int_:
#     summ = summ + t

# print(summ)


# 1) Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е. соединение, строк. В остальных случаях введенные числа суммируются.


# a = {'apple': 2, 'orange': 5, 'banana': 10}
# b = a.copy()

# for x,y in b.items():
#     if y % 2 == 0:
#         a.pop(x,y)
# print(a)

# a = {'a': 1, 'b': 2, 'c': 3}
# b = {} for k, v in a.items():
#     b.setdefault(v, k) print(b)
