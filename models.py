from peewee import *
from playhouse.postgres_ext import *

db_handler = PostgresqlExtDatabase("vk_test")


class MyModel(Model):
    class Meta:
        database = db_handler


class SendedUser(MyModel):
    from_user_id = IntegerField()
    to_user_id = IntegerField()


tables = [SendedUser]
db_handler.create_tables(tables)

db_handler = SqliteDatabase("/home/deax/Загрузки/kate.db")


class MyModel1(Model):
    class Meta:
        database = db_handler


class Friends(MyModel1):
    _id = PrimaryKeyField()
    owner_id = IntegerField(null=True)
    friend_id = IntegerField(null=True)
