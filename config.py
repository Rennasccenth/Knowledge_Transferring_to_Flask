import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_PATH = os.environ.get("DATABASE_PATH")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    pass


class TestingConfig(Config):
    TESTING = True
