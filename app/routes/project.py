from flask import Blueprint, request, jsonify
from app import db
from models.project import Project
from models.template import get_project_template
import sqlalchemy
import os

project_bp = Blueprint('project', __name__, url_prefix='/project')

@project_bp.route('/create', methods=['POST'])
def create_project():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description', '')
    if not name:
        return jsonify({'error': 'Projektname erforderlich'}), 400
    # Projekt in zentrale DB anlegen
    project = Project(name=name, description=description)
    db.session.add(project)
    db.session.commit()
    # Dynamische DB für das Projekt anlegen
    db_path = f'project_{project.id}.db'
    db_uri = f'sqlite:///{db_path}'
    engine = sqlalchemy.create_engine(db_uri)
    # Tabellen nach Template anlegen
    for table in get_project_template():
        columns = ', '.join([f"{col[0]} {col[1]} {col[2]}" for col in table['columns']])
        create_stmt = f"CREATE TABLE IF NOT EXISTS {table['table_name']} ({columns})"
        engine.execute(sqlalchemy.text(create_stmt))
    return jsonify({'message': 'Projekt und Datenbank erstellt', 'project_id': project.id})
