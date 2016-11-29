from mongo_alchemy_sample_util.database import db
from mongo_alchemy_sample_util.models import Model


class Person(Model):
    __public__ = ('mongo_id', 'name', 'age')

    name = db.StringField()
    age = db.IntField()
