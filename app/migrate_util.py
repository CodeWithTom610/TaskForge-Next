from flask_migrate import Migrate
from . import db

migrate = Migrate()

def init_migrate(app):
    migrate.init_app(app, db)
