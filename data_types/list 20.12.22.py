"Тип данных - list(списки)"

# list - изменяемый тип данных, который представляет с собой коллекию какой либо последовательности
# list_ = [12, 23, True, False[12, "astr"], "str", None, [12, []]]
# index y list, 
# list_ = [1,2,7,4,8,10]
# print(list_[0]) # вывели цифру 8
# print(list_[1::2]) #вывели цифры 2 и 8 (срез)

# list_ = [10,5,2,10,[0,0,0,1,0]]
# mini_list = list_[4] # [0,0,0,1,0]
# print(list_[4][3]) 

# str_ = "hello world"
# list_ = list(str_) # list() - фукция
# print(list_) ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# list_ = [1,2,3,4,5,20,True,False, None, "str"]
# lists_len = len(list_) # 10 len - фукция для подсчета элементов
# print(lists_len) # 10

# # turple - неизменяемый тип данныхб являющийся последовательностью элементов, литералами являются запятые и круглые скобки
# turple_ = (1,2,3,4,5) круглые скобки
# list_ = [1,2,3,4,5,] квадратные скобки
# print(turple_)

# RANGE
# range(start, end, step) - это генератор последовательности
# в новой версии питона это тип данных

# range_ = 0,11
# range_2 = range(0,11)
# print(list(range_2))
# print(tuple(range_2))

# циклы(for, while)

# for - это цикk, который работает до конца интерируемого обекта
# while -это цикл, который работает пока условия True

# meshok = ["potato", "tomato", "pomidor"]
# kastrulya = []
# for ovoshi in meshok:
#     print(ovoshi)
#     kastrulya.append(ovoshi)
# print(kastrulya)

# i = "makers_bootcamp"
# for i in "makers bootcamp":
#     print(f"Это буква - {i}")

# "while"
# i = 0
# while i < 10:
#     print(f"hello world, это {i} итерация")
#     i+=1

# BRAK, CONTINUE
# break - это оператор циклов, который ломает цикл и выходит из нее
# continue - это оператор циклов, который пропускает итерацию

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(f"hello world, это {i} итерация")
#     i=i+1

# i = 0
# while i < 10:
#     i = i + 
#     if i == 2:
#         continue
#     print(f"hello world, это {i} итерация")

# for i in range(11):
#     if i ==5:
#         break # ломает цикл и заканчивает его когда i = 5
#     print(f"это {i} итеация")


# for i in range(11):
#     if i ==5:
#         continue # пропускает итерацию когда i = 5
#     print(f"это {i} итеация")

# МЕТОДЫ list
# APPEND()
#list.append(element) - это метод листов, который добавляет указанный элемент в конец листа
# list_ = []
# list___ = list()
# print(list_,list___)
# Способы написание листов

# list_ = []
# for i in range(0,11,2):
#     list_.append(i)

# print(list_)

# list_ = []
# for i in range(11):
#     if i % 2 == 0:
#         list_.append(True)
#     elif i == 0:
#         list_.append(None)
#     else:
#         list_.append(False)
# print(list_)

# list_ = [1,2,3,True,False,None, "Rem"]
# list_.append("Anton")
# print(list_)

# "EXTEND()"
# # list_extend(list2) - метод листов, который расширяет первый лист засчет второго листа
# list_1=[1,2,3]
# list_2=[4,5,6]
# list_1.append(list_2) [1,2,3,[4,5,6]] #добавляет в конец
# list_1.extend(list_2) [1,2,3,4,5,6] #соединяет
# print(list_1)

# "insert()"
# list.insert(index, element) - это метод листовб который на место index добавляет element

# list_ = [0,0,0,0,0,0,0,0,0,0,0,0]
# list_.insert(5, True)
# print(list_)

"index"
# list.index (element, start, end) - это метод листов, который находитс индекс указанного элемента
# list_ = ["nyc", "Moscow", "sp", "bishkek", "Osh"]
# for city in list_:
#     print(f"город - {city} под индексом {list_.index(city)}")                                                   

"POP()"
# list.pop() - это метод листов, который удаляет и возвращает элемент по указанному индексу, если индекс не указать, он удалит последний элемент.

list_ = [1,2,3,12,123,43,12,4,5,"hello"]
pop_element = list_.pop(-1)
# print(list_)
print(pop_element)

# list_ = [1,2,3,12,123,43,12,4,5]
# pop_element = list_.pop()
# print(list_)
# print(pop_element)

# REMOVE

# list.remove(element) - это метод листов, для удаления какого либо элемента, если такого элемента нет то выйдет ошибка
# # 
# list_ = [1,2,3,4,5,6,7,8,9]
# list_.remove(6)
# print(list_) 

# SORT()
# list.sort(key=len, reverse=True) - это метод листов, для сортировки его элементов
# def new_func():
#     list_ = ["sultan", "sanjar", "aigerim", "erkaym"]
#     list_.sort(key=len, reverse=False)
#     print(list_)

'COUNT()'
# # list_.count(element) - это метод листов, который считает сколько elements есть в листе
# list_ = [1,231,31,3,6,2,1,1,34,1,3,1,12,1, "hello", "1", "1", "0"]
# count_list = list_.count(1)
# print(count_list)

"COPY(), DEEPCOTY()"
# list_.copy()- это метод листов, который копирует лист поверхностно
# copy,deepcopy() - это метод листов, который коопирует лист углубленно

# list_ = [1,2,3,4,5,6]
# copy_list = list_.copy()
# list_.append(0)
# print(list_)
# print(copy_list)
