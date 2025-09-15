# Hier wird das Template für neue Projektdatenbanken definiert
# Beispiel: Tabellenstruktur für ein neues Projekt

def get_project_template():
    return [
        {
            'table_name': 'tasks',
            'columns': [
                ('id', 'Integer', 'primary_key=True'),
                ('title', 'String(128)', 'nullable=False'),
                ('description', 'Text', ''),
                ('status', 'String(32)', 'default="open"'),
            ]
        },
        # Weitere Tabellen nach Bedarf
    ]
