import sqlite3

from config import DB_PATH

class DatabaseManager:

    def __init__(self):

        self.conn = sqlite3.connect(DB_PATH)

    def initialize(self):

        cur = self.conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS documents(
            id INTEGER PRIMARY KEY,
            path TEXT UNIQUE,
            title TEXT,
            content TEXT
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS embeddings(
            doc_id INTEGER PRIMARY KEY,
            vector BLOB
        )
        """)

        self.conn.commit()

    def insert_document(
        self,
        path,
        title,
        content
    ):

        cur = self.conn.cursor()

        cur.execute("""
        INSERT OR REPLACE INTO documents
        (path,title,content)
        VALUES(?,?,?)
        """,
        (path,title,content))

        self.conn.commit()