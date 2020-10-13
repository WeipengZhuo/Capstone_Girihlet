import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = 'b\\'\\xc5>`\\xe3C\\x19\\x13\\xdc\\xeaV\\xefT\\x9d\\xa4x\\xae\\''

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT = True
    SECRET_KEY = 'b\\'\\xc5>`\\xe3C\\x19\\x13\\xdc\\xeaV\\xefT\\x9d\\xa4x\\xae\\''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///local_database.db'

class TestingConfig(Config):
    TESTING = True
