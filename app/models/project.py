from app import db

class Project(db.Model):
    __bind_key__ = 'projects'
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.Text)
    # Weitere Felder nach Bedarf
