import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'if you see this, you have control of the universe'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
