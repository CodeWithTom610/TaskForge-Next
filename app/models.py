
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

def get_db():
	from . import db
	return db

def get_login_manager():
	from . import login_manager
	return login_manager

class User(UserMixin, get_db().Model):
	id = get_db().Column(get_db().Integer, primary_key=True)
	username = get_db().Column(get_db().String(64), unique=True, nullable=False)
	email = get_db().Column(get_db().String(120), unique=True, nullable=False)
	password_hash = get_db().Column(get_db().String(128))

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

get_login_manager().user_loader(lambda user_id: User.query.get(int(user_id)))
