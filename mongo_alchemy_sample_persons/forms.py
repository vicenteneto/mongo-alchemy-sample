from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

from mongo_alchemy_sample_persons.models import Person


class PersonForm(FlaskForm):
    document_class = Person

    name = StringField(validators=[DataRequired()])
    age = IntegerField(validators=[DataRequired()])
    instance = None

    def save(self):
        if self.instance is None:
            self.instance = self.document_class()

        self.instance.name = self.name.data
        self.instance.age = self.age.data
        self.instance.save()

        return self.instance
