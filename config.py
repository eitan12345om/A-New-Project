import os

class Config():
    SECRET_KEY = 'somuchsecret'
    HOST = 'http://localhost:5000'

class Develop(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or Config.SECRET_KEY
    HOST = os.environ.get('HOST') or Config.HOST
