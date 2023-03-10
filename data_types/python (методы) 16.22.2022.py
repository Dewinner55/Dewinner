"Методы строк"

# print(dir(str)) - "список методов"

"REPLACE"
# "str.replace(старое, новое значение, кол-во") - это метод строк, которое меняет старое значение на новое, если указать количество, то поменяет столько сколько раз мы указали кол-во

# text = "ha ha ha ha"
# result = text.replace("h", "1", 2)
# print(result)

"strip"
# str.strip() - методы строк, которые убирает пробелы в начале и в конце строки
# name = "    hello world     "
# result = name.strip()
# print(result)
# # print(name)
# print(len(result))
# print(len(name))
# str.rstrip - уберает пробелы справа
# text = "   hello world         "
# print(len(text.rstrip()))
# str.lstrip - уберает пробелы слева(в начале)

"ISDIGIT, ISNUMERIC, ISDECIMAL"
# str.isdigit()
# str.isnumeric() - это методы строк, которые проверяют являются ли - Проверьте состоит ли ваша строка полностью из чисел. Вывод: True/False
# str.isdecimal() - это метод строкб которы проверяет состоит ли нша строка только из латиницы или кирилицы

# text = "25"
# print(text.isdigit())
# print(text.isdecimal())
# print(text.isnumeric())
# age = input("Введите свой возвраст")
# print(age.isdigit())


# string = "abracadabra"
# new_string = string.replace("d", "k")
# print(new_string)
# text = "asdasdad---++-a//$"
# print(text.isalpha())

# text_2 = "helloworld"
# print(text_2.isalpha())

"ISALNUM"
# str.insalnum() - это метож бкоторый проверет на то что состоит ли наша строка из чисел и символов датинского или кирилского алфавита

"ISTITLE"
# str.istitle - это метод строк, который проверяет начинается ли каждое слова в строке с верхнего регистра (с большой буквы)

# name = "sultan kek"
# name2 = "Sultan Kek"
# print(name.istitle())
# print(name2.istitle())

"INDEX"
# str.index(values, start, end) - это метод строк который возвращает индекс заданного значения(values)
# text = "dasdasdasdKSAasdasdasdasdasKSWEdasd9312"
# print(text.index("K", 11, 90))
"COUNT"
# str.count(values, start) - метод строк, который считает сколько у нас значений(value) есть в строке

# text = "dsaidasdiiasdaaidsdsadisaid"
# print(text.count("i")) # начинает искать от начало до конца
# print(text.count("i", 5)) # начинает искать с  5 индекса
# print(text.count("i", 5, 9)) # начинает искать с 5 индекса до 9 ( не включетльно)

"FIND"
# str.find(values, start, end) - это метод строк, который же как и метод строк str.index, но не выведет ошибку, если значение(values) нету в строке он просто вернет индекс -1 

# text = "makers bootcamp"
# print(text.find("z"))
# отличие
# text = "makers bootcamp"
# print(text.index("z"))

"SWAPCASE"
# str.swapcase() - это метод строк, который меняет на противоположный регистр (a->A), (A->a)

# text = "asdasdasdas"
# print(text.swapcase())
# text1 = "SASFSFSAFDA"
# print(text1.swapcase())
# text1 = input("введите текст")
# print(text1.swapcase())

"CAPITALIZE"
# str.capitalize - это метод строк который меняет первую букву строки на верхний регистр
# text = "hi my name is Anton"
# print(text.capitalize())

"TITLE"
# str.title() - это метод строк, который переводит начало каждго слова в строке в в ерхний регистр

# text = "hi my name is gustaf"
# print(text.title())

# "SPLIT"
# #  str.split (разделить) - это метлд строк, который переводит в лист при помощи разделителя 
# text = "hi my name is Sultan"
# print(text.split("i"))


# text2 = "hi my name is gustaf"
# print(text2.split())

"JOIN"
# # str.join(str) - это метод строк, который соединяет элементы листа 
list = ["12", "23", "54", "25"]
print("".join(list))

# string1 = "America"
# string2 = "Japan"
# print(string1[0] + string2[0] + string1[3] + string2[2] + string1[-1] + string2[-1])


# is - эт проверка

# string = "mkdsahdjkajkdhasjkdhajshdjlasdjkashjkdhakud"
# result = string[len(string)//2]
# print(result)
# print(len(string))
# print(string[len(string)//2])
# print([len(string)//2])

# num = input()
# char = chr(int(num))
# if char.isalpha():
#     print(f'Это буква {char}')
# else:
#     print(f'Это не буква, а символ {char}')























