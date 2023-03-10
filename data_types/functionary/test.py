# print(dir(dict))

# list_ = [1, 2, 3]
# dict_ = {}
# dict_new = dict_.fromkeys(list_, 10)
# print(dict_new)

# func12 = (["hEllo", "wORld"], "lower")


# def func(func12, b):
#     a = []

#     for x in func12:
#         if b == "lower":
#             a.append(x.lower())
#         # print(x)
#         return (a)


# print(func(["Hello", "World"], "lower"))


# def func12(list1, b):
#     a = []
#     for i in list1:
#         if b == 'lower':
#             a.append(i.lower())
#         elif b == 'upper':
#             a.append(i.upper())
#     return (a)


# print(func12(["hEllo", "wORld"], 'lower'))


# print(func12(["hEllo", "wORld"], 'lower'))

# func12 = (["hEllo", "wORld"], "lol")

# for x in func12:
#     print(x)

# myList = ["Hello"]
# myDict = {myList[i]: len(myList[i]) for i in range(len(myList))}
# print(myDict)


# def func13(stroka, k, v, c, s):
#     dict_new = {stroka[i]: len(stroka[i]) for i in range(len(stroka))}

list_ = ["Hello"]
str_ = str(list_)
str_new1 = str_[2:-2]
str_new2 = "".join(str_new1)
list_new = list(str_new2)
print(str_new2)
print(list_new)
print(len(list_new))
# dict_new = {list_new[i]: len(list_new[i]) for i in range(len(list_new)) if list_new.count(i) > 1}
# dict_new = {list_new[i]: len(list_new[i]) for i in range(len(list_new)) if list_new.count(i) > 1}
print(" ")
print(dict_new)


# i = []
# for x in list_:
#     i = i[x]
#     print(i)
