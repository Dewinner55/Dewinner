# num = int(input())
# d = num % 10
# c = (num//10) % 10
# b = (num//100) % 10
# a = num // 1000
# print(a, b, c, d)
# print(f"Цифра в позиции тысяч равна {a}\nЦифра в позиции сотен равна"


# !!!!!!!!!!!!!
# a, b, c = int(input()), int(input()), int(input())
# if b-a == c-b:
#     print("YES")
# else:
#     print("NO")
# print(c-b)
# a, b, c = int(input()), int(input()), int(input())
# if a == c - b:
#     print("Yes")
# else:
#     print("No")

def func15(a):
    users = [
        {'name': 'Jack', 'age': 35, 'work': 'IT-backend developer'},
        {'name': 'Helen', 'age': 35, 'work': 'Nurse'},
        {'name': 'Bob', 'age': 35, 'work': 'Driver'},
        {'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer'},
        {'name': 'Helga', 'age': 35, 'work': 'IT-HR'}
    ]
    for x in users["IT"]:
        print(x)


func15()
