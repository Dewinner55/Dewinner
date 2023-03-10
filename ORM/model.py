from playhouse.migrate import migrate, PostgresqlMigrator
import peewee
from main import db
from datetime import datetime


class Category(peewee.Model):
    category_id = peewee.PrimaryKeyField(null=False)
    # unique - сохраняет только один дубликат с названием
    name = peewee.CharField(max_length=50, unique=True)
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'categories'
        order_by = ('created_at',)


class Product(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    title = peewee.CharField(max_length=100)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=100)
    category_id = peewee.ForeignKeyField(
        Category, to_field='category_id', on_delete='cascade', related_name='products')
    crated_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'product'
        order_by = ('created_at',)


db.connect()
Category.create_table()
Product.create_table()

# --------------------------------
# migrate


migrator = PostgresqlMigrator(db)
migrate(
    migrator.alter_column_type('product', 'title', peewee.TextField())
)
