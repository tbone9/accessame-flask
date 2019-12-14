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
    # user = ForeignKeyField(User, backref='users')

    class Meta:
        db_table = 'places'
        database = DATABASE

class Rating(Model):
    id = PrimaryKeyField(null=False)
    main_entrance = IntegerField(null=True)
    bathroom = IntegerField(null=True)
    hallways = IntegerField(null=True)
    notes = CharField(null=True)
    place = ForeignKeyField(Place, backref='places')
    user = ForeignKeyField(User, backref='users')

    class Meta:
        db_table = 'ratings'
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Place, Rating], safe = True)
    print("tables created successfully")
    DATABASE.close()
