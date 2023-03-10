# Задание 23

# Вам дан список, напишите код, который будет соединять в новый список элементы по n-ному шагу


# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# list1 = [list_[i::step] for i in range(len(list_)) if i < step]
# print(list1)


# size = 3
# list_ = []
# for i in range(size):
#     list_.insert(i, list(range(1, size + 1)))
# print(list_)


# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# for i in colors1:
#     for j in colors2:
#         if i == j:
#             colors1.remove(i)
#             colors2.remove(j)
#             continue
# print(colors1)
# print(colors2)


# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# resc1 = []
# resc2 = []
# for i in colors1:
#     if not i in colors2:
#         resc1.append(i)
# for k in colors2:
#     if not k in colors1:
#         resc2.append(k)
# print(resc1)
# print(resc2)

#   Вам дан список с элементами, добавьте элемент, который хранится в переменной element в этот список после каждого n-ого шага

# # Например:

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# step = 2
# element = 'A'
# for x in list_:
#     list_.insert(step, element)
#     print(list_)


# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = [list_[i::step] for i in range(len(list_)) if i < step]
# print(list1)

# list_1 = []
# list_2 = []
# list_3 = []
# list_4 = []
# for i in list_:
#     list_1.append(i)
# print(list_1)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# step = 2
# element = "A"
# for x in list_:
#     if step < len(list_):
#         list_.insert(step, element)
#         step = step + 3
# print(list_)


list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
step = 2
element = "A"
list_1 = [x for x in list_]
print(list_1)
