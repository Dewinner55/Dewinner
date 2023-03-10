# zip(iterables) - она соедигяет каждый элемент итерируемых объектов между собой, по их распорядку, в тип данных tiple и возвращает его

# ls1 = [1, 2, 3]
# ls2 = [4, 5, 6, 7, 8, 9]

# res = list(zip(ls1, ls2))
# print(res)


# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500]
# ls3 = [10, 20, 30]

# res = list(zip(ls1, ls2, ls3))

# print(res)


# zip для создания словарей

# a = dict([(1, 2), [3, 4]])
# print(a)
#            {1;2,3:4}.items()
#             dict_items[(1,2),[3,4]]

# d_keys = ("hostname", "location", "vendor", "model", "IOS", "IP")
# d_values = ["apple_r1", "winterfall", "jobs", "watch", "16,0", "10.255.0.1"]

# res = list(zip(d_keys, d_values))
# res2 = list(zip(d_values, d_keys))

# print(" ")
# print(res)
# print(" ")
# print(res2)

# d_keys = ["hostname", "location", "vendor", "model", "IOS", "IP"]
# d_values = ["apple_r1", "winterfall", "jobs", "watch", "16,0", "10.255.0.1"]

# i = 0
# res3 = {}

# for x in d_keys:
#     res3[x] = d_values[i]
#     i += 1
# print("")
# print(res3)

# d_keys = ["hostname", "location", "vendor", "model", "IOS", "IP"]
# data = {
#     "r1": ["london_r1", "New Globa Walk", "Cisco", "4451", "15,4", "10.255.0.1"],

#     "r2": ["london_r2", "North West", "Cisco", "5541", "16", "10.255.0.2"],

#     "sw1": ["london_sw11", "East West", "Cisco", "3850", "16,4", "10.255.0.3"]
# }

# for k in data:
#     # print(k)
#     data[k] = dict(zip(d_keys, data[k]))
#     print(data[k])
# print(data)

"_______________________________________________________________________________________"
# all(), any()

# all(iterable) - Возвращает Trueб если все элементы внутри объекта истинна, иначе возвращает False

# all([1, 2])
# print(all([1, 2]))  # True
# all([])
# print(all([]))
# print(all([[]]))
# print(all([[1, 2, 3], 5, None]))
# print(all([[1, 2, 3], 5, True]))
# print(all([[1, 2, 3], 5, True, -1, None]))  # None вернет False

# ip = "10.10.10.10"

# result = all(i.isdigit() if len(ip.split('.')) ==
#              4 else False for i in ip.split("."))
# print(result)
# res = (i.isdigit() for i in ip.split(".") if len(ip.split('.')) ==
#             4)
# print(tuple(res))

# any - возвращает True если есть хотябы один элемент со значение Истинна

# ls = [0, 0, 0, "", False]
# print(any(ls)) # вернул False, т.к. нет ни одного True

# ls = [0, 0, 1, "", False]
# print(any(ls)) # Вернул True, т.к есть один True

# ignore = ["rm -rf", "reset", "alias"]
# command = input("Введите комманду: ")

# if any(word in command for word in ignore):
#     raise Exception("Invalid command")
# print("Vse Ok!")

# a = "rm -rf"
# b = a in ignore
# print(b)


# result = all(i.isdigit() if len(ip.split('.')) == 4 else False for i in ip.split("."))

# myList = ["Hello"]
# myDict = {myList[i]: len(myList[i]) for i in range(len(myList))}
# print(myDict)


# def func13(stroka, k, v, c, s):
#     dict_new = {stroka[i]: len(stroka[i]) for i in range(len(stroka))}

# def func13(list_new):
#     # list_new = str(list_new)
#     # list_new = list_new
#     # list_new = "".join(list_new)
#     # print(" ")
#     # print(list_new)
#     # list_new = list(list_new)
#     # print(" ")
#     # print(list_new)
#     dict_new1 = {i: list_new.count(i) for i in list_new}
#     return dict_new1


# print(func13("Hello"))


# def func14(list_new):
#     dict_ = {}
#     for k in list_new:
#         dict_.setdefault(k, list_new.count(k))
#     return dict_


# print(func14("Hello"))
