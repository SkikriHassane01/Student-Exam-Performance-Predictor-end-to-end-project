class Config:
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
