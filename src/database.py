import json
import sqlite3
from dataclasses import dataclass


def create_database(conn):
    query = r"""CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL );"""
    cur = conn.cursor()
    cur.execute(query)


@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

    def to_json(self):
        return json.dumps({ "id": self.id, "title": self.title, "content": self.content }, ensure_ascii=False)


class Database:
    def __init__(self, db_name: str):
        if not db_name.endswith('.db'):
            db_name += '.db'
        self.conn = sqlite3.connect(db_name)
        create_database(self.conn)

    def add(self, note: Note):
        # Parameterized query is a safe way to execute SQL
        args = (note.title, note.content)
        query = f"INSERT INTO note (title, content) VALUES (?, ?);"
        cur = self.conn.cursor()
        cur.execute(query, args)
        self.conn.commit()  # Commit the transaction implicity open by the INSERT INTO command

    def get_all(self):
        query = "SELECT id, title, content FROM note;"
        cur = self.conn.cursor()
        res = cur.execute(query)
        return [ Note(id=id_, title=title, content=content) for id_, title, content in res.fetchall() ]
    
    def get(self, note_id: int):
        args = (note_id,)
        query = "SELECT id, title, content FROM note WHERE id = ?;"
        cur = self.conn.cursor()
        res = cur.execute(query, args)
        struct_res = [ Note(id=id_, title=title, content=content) for id_, title, content in res.fetchall() ]
        if len(struct_res) > 0:
            return struct_res[0]
        return None

    def update(self, entry: Note):
        args = (entry.title, entry.content, entry.id)
        query = "UPDATE note SET title = ?, content = ? WHERE id = ?;"
        cur = self.conn.cursor()
        cur.execute(query, args)
        self.conn.commit()

    def delete(self, note_id: int):
        args = (note_id, )
        query = "DELETE FROM note WHERE id = ?;"
        cur = self.conn.cursor()
        cur.execute(query, args)
        self.conn.commit()
