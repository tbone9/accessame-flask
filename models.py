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

class Place(Model):
    id = PrimaryKeyField(null=False)
    name = CharField()
    address = CharField()
    lat = FloatField()
    lng = FloatField()
    user = ForeignKeyField(User, backref='users')
    main_entrance = IntegerField(null=True)
    main_entrance_ratings = IntegerField(null=True)
    bathroom = IntegerField(null=True)
    bathroom_ratings = IntegerField(null=True)
    overall = IntegerField(null=True)
    bathroom_ratings = IntegerField(null=True)

    class Meta:
        db_table = 'places'
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Place], safe = True)
    print("tables created successfully")
    DATABASE.close()
