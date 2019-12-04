import os
import datetime
from peewee import *
from flask_login import UserMixin
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))
else:
    DATABASE = SqliteDatabase('accessame.sqlite')

class User(UserMixin, Model):
    id = PrimaryKeyField(null=False)
    email = CharField(unique=True)
    password = CharField()
    name = CharField()

    class Meta:
        db_table = 'users'
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe = True)
    print("tables created successfully")
    DATABASE.close()
