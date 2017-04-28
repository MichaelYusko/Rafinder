from db import DATABASE
from models.user import User


def create_db():
    DATABASE.create_tables([User])


if __name__ == '__main__':
    create_db()
