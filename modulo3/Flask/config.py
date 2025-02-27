import os

SECRET_KEY = os.urandom(32)

basedir = os.path.dirname(os.path.realpath(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'data.db')
#SQLALCHEMY_DATABASE_URI = os.path.join(basedir, 'tmp', 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False