# Функции высшего порядка - это функция которая в качестве аргумента принимает другую функцию

# Декаратор - это функция которая позволяет без изменения кода обернуть другую функцию для того чтобы расширить функционал обернутой функции


# def decarator(func):
#     print(f"Called Func name: {func.__name__}")  #2: Вызванная функция
#     return func() # 3: идет вызов функции # 6 return "hello"


# def hello():
#     print("Всем привет!") # 4
#     return "Hello"# 5


# def john():
#     print("Hello my name is John Snow!")
#     return "John Snow"


# decarator(hello) # 1:
# decarator(john)
# from typing import Callable


# def banchmark(func: Callable):
#     import time
#     start = time.time()
#     res = func()
#     finish = time.time()
#     print(f"Время выполнения функции {func.__name__}: заняло {finish - start}")
#     return res


# def loop():
#     i = 1
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1
#     return i


# print(banchmark(loop))

# Pythonic way -> @decorator
# Синтаксический сахар -> "это Красота кода"
# Синтаксический сахар использовать необохдимо обернув функцию пример:

# def banchmark(func: Callable):
#     def wrapper():  # 2


# def banchmark(func: Callable):
#     def wrapper():  # 2
#         import time
#         start = time.time()
#         res = func()  # 3
#         finish = time.time()
#         print(
#             f"Время выполнения функции {func.__name__}: заняло {finish - start}")
#         return res
#     return wrapper


# @banchmark
# def loop():  # 4
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1
#     return i


# @banchmark
# def add():
#     i = 0
#     range_number = 1_000_000
#     ls = []
#     while i < range_number:
#         i += 1
#         ls.append(i)
#     return ls


# print(loop())  # 1
# add()


# def strong(func):
#     def wrapper(*args, **kwargs):
#         return "<strong>" + func() + "</strong>"
#     return wrapper


# def div(func):
#     def wrapper(*args, **kwargs):
#         return "<div>" + func() + "</div>"
#     return wrapper


# @div
# @strong
# @div
# def john():
#     return "John Snow"


# print(john())

# def trace(func):
#     def wrapper(*args, ** kwargs):
#         print(f"Trace: вызвана {func.__name__}(),\n{args} {kwargs}")
#         original_result = func(*args, ** kwargs)
#         print(f"Trace: вызвана {func.__name__}(),\nвернула {args} {kwargs}")
#         return original_result
#     return wrapper


# @trace
# def say(name, line):
#     return f"{name}: {line}"


# print(say("John", "Snow"))


# Напишите декоратор repeat, который принимает как именованный аргумент num целое число (количество выполнения декорированной функции) и запускает декорированную функции указанное количество раз.

# def repeat(num):
#     def wrapper(func):
#         def wrapper2(name):
#             i = 1
#             while i <= num:
#                 func(name)
#                 i += 1
#         return wrapper2
#     return wrapper


# @repeat(num=4)
# def function(name):
#     print(f"{name}")


# function("hello")


# def reapet():
#     print("Hello")
#     return reapet


# reapet()()
