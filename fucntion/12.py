
# У вас есть список со вложенными списками, выведите самый длинный список и самый короткий

# Например:

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

# Результат:

# max_list[13, 15, 17]
# min_list[0]


# ['a', 'b', 'c', 'x', 'd', 'e', 'f', 'x', 'g', 'h', 'i', 'x', 'j']


# list1 = [1, 2, 3, 4, 5]
# list2 = []
# for v in list1:
#     if v % 2 == 0:
#         list2.append(v)
# print(list2)


# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# i = 3
# while i < len(letters):
#     letters.insert(i, 'x')
#     i += 4

# print(letters)

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# element = 'A'
# step = 2
# while step < len(list_):
#     list_.insert(step, element)
#     step += 3

# print(list_)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# step = 2
# element = "A"
# for x in list_:
#     if step < len(list_):
#         list_.insert(step, element)
#         step = step + 3
# print(list_)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# step = 2
# element = "A"
# # list_ = [x for x in list_]
# # list_new = list_.insert(step, element)
# print(list_)

# list_new2 = [x(list_.insert(step, element)) for x in list_]
# print(list_new2)

# n = int(input())
# if n >= 11 and n <= 14:
#     print(f'На лугу пасется {n} коров')
# else:
#     temp = n % 10
#     if temp == 0 or (temp >= 5 and temp <= 9):
#         print(f'На лугу пасется {n} коров')
#     if temp == 1:
#         print(f'На лугу пасется {n} корова')
#     if temp >=2 and temp <=4:
#         print(f'На лугу пасется {n} коровы')


# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeated = []
# for i in list_:
#     if list_.count(i) > 1:
#         if i not in repeated:
#             repeated.append(i)
# print(repeated)

# Задание 22

# У вас есть список со вложенными списками, выведите самый длинный список и самый короткий

# Например:

# lists = [[0], [1, 3], [5, 7], [9, 11, 1, 1], [143, 13, 15, 17]]
# max_list = max(lists, key=len)
# min_list = min(lists, key=len)
# print(f"max_list {max_list}")
# print(f"min_list {min_list}")

# lists = [[0], [1, 3], [5, 7], [9, 11, 1, 1], [143, 13, 15, 17]]


# max_list = []
# min_list = []

# for x in range(len(lists)-1):
#     if len(lists[x+1]) > len(lists[x]):
#         max_list = lists[x+1]
#     else:
#         max_list = lists[x]

# for x in range(len(lists)):
#     if len(lists[x]) < len(lists[x]):
#         min_list = lists[x-1]
#     else:
#         min_list = lists[x]


# print(max_list)
# print(min_list)


# lists = [[13], [13], [14, 1], [14, 1]]
# max_ = max([x for x in lists], key=len)
# min_ = None
# if len(lists) > 1:
#     min_ = min([x for x in lists], key=len)
#     if max_ == min_:
#         min_ = None
# print(f'max_list {max_}')
# print(f'min_list {min_}')


# Задание 33

# Вам дан список со вложенными списками, выведите тот список, у которого самая большая сумма

# Например:

# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [20]]
# list1 = []
# # Результат:

# # [10, 11, 12]

# # max_ = max([x for x in lists], key=sum)
# # print(max_)

# for x in lists:
#     y = sum(x)
#     list1.append(y)


# list1 = max(lists)
# print(list1)


# with open("text.txt", "r") as file:
#     list_ = []
#     list_1 = []
#     list_2 = []
#     for i in file.readlines():
#         list_.append(len(i))
#     print(list_)
#     file.seek(0)
#     for s in file:
#         list_1.append(len(s.split()))
#     print(list_1)
#     file.seek(0)
#     list_new = list(zip(list_, list_1))
#     print(list_new)
#     list_with_lines = file.readlines()
#     print(len(list_with_lines))


