# Создать 2 скрипт: 1)запишет в файл numbers числ от 1 до 20(вкл) 2)создать скрипт под название squares который будет возводить в квадрат числа из файл numbers

# with open("numbers.txt", "w") as file:
#     data = range(1, 21)
#     for x in data:
#         file.write(f"{x}\n")
# with open("squares", "w+") as file2:
#     with open("numbers.txt") as file1:
#         data = file1.read()
#         data1 = data.split("\n")
#         data1.pop()
#         new_data = list(map(int, data1))
#         for x in new_data:
#             file2.write(f"{x ** 2}\n")

# TASK 3
# with open("task3.txt", "w+") as file:
#     data = range(0, 10)
#     for i in data:
#         file.seek(0)
#         file.write(str(i))
#         file.write("*")
#         "/".join(file)
#         print(i)

# TASK 6
# def read_last(lines, filename):
#     with open(filename) as file:
#         list_ = file.readlines()
#         if lines < len(list_):
#             i = 0
#             reversed_list = list_[::-1]
#             while i < lines:
#                 print(reversed_list[i].replace("\n", ""))
#                 i += 1
#         else:
#             list_.reverse()
#             for i in list_:
#                 print(i.replace("\n", ""))


# read_last(5, "article.txt")


# TASK 7

def longest_words(filename):
    with open(filename) as file:
        list_ = file.readlines()
        long_list = []
        for i in list_:
            if len(i) == len(max(list_)):
                long_list.append(i.replace("\n", ""))
            # if len(long_list) == 1:
            #     return long_list[0]
            if len(long_list) >= +1:
                return long_list


print(longest_words("article.txt"))
