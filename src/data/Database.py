import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def create_table(self, table_name, columns):
        column_definitions = ", ".join(f"{col} {dtype}" for col, dtype in columns.items())
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.execute(sql)