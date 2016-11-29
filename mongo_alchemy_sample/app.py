from importlib import import_module

from flask import Flask
from flask_cors import CORS

from mongo_alchemy_sample import settings
from mongo_alchemy_sample.settings import VIEWS
from mongo_alchemy_sample_persons.models import Person
from mongo_alchemy_sample_util.constants import ErrorMessages
from mongo_alchemy_sample_util.database import db


def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        app_config = getattr(settings, config + 'Config')()
        app.config.from_object(app_config)

    CORS(app)
    db.init_app(app)

    __load_application_base()
    __register_blueprints(app)
    __register_error_handlers(app)

    return app


def __load_application_base():
    if not Person.query.all():
        first_person = Person(name='Vicente', age=25)
        first_person.save()


def __register_blueprints(app):
    views = [import_module(module_name + '.views') for module_name in VIEWS]
    for view in views:
        app.register_blueprint(view.blueprint)


def __register_error_handlers(app):
    app.register_error_handler(400, __handle_bad_request)


def __handle_bad_request(exception):
    form = exception.form

    message = ErrorMessages.DOES_NOT_SATISFY_ALL_VALIDATORS
    for field, errors in form.errors.items():
        for error in errors:
            message += '%s - %s' % (getattr(form, field).label.text, error)

    return message
