from passlib.apps import custom_app_context as pwd_context
from peewee import CharField

from models import BaseModel


class User(BaseModel):
    name = CharField()
    password = CharField(max_length=128)

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)
