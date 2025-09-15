# Flask Projekt-Kollaborations-Tool

## Features
- Zwei Hauptdatenbanken (User/Auth und zentrale Projektverwaltung)
- Flask-Login für Authentifizierung
- Flask-Bcrypt für Passwort-Hashing
- Flask-Migrate für Migrationen
- Dynamische Erstellung von Projekt-Datenbanken per Link/Request anhand eines Templates
- Modularer Aufbau: models, routes, config, templates, static

## Setup
1. Python 3.9+ installieren
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
3. Datenbankmigrationen initialisieren:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
4. App starten:
   ```bash
   flask run
   ```

## Hinweise
- Neue Projekte werden per POST auf `/project/create` angelegt.
- Das Template für Projektdatenbanken ist in `models/template.py` definiert.
