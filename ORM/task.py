# for number in range(1,300 + 1):
# # print(number)
# import csv
# import datetime
# import time


# filename = 'rows_300.csv'

# with open(filename, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['№', 'Секунда', 'Микросекунда'])
#     for i in range(1, 301):
#         now = datetime.datetime.now()
#         second = now.second
#         microsecond = now.microsecond
#         print(microsecond)
#         writer.writerow([i, second, microsecond])
#         time.sleep(0.01)
#         now_end = datetime.datetime.now()
#         microsecond_end = now_end.microsecond
#         print(microsecond_end)
#         elapsed_time = microsecond_end - microsecond
#         print(elapsed_time)

# print(microsecond)

# from PIL import Image, ImageDraw
# import random
# # import os

# # Создаем директорию, если ее нет
# # if not os.path.exists('circles'):
# #     os.makedirs('circles')

# # Генерируем случайное количество кругов от 5 до 15
# num_circles = random.randint(5, 15)

# # Создаем и сохраняем каждый круг
# for i in range(num_circles):
#     # Создаем новое изображение с белым фоном
#     img = Image.new('RGB', (200, 200), color='white')
#     draw = ImageDraw.Draw(img)

#     # Генерируем случайный цвет для круга в формате RGB
#     color = tuple(random.randint(0, 255) for x in range(3))

#     # Генерируем случайные координаты и радиус для круга
#     x = random.randint(0, 150)
#     y = random.randint(0, 150)
#     r = random.randint(10, 50)

#     # Рисуем круг с заданными координатами, радиусом и цветом
#     draw.ellipse((x, y, x + r, y + r), fill=color)

#     # Сохраняем изображение в формате PNG
#     filename = f'circles/circle_{i}.png'
#     img.save(filename)

# import csv


# def calc_price(filename: str) -> float:
#     total_price = 0.0

#     with open(filename, 'r') as file:
#         reader = csv.reader(file, delimiter=' ')
#         for row in reader:
#             item_price = float(row[1]) * float(row[2])
#             total_price += item_price

#     return total_price


# filename = 'prices.txt'
# total_price = calc_price(filename)
# print(f'Total price: {total_price:.2f} rubles')

