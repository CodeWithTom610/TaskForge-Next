from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from config import Config

# Extensions
login_manager = LoginManager()
bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Blueprints importieren
    from routes.auth import auth_bp
    from routes.project import project_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(project_bp)

    return app
