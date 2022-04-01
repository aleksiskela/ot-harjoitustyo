from db_connection import get_db_connection
from datetime import date

class StorageManager:
    def __init__(self):
        self._db = get_db_connection()

    def create_new_storage(self, storage_name: str):
        self._db.execute("INSERT INTO Storages (name) VALUES (?)", [storage_name])

    def view_storages(self):
        return self._db.execute("SELECT name FROM Storages").fetchall()