# Области видимости и пространства имён. Теория
# def func():
#     var = 15
#     return var * 2
# print(func())

# Область видимости и пространства имён (scopes) - определяет контекст переменной, в рамках которой мы можем её использовать

# built-in - (встроенная функция) - print, len. math и.т.д.
# global (глобальна область видимости)
# enclosed (нег лобальная область видимости, nonlocal)
# local (локальная)

# x = 200


# def fucn():
#     print(x, "!")

# fucn()

# a = 10  # global(глобальная зона видимости)


# def hello():  # global(глобальная зона видимости)
#     a = "Hello World!"  # local(локальная зона видимости)
#     print(a, "local inside at func!")


# hello()
# print(a, "global")  # bulit-in(встроенная зона видимости)

# x = "global"
# print(x)


# def enclosed():
# x = "enclosed"  # enclosed
# var = 5

# def local():
# x = "local"  # local
# print(x)
# print(x)
# local(x)
# print(x)


# enclosed()
# print(x)


# a = 10


# def func():
#     print(a)
#     a = "local" # будет ошибка, т.к. переменная а была уже выведена и повтроное использование программа не увидит


# func()


# ------------------ global ------------> он позволяет изменять значения не локальной переменной находясь в локальной области видимости.

# var = 100


# def increment():
# global var
# var += 1


# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)

# def counter():
#     num = 0

#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment


# c = counter()
# print(c)  # <function counter.<locals>.increment at 0x7fa31b082050>
# print(c())
# print(c())
# print(c())
# print(c())


# def counter():
#     num = 0

#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment


# i = counter()

# for x in range(0, 100_000):
#     if x % 3 == 0 and x % 5 == 0:
#         res = i()
#         # print(res)

# print(f"Result: {res}")


# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# globals(), locals()

# a = 5
# b = 6
# c = 7


# def func():
#     john = "john snow"
#     print(locals())


# print(globals())
# print()
# func()
# --------------------------------------------------------------------------------#

# string = "happy birthday!"
# list_ = [x for x in string.split(" ")]
# print(list_)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {
#     'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list_ = [y for k, v in dict_.items for x, y]
# print(list_)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list1 = [y for k, v in dict_.items() for x, y in v.items()]
# print(list1)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}

# for k, v in dict_.items():
#    for x, y in v.items():
#       print(y)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric',
#              'patty', 'yoko', 'cynthia', 'linda', 'jude']
# tuple_ = tuple(list_name)
# print(tuple_)

#   Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом. Программа должна вывести YES, либо NO
#   Вводить в порядке x1, y1, x2, y2

x1 = int(input("Первая клетка: "))
y1 = int(input("Второая клетка: "))
x2 = int(input("Третия клетка: "))
y2 = int(input("Четвертая клетка: "))

for x in x1:
    
