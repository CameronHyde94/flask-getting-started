"""
model.py
--------
Implements the model for our website by simulating a database

Don't use this in a real-word production setting. Use something like 
https://flask-sqlalchemy.palletsprojects.com/.
"""

import json

def load_db():
    with open("flashcards_db.json", encoding="utf8") as f:
        return json.load(f)

def save_db():
    with open("flashcards_db.json", 'w') as f:
        return json.dump(db, f)


db = load_db()