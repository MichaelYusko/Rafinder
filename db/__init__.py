import config
from peewee import SqliteDatabase

DATABASE = SqliteDatabase(config.DATABASES['default'])
