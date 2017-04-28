from peewee import Model
from db import DATABASE


class BaseModel(Model):
    class Meta:
        database = DATABASE
