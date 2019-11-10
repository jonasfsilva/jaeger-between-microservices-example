import os
from peewee import *


DATABASE = os.getenv('DATABASE')
print(DATABASE)
db = SqliteDatabase(DATABASE)


class User(Model):
    
    class Meta:
        database = db
        db_table = 'user'

    nome = CharField()
    email = CharField()
    telefone = CharField()
    pais = CharField()
    cidade = CharField()
    endereco = CharField()
    senha = CharField()
    verificado = BooleanField()


User.create_table()
