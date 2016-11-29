VIEWS = (
    'mongo_alchemy_sample_persons',
)


class Config(object):
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = False
    MONGOALCHEMY_DATABASE = 'mongo_alchemy_sample'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
