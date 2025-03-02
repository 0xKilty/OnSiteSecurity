import sqlite3

from ..data.Database import Database

class SiteDatabase(Database):
    def __init__(self, db_file):
        super().__init__(db_file)
        self.create_table("sites", {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "domain": "TEXT UNIQUE NOT NULL"
        })
    
    def add_site(self, domain):
        try:
            sql = f"INSERT INTO sites (domain) VALUES ('{domain}')"
            self.execute(sql)
            return True
        except sqlite3.IntegrityError:
            return False
        
    def has_visited(self, domain):
        self.cursor.execute("SELECT 1 FROM sites WHERE domain = ? LIMIT 1", (domain,))
        return self.cursor.fetchone() is not None