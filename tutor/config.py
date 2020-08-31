class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:tutor@localhost:5432/tutor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    