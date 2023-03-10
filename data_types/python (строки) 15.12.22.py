"ТИП ДАННЫХ СТРОКИ"

"СТРОКИ - это набор последовательных символов, которые мы используем для хранения и предоставления текстовой информации."
"Индексация = нумерование символов"
# name = "jonh snow"
# "       012345678"
# print(name[5])
# У числов нет Индексации с типом данных int
# age = 25

"ЧТО ТАКОЕ СРЕЗЫ"
"Срезы по индексам - это когда мы получаем определнную часть строки при помощи индекса"
"У срезов есть свои параметры [start : end : step]" 
# name = "jonh snow man"
# snow = name[5:9] (<- мы задали Hачала и Конец выводимых символом используя Индексацию "snow")
# snow2 = name [5:] (<- End не указали поэтому он возьмет до конца "snow man")
# name = name[0:7]
# john2 = name[:4] (<- Start не указали поэтому он возьмет с сначала "john")
# print(name)
# print(john2)
"step - шаг среза, который указывает через сколько символов прохидиться(заданный интервал пропуск символом), также по умолчанию стоит 1"
# print(name[0:13:2]) #"jn nwmn"

# name = "john snow man" 
# reversed_name = name[::-1] #"реверс текста через -1 по параметру step"
# reversed_name = name [:9:-1]
# print(reversed_name)

"СКЛЕИВАНИЕ СТРОК (КОНКАТЕНАЦИЯ)"
# first_name = "sultan"
# second_name = "talaibekov"
# full_name = " " + first_name + " " + second_name
# print(full_name)
# print(full_name * 3)

'''"ФОРМАТИРОВАНЕ СТРОК"
 1) С ПОМОЩЬ %
 2) С ПОМОЩЬЮ (.format())
 3) ИНТЕРПОЛЯЦИЯ СТРОК (f"строка {}") (В начале f, потом внутри текста поставить фигурные скобки{} в скобках поставить переменную)
'''
# name = "john"
# print("привет", name, "как дела")
# print(f"привет {name} как дела")
 
# 1) через %
# name = input("Введите свое имя: ")
# print("Привет, меня зовут", name, "Sultan")
# print("Привет, меня зовут" " " + name + " " "Sultan")
# age = 25
# print("Привет, меня зовут %s Talaibekov, мне %s" %(name, age))

# 2) .format
# name = input("Введите своё имя")
# age = 25
# result = "привет моё имя {}, мне {}" .format(name, age)
# print(result)

# 3) f'строки'
# name = input("Введите свое имя")
# age = 25
# result = f"привет моё имя {name}, мне {age}"
# print(result)

"ЭКРАНИРОВАНИЕ СТРОК"
'''
\n - перенос строки
\t - табуляция (типо делает 4 пробела)
\v - вертикальная табуляция (спускает строку взни но сохраняя позцию по вертикали)
\n\t 
\t\n 
'''
# print("hello\nworld my name is Anton\nI\"m Sabina\" s mom")
# print("hello world\tmy name is Gustaf\v\vI\"m Sabina\" s mom")
# print("hello world\t\nmy name is Gustaf\n\tI\"m Sabina\" s mom")

# len - измеряет количество символов
# name = "dasdasdasdasda"
# print(len(name))

# string = "hello"
# print(string[3:])
# string = "hello"
# print(string[0] + string[4])

# hashtags = "#kers#bootcamp#программирование#it#курсы"

# text = hashtags.replace("#", " ")
# print(text.split())

# name = input("Введите имя")
# last_name = input("Введите фамилию")
# city = input("Введите город")
# age = input("Введите возраст")
# print(f"Вас зовут {name}", f"Ваша фамилия {last_name}", f"Вам {age}", f"Вы проживаете {city}")

# string = "abracadabra"
# new_string = string[5]
# new_string1 = new_string.replace("a", "K")
# print(string[:5] + new_string1 + string[6:]) 
# string = "kilimanjaro"
# print(string[-2:])


# string = "hello world"
# print(string + "\n" + string + "\n" + string)

# string = "Python is the best"
# print(string.startswith("Python")) startswitch - Если нужно определить, начинается ли строка с определенной подстроки, поможет метод startswith(): >

# string = "hello world"
# print(string.split()) Объявите переменную string со значением в виде любой строки, используя пробел. # Разделите строку по разделителю (пробелу) чтобы получился список.

# string = input("Введите значение")
# string1 = "Makers"
# result = f"{string} {string1}"
# print(f"{string} {string1}")

# name = input("Введите свое имя")
# age = 25
# result = f"привет моё имя {name}, мне {age}"
# print(result)

# string1 = "America"
# string2 = "Japan"
# new_string = string1 + string2
# print(new_string)
# print(new_string[0] + new_string[7] + new_string[3] + new_string[9] + new_string[6] + new_string[-1])

# string1 = "America"
# string2 = "Japan"
# print(len(string1))

# string1 = "America"
# string2 = "Japan"
# print(string1[0]+string2[0]+string1[len(string1)//2]+string2[len(string2)//2]+string1[-1]+string2[-1])

# string = "danger"
# print(string[len(string)//2 ])
