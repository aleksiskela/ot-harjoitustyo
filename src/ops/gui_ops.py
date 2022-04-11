from repositories.storage_manager import StorageManager


class Operator:
    def __init__(self):
        self._manager = StorageManager()
        self._active_storage = ""

    def get_all_storages(self):
        raw = self._manager.view_storages()
        all_storages = [storage[0] for storage in raw]
        return all_storages

    def create_intro_text(self):
        if len(self.get_all_storages()) == 0:
            return "No storages created yet. Start by creating one."
        return "Available storages:"

    def set_active_storage(self, storage):
        self._active_storage = storage

    def get_active_storage(self):
        return self._active_storage

    def get_all_items(self):
        return self._manager.find_items(self._active_storage)


operator = Operator()
