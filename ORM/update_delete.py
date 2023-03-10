from model import Product, Category

# ОБНОВЛЕНИЕ ДАННЫХ
# query = Product.update(price=500).where(Product.title=="DG t-shirt")

# print(query)
# query.execute()
# update = Product

# УВЕЛИЧИВАЕМ ВСЕМ ТОВАРАМ ЦЕНУ НА 0.5
# query = Product.update(price=(Product.price + Product.price * 0.5))
# query.execute()

# query = Product.update(price=20000).where(Product.category_id == 1 and Product.category_id == 3)
# query.execute()

# УДАЛЕНИЕ ДАННЫХ
# quere = Product.delete().where(Product.title == "DG t-shirt")
# quere.execute()

# УДАЛЕНИЕ ЧЕРЕЗ ОБЪЕКТ
# product = Product.get(id=42)
# print(product, product.title)
# product.delete_instance()

# query = Product.delete().where(Product.id >= 9)
# print(query)
# query.execute()
