from datetime import date, datetime

from bson.objectid import ObjectId

from mongo_alchemy_sample_util.database import db


class Model(db.Document):
    """
    Mixin for retrieving public fields of model in json-compatible format
    """
    __public__ = None

    def to_json(self, exclude=(), extra=()):
        """
        Returns model's PUBLIC data for jsonify
        """
        data = {}
        keys = self._values.items()
        public = self.__public__ + extra if self.__public__ else extra
        for key, field in keys:
            if public and key not in public:
                continue
            if key in exclude:
                continue
            value = self.__serialize(field.value)
            if value:
                data[key] = value
        return data

    @classmethod
    def __serialize(cls, value, follow_fk=False):
        if type(value) in (ObjectId,):
            ret = str(value)
        elif type(value) in (datetime, date):
            ret = value.isoformat()
        elif hasattr(value, '__iter__'):
            ret = []
            for v in value:
                ret.append(cls.__serialize(v))
        elif Model in value.__class__.__bases__:
            ret = value.to_json()
        else:
            ret = value

        return ret
