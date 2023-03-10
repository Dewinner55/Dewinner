# [Работа с файлами]

# [Каретка - Указатель\Курсор]

# [open(<путь до файла>)]

# [file = open("/home/legion/Desktop/py26/Files/files.py") - Абсолютный путь]

# [file = open("files.py") - относительный путь
# ~ working -> Desktop/py26/files/files.py]

# file = open("Files.py")
# data = file.read()

# print(data)
# print(type(data))

# file.close()

# Режим работы с файлами
#  r/r+ (read)
#  w/2+ (write)
#  a/a+ (append)

# file = open("test.txt", "r")

# print(file.read())

# file.close()

# file = open("test.txt", "r")
# data = file.readlines()

# print(data)
# print(type(data))
# print(len(data[0]))

# file.close()

# file = open("test.txt", "r")

# print(file.readline())

# print("!!!")
# print(file.read())

# file.close()

# Контекстный менеджер
# with open("test.txt", "r") as file:
#     data = file.read()

#     print(data)
#     print(file, "Insite")

# print(file.read(), "Ousite")

# with open("test.txt", "r") as file:
#     data = file.read(5)
#     print(type(data))
#     print(data)
#     print("")
#     print(type(file))
#     print(file.read())
#     print(file.tell())

# file.tell() - Возвращает ИНДЕКС где находиться
# УКАЗАТЕЛЬ(крусор)
# file.seak(index) - перемещает КУРСОР на ИНДЕКС который вы передали

# with open("test.txt", "r") as file:
#     print(file.readline())
#     file.seek(5)
#     print(file.readline())
#     file.seek(5)
#     a = file.read()
#     print(file.readline())

# print(a)

# test1 создает новый файл для записи, если файл с названием не был найден
# with open("test.txt", "w") as file:
#     file.write("Pervaaya strochka!\n")
#     file.write("He is bastard of Ned Stark!\n")
#     file.write("this is lesson about files!\n")
#     # file.seek(10)
#     data = ["Pervaya strochka!\n", "He is bastard of Ned Stark!\n",
#             "This is lesson about files!\n"]
#     file.writelines(data)

# with open("test.txt", "a") as file:
#     file.write("John Snow in North King!\n")
#     file.write("You know nothing John Snow!\n")
#     print(file)

# file = open("test.txt")
# data = file.read()
# print(data)

# with open("test.txt", "a+") as file:
#     file.write("John Snow in North King!\n")
#     file.write("You know nothing John Snow!\n")
#     file.seek(10)
#     print(file.read())

# try:
# except ImportError:
#     import Image
# import pytesseract
# import re


# def get_imei_code(image):
#     string = pytesseract.image_to_string(image)
#     # print(string)
#     # print(type(string))
#     list_of_imei = re.findall(r"IMEI\d.\s\d+", string)
#     print(list_of_imei)

#     with open("imei_codes.txt", "w") as file:
#         file.writelines(x+"\n" for x in list_of_imei)
#         # for x in list_of_imei:
#         #     file.write(f"{x}\n")
#     file = open("imei_codes.txt")
#     data = file.read()
#     print(data)


# image = "unnamed.jpg"
# get_imei_code(image)
