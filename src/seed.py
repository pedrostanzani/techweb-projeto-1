import json
from database import Database, Note

with open("./data/notes.json", "r") as file:
    content = file.read()
    data = json.loads(content)

db = Database("database")

for note in data:
    title = note['titulo']
    content = note['detalhes']
    db.add(Note(title=title, content=content))
    print(f"[Database seeding 🌱]: just added a note titled \"{title}\"")

