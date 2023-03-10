# ls = list(range(0,200,2))
# print(ls)

# ls = []
# for x in range(0,300):
#     if x % 2 == 0 and x % 3 == 0:
#         # print(x)
#         ls.append(x)
# print(ls)

# ls = []
# for x in range(0,100):
#     if x % 2 == 0:
#         ls.append(x**2)
#     else:
#         ls.append(x)
# print(ls)

#  list comperhensions - генераторы списков 
# list comperhensions - упрощенный подход к созданию списков, который задействует цикл for а также конструкции if else для определение условий генерации

# ls = [x for x in range(0,200) if x % 2 == 0]
# print(ls)

# ls = [x for x in range(0,200) if x % 2 == 0 and x % 3 == 0]
# print(ls)

# ls = [x ** 2 if x % 2 == 0 else x for x in range(0,200)]
# print(ls)

# ls = [x ** 3 if x % 2 != 0 else x + 100 for x in range(1,11)]
# print(ls)

# ls = list(range(0,11))
# i = 0
# for x in ls:
#     i += 1
#     if i == 3:
#         i = 0
#         index = ls.index(x)
#         ls.insert(index, "John")
# print(ls)

# ls = [[1,2,3],[4,5,6],[7,8,9]]
# ls = [x + 10 if x % 0 else x ** 2 for inner ls]
# ls = [x + 10 if x % 2 == 0 else x ** 2 for inner in ls for x in inner]
# print(ls)

# from datetime import datetime

# start = datetime.now()
# ls = [x for x in range(1,1_000_000)]

# # for x in range(1,100_000_000):
# #     ls.append(x)

# finish = datetime.now()

# print("Время действия программы: ", finish-start)

# friuts = ["apple", "banana", "kiwi", "mango", "limon", "mandarine"]
# ls = [x for x in friuts if x != "apple"]

# print(ls)

# ls = [x.upper() for x in friuts if not x.startswith ("m")]

# print(ls)

# a = {x for x in range(0,11)}

# print(a)

# print(type(a))

# dict_ = {x: x ** 2 for x in range(0,11)} # DICT {KEY, VALUES for x in rande(0,100)}
# print(dict_)

# dict1 = {
#         "a": 1, 
#         "b": 2, 
#         "c": 3, 
#         "d": 4, 
#         "e": 5, 
#         "f": 6, 
#         "g": 7, 
#         "h": 8
#         }
# new_dict = {k: "odd" if v % 2 != 0 else "even" for k, v in dict1.items()}
# print(new_dict)

name = {}
print(dir(name))