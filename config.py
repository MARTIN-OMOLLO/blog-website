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
    