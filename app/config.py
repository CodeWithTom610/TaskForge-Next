import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///main.db'
    SQLALCHEMY_BINDS = {
        'projects': os.environ.get('PROJECTS_DB_URL') or 'sqlite:///projects.db'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
