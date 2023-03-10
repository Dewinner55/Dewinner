from string import digits
# print(digits)
# print(type(digits))
# num = input("Введите число: ")
symbols = digits + "-" + "."
flag = True
while flag:
    is_correct_number = True
    num1 = input("Введите первое число: ")
    for x in num1:
        if not x in symbols:
            print("Вы ввели неправильное число! ")
            is_correct_number = False
            break
    if not is_correct_number:
        continue

    num2 = input("Ввидите второе число")    
    for x in num2:
        if not x in symbols:
            print("Вы ввели неправильное число! ")
            is_correct_number = False
            break
    if not is_correct_number:
        continue
    num1 = float(num1) if "." in num1 else int(num1)
    num2 = float(num2) if "." in num2 else int(num2)
    operator = input("Введите арифмитический знак (+, -, *, /,): ")
    if operator == "+":
        print("Результат: ", num1 + num2)
    elif operator == "-":
        print("Результат: ", num1 - num2)
    elif operator == "*":
        print("Результат: ", num1 * num2)
    elif operator == "/":
        print("Результат: ", num1 / num2)
    else:
        print("Вы ввели неправильный арифмитический знак! ")
    choise = input("Хотите продолжить(yes/no)?")
    if choise.lower().strip() == "no":
        flag = False
        print("пока пока!".title())
    