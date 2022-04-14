from db_connection import get_db_connection


class StorageManager:
    def __init__(self):
        self._db = get_db_connection()

    def find_storage_id(self, storage_name: str):
        return self._db.execute(
            "SELECT id FROM Storages WHERE name=?",
            [storage_name]).fetchone()[0]

    def if_storage_exists(self, storage_name: str):
        if self._db.execute(
            "SELECT name FROM Storages WHERE name=?",
                [storage_name]).fetchone() is None:
            return False
        return True

    def if_item_in_storage_exists(self, storage_name: str, item_name: str):
        if self._db.execute(
            "SELECT item_name FROM Items WHERE storage_id=? AND item_name=?",
                [self.find_storage_id(storage_name), item_name]).fetchone() is None:
            return False
        return True

    def if_amount_enough(self, storage_name, item_name, amount_to_use):
        storage_id = self.find_storage_id(storage_name)
        if amount_to_use > self._db.execute(
                "SELECT amount FROM Items WHERE storage_id=? AND item_name=?",
                [storage_id, item_name]).fetchone()[0]:
            return False
        return True

    def create_new_storage(self, storage_name: str):
        self._db.execute(
            "INSERT INTO Storages (name) VALUES (?)", [storage_name])

    def view_storages(self):
        return self._db.execute("SELECT name FROM Storages").fetchall()

    def delete_storage(self, storage_name: str):
        storage_id = self.find_storage_id(storage_name)
        self._db.execute("DELETE FROM Items WHERE storage_id=?", [storage_id])
        self._db.execute("DELETE FROM Storages WHERE name=?", [storage_name])

    def find_all_items_in_storage(self, storage_name: str):
        storage_id = self.find_storage_id(storage_name)
        return self._db.execute(
            "SELECT item_name, amount, minimum_amount FROM Items WHERE storage_id=?",
            [storage_id]).fetchall()

    def insert_required_item_to_storage(self, storage_name: str, item_name: str,
                                        minimum_amount: int):
        storage_id = self.find_storage_id(storage_name)
        self._db.execute(
            f"INSERT INTO Items (storage_id, item_name, minimum_amount) VALUES ({storage_id},?,?)",
            [item_name, minimum_amount])

    def pick_item(self, item_name, storage_name):
        storage_id = self.find_storage_id(storage_name)
        return self._db.execute("SELECT item_name, amount, minimum_amount FROM Items WHERE storage_id=? AND item_name=?",[storage_id, item_name]).fetchall()

    def delete_required_item_from_storage(self, storage_name: str, item_name: str):
        storage_id = self.find_storage_id(storage_name)
        self._db.execute("DELETE FROM Items WHERE storage_id=? AND item_name=?",
                         [storage_id, item_name])

    def load_item(self, storage_name, item, amount):
        storage_id = self.find_storage_id(storage_name)
        self._db.execute(
            "UPDATE Items SET amount=amount+? WHERE storage_id=? AND item_name=?",
            [amount, storage_id, item])

    def use_item(self, storage_name, item, amount):
        storage_id = self.find_storage_id(storage_name)
        self._db.execute(
            "UPDATE Items SET amount=amount-? WHERE storage_id=? AND item_name=?",
            [amount, storage_id, item])

    def update_item(self, storage_name, item_name, amount):
        storage_id = self.find_storage_id(storage_name)
        self._db.execute(
            "UPDATE Items SET amount=? WHERE storage_id=? AND item_name=?",
            [amount, storage_id, item_name])

    def delete_all(self):
        self._db.execute("DELETE FROM Items")
        self._db.execute("DELETE FROM Storages")
