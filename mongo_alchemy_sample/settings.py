VIEWS = (
    'flask_celery_sample_persons',
)

PROJECT_APPS = VIEWS + (
    'flask_celery_sample',
    'flask_celery_sample_util'
)


class Config(object):
    # Flask
    DEBUG = False
    TESTING = False

    # Flask-WTF
    WTF_CSRF_ENABLED = False

    # Celery
    CELERY_BROKER_URL = 'amqp://xproject:xpr0j3ct@localhost:5672/xprojecthost'
    CELERYD_CONCURRENCY = 1
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    # Flask-MongoAlchemy
    MONGOALCHEMY_DATABASE = 'flask_celery_sample'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
