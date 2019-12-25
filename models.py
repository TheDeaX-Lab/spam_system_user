from peewee import *
from playhouse.apsw_ext import APSWDatabase

db_handler = APSWDatabase('file_spam.db')


class MyModel(Model):
    class Meta:
        database = db_handler


class SendedUser(MyModel):
    from_user_id = IntegerField()
    to_user_id = IntegerField()


tables = [SendedUser]
db_handler.create_tables(tables)
