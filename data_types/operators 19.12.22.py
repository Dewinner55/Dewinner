# Операторы сравнения
# Условные операты
# Логические операторы



# операторы сравнения
# <, >, ==, <=, >=, !=(не равно)
# num1 = 18
# num2 = 15
# print(num1 != num2)
# stroka1 = "hello" (ascii code)
# stroka2 = "world" (ascii code)
# print(ord("h")) (Узнать (ascii code)) с символ = индекс
# print(ord("w")) (Узнать (ascii code))
# print(chr(90)) (Узнать (ascii code)) с индекса = символ



# "ОПЕРАТОРЫ IF / ELSE / ELIF - условные операторы созданы чтобы программа могла выполнять разные участки кода в зависимости от условия"
# text = "Hello world! My name is John"
# if ord(text[0]) == 72:
#     print ("yes")
# else:
#     print("No")



# if <condition>:
# <body if>
# <body if> # сработает только если true
# elif <condition>:
# <body elif>
# elif <condition>:
# <body elif>
# else:
# <body> # сработает только если во всех остальных False



# string = input("enter smt:")
# if string == "Hello":
#     print("hello stranger!") #print пишется снчало табуляции(т.е. пробелы можно и один пробел ввести)
# elif string == "john":
#     print("wtlcome back John Snow")
# elif string == "Mercedez":
#     print("Mersedez Bens S class")
# else:
#     print("совпадения не найдено")
# print("the end")



# # email = input("Enter Email: ")
# password1 = input("Enter password: ")
# if len(password1) < 8:
#     raise Exception("password too short!(password need at least 8 characters!") #raise ошибка, останавливает код
# password2 = input("Enter password confirmation: ")
# if password1 != password2:
#     raise Exception("Passwords did't match!")
# else:
#     print("Successfully signed up!")
# age = input("Введите свой возраст: ")
# if age.isdigit():
#     age = int(age)
#     print(f"Your age: {age}!")
# else:
#     raise Exception("Enter the vailid age(only digits!")
# if age > 170:
#     raise Exception("Invalid age!")
# if age < 1:
#     raise Exception("Invalid age!")
# if age < 18:
#     print(f"Chuvak prihodi cherez {18 - age} let/goda!")
# else:
#     print("Ty prohodish po vozrastu, Welcome!")

#логические операторы
#    and -> логическое и
#    or -> лог или
#    not -> лог отрицание
#операторы идентификации
#       in -> проверяет наличие элемента внутри массива либо строки
#       is -> сравнивает ячкйки памяти
#       == сравниева знfчения
#       is not -> отрицательное сравнение двух ячеек

# my_age = 20
# other_age = 18
# result = my_age == 21 and other_age == 18
#                #  false      # True
#                     # False
# "result = my_age == 21 or other_age == 18"
#                 #  true      # true
#                         # True
# print(result)
# result = not my_age == 21
# print(result)
# cash = input("Enter your cash:") #cash = int(input("Enter your cash:")), можно не писать if cash.isdigit():cash = int(cash)
# if cash.isdigit():
#     cash = int(cash)
# if cash > 1000 and cash < 10000:
#     print("Sredne")
# elif cash >= 10000 and cash < 100_000:
#     print("mnogo")
# elif cash >= 100_000:
#     print("krasavchik")
# else:
#     print("pechalno")
# is_google_user = True
# is_github_user = False
# is_age_less_21 = False
# user_coin = 8000
# if (is_google_user or is_github_user) and (is_age_less_21 or user_coin > 5000):
#     print("Your enter the system")
# else:
#     print("Sorry, you couldn't enter")
# str1 = "Hello world"
# choice = input("Enter the character: ")
# if choice in str1: # in - in -> проверяет наличие элемента внутри массива либо строки
#     print(f"символ {choice} есть в строке: '{str1}'!")
# else:
#     print(f"символа {choice} нет в строке: '{str1}'!")

'''number = int(input(""))
if number > 0:
    print(True)
else:
    print(False)'''

# mark = int(input(""))
# if mark > 90:
#     print("Отлично, Ваша оценка 5!")
# elif mark => 80:
#     print("Здорово, Ваша оценка 4!")
# elif mark => 70:
#     print("Хорошо, Ваша оценка 3!")
# elif mark => 60:
#     print("Вам стоит подучить материал")
# else:
#     print("Вы не сдали экзамен")

# number = int(input(""))
# if number < 0:
#     print(f"negative {number}")
# elif number > 0:
#     print(positive)
# else:
#     print(zero)

# number = int(input(""))
# if number < 0:
#     print(f"negative {number}")
# elif number > 0:
#     print(f"positive {number}")
# else:
#     print(f"zero {number}")

# x = int(input(""))
# y = int(input(""))
# if x/y % 1:
#     print((x/y)%(x/y))
# elif x / y:
#     result = x / y
#     print(True)

#     """
# #   По теме: Логические и условные Операторы
# # """
# """
# 1) Создайте программу, которая будет требовать пароль и проверять, содержатся ли в нем только числа, при этом длина пароля не должна быть менее 8 символов . Если все эти условия выполняются, то программа выдает вам сообщение ‘Ваш пароль сохранен’, если же нет - то программа должна указать необходимое условие для сохранения вашего пароля.

# Например:
# Ввод: Введите пароль: Makers12345
# Вывод: Ваш пароль должен хранить только числа

# Ввод: Введите пароль: a12345
# Вывод: Ваш пароль должен содержать не менее 8 символов
# Ваш пароль должен содержать только буквы


# password = input("Введите пароль; ")
# if password.isalpha() == True:
#     # print("Ваш пароль должен хранить только числа")
#     raise Exception("Ваш пароль должен хранить только числа")
# elif len(password) >= 8:
#     print("Ваш пароль сохранен")
# else:
#     print("Ваш пароль должен содержать не менее 8 символов. Ваш пароль должен содержать только буквы")

# 2) Напишите программу, которая должна рассчитывать средний балл по следующим предметам: математике, английскому языку и литературе. Проходной балл составляет более 69 баллов. Если ученик набрал проходной балл, то ему выдается сообщение о том, что он допущен к экзаменам. Если он не набрал нужное количество баллов, то ему выдается сообщение о том, что у него недопуск к экзаменам.

# Например:
# Ввод: Введите свои баллы по математике, английскому языку и литературе через запятую: 78, 90, 67
# Вывод: Вы допущены к экзаменам. Ваш средний балл составляет 78.3

# bally =
# mathematica =
# english =
# literal = 
# list = int(input(" "))
# print(int(list.split(",")))
# prohodnoy_bal = 69
# if Bally > prohodnoy_bal:
#     print(f"Вы допущены к экзамену, ваш средний бал составляет {prohodnoy_bal}")
# else:
#     print(f"Вы не допущены к экзамену, ваш бал составляет {prohodnoy_bal}")
