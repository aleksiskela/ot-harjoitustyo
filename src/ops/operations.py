from repositories.storage_manager import StorageManager


class Operations:
    def __init__(self):
        self._manager = StorageManager()
        self._active_storage = None
        self._active_item = None
        self._temp_items = []

    def get_all_storages(self):
        raw = self._manager.view_storages()
        all_storages = [storage[0] for storage in raw]
        return all_storages

    def create_intro_text(self):
        if len(self.get_all_storages()) == 0:
            return "No storages created yet. Start by creating one."
        return "Available storages:"

    def create_new_storage(self, storage_name: str):
        self._manager.create_new_storage(storage_name)

    def delete_storage(self):
        self._manager.delete_storage(self._active_storage)

    def set_active_storage(self, storage):
        self._active_storage = storage

    def get_active_storage(self):
        return self._active_storage

    def set_active_item(self, item_name):
        self._active_item = item_name

    def get_active_item(self):
        return self._manager.pick_item(self._active_item, self._active_storage)[0]

    def get_all_items(self):
        return self._manager.find_all_items_in_storage(self._active_storage)

    def add_temp_item(self, item: tuple):
        self._temp_items.append(item)

    def clear_temp_items(self):
        self._temp_items.clear()

    def get_temp_items(self):
        return self._temp_items

    def add_new_required_item(self, item_name, min_amount):
        self._manager.insert_required_item_to_storage(self._active_storage,item_name, min_amount)

    def update_item(self, new_amount):
        self._manager.update_item(self._active_storage, self._active_item, new_amount)

    def delete_item(self):
        self._manager.delete_required_item_from_storage(self._active_storage, self._active_item)


operations = Operations()