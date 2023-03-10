# ORM (Object-Relational Mapping) - технология программирования, благодаря которой разработчики могут исопользовать язык программировния для взаимодейсвтия с реляцмонной базой данных (PostgresSQL, MySQL, OracleDB). Вместо того чтобы писать сырые запросы на операторах на языках SQL, вы будете писать код на ООП на языке программирования.Это очень сильно ускоряет разработку приложения и базы данных, особенно на начальных этапах.

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(database='orm',
                        user='lenova',
                        password='1',
                        host='localhost',
                        port=5432)
# db.connect()


