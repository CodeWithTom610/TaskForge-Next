from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate

from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'

bootstrap = Bootstrap5()
migrate = Migrate()

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(Config)
	db.init_app(app)
	migrate.init_app(app, db)
	login_manager.init_app(app)
	bootstrap.init_app(app)

	from .routes import main
	app.register_blueprint(main)
	from . import routes, models
	return app
