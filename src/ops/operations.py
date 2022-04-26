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

    def add_new_required_item(self, item_name, min_amount, monitored):
        self._manager.insert_required_item_to_storage(self._active_storage,item_name, min_amount, monitored)

    def update_amount(self, new_amount):
        self._manager.update_amount(self._active_storage, self._active_item, new_amount)

    def update_expiry_date(self, expiry_date):
        self._manager.set_expiry_date(self._active_storage, self._active_item, expiry_date)

    def update_monitored_status(self, status):
        self._manager.set_monitored_status(self._active_storage, self._active_item, status)

    def update_misc(self, misc):
        self._manager.set_misc(self._active_storage, self._active_item, misc)

    def monitored_message(self, value):
        if value == 1:
            return "Monitored"
        return "Not monitored"

    def delete_item(self):
        self._manager.delete_required_item_from_storage(self._active_storage, self._active_item)


operations = Operations()