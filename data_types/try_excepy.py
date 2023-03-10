# ОБРАБОТКА ИСКЛЮЧЕНИЙ
# ОПЕРАТОР try except

# ОШИБКИ -> СВЯЗАНЫ С КОДОМ
# SyntaxError
# IndentationError
# TabError

# ИСКЛЮЧЕНИЯ -> invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# IndexError
# ValueError
# ImportError
# BaseException -> ПОРОДИТЕТЕЛЬ
#  ВСЕХ ИСКЛЮЧЕНИЙ

# try:
#     <body try>
# except <Exception>:
# <body>
# <else>:
# <body> Только если все окей
# <finaly>:
# <body> В любом случае в конце кода

# try:
#     num1 = int(input("Введите число: "))
#     print(num1)
# except ValueError:
#     print("Important!")

# list_ = [1, 2, 3, 4, 5]
# try:
#     index = int(input("Vedite index: "))
#     res = list_[index]
#     print(res)
# except ValueError:
#     print("Values Errro")
# except IndexError:
#     print("Index Error")
# finally:
#     print("bye")


# try:
#     num1 = int(input("Enter: "))
#     num2 = int(input("Enter: "))
#     result = num1 / num2
# except ZeroDivisionError:
#     print("na 0 delit nelzya")
# except ValueError:
# #     print("invalid symbols for int()!")
# else:
#     print(result)
# finally:
#     print("The End!")

