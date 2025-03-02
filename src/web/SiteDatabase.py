import sqlite3

from ..data.Database import Database

class SiteDatabase(Database):
    def __init__(self, db_file):
        super().__init__(db_file)
        self.create_table("visited", {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "domain": "TEXT UNIQUE NOT NULL"
        })

        self.create_table("to_visit", {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "domain": "TEXT UNIQUE NOT NULL"
        })
    
    def add(self, domain, table):
        try:
            sql = f"INSERT INTO {table} (domain) VALUES ('{domain}')"
            self.execute(sql)
            return True
        except sqlite3.IntegrityError:
            return False
        
    def is_in(self, domain, table):
        print(f"SELECT 1 FROM {table} WHERE domain = '{domain}' LIMIT 1")
        self.cursor.execute(f"SELECT 1 FROM {table} WHERE domain = '{domain}' LIMIT 1")
        return self.cursor.fetchone() is not None