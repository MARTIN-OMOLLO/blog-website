import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass

    class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATA_URL')
    


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:martin123@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
    