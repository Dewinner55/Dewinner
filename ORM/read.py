import peewee
from model import Product, Category


def get_all_categories():
    return Category.select()


def get_all_products():
    return Product.select()


print(get_all_categories())
print(get_all_products())

# print()
# categories = get_all_categories()
# print("Категории в Базе Данных: ")
# for x in categories:
#     print(type(x))
#     print(x)
#     print(x.name)
#     print(x.created_at)

# print()
# product = get_all_products()
# print("Категории в Базе Данных: ")
# for x in product:
#     print(type(x))
#     print(x)
#     print(x.title, x.price, x.category_id.name)
#     print()

# products = get_all_products()
# category = int(input("Введите категорию (1-платья, 2-джинсы, 3-футболки, 4-свитеры, 5-обувь): "))
# for x in products:
#     if x.category_id.category_id == category:
#         print(x.title, x.price, x.category_id.name)

category_name = input("Введите title категории: ").lower().strip()
try:
    category = Category.get(name=category_name)
except peewee.DoesNotExist:
    print("Такой категории нет!")
else:
# print(category)
# print(type(category))
# print(category.category_id, type(category.category_id))
    print(category.products)
    for x in category.products:
        print(f"Товар {x.title}, Цена {x.price}, Категория {x.category_id.name}")