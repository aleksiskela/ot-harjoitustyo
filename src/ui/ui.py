from ops.ops import Console


class CLI:
    def __init__(self):
        self._ops = Console()

    def start(self):
        self._ops.start()
        self._ops.instruction()

        while True:
            action = self._ops.user_input()
            if action == "0":
                self._ops.exit()
                break
            elif action == "1":
                self._ops.create_new_storage()
            elif action == "2":
                self._ops.delete_storage()
            elif action == "3":
                self._ops.view_storages()
            elif action == "4":
                self.open_storage()
                self._ops.instruction()
            else:
                self._ops.instruction()

    def open_storage(self):
        exists = self._ops.open_storage()
        if not exists:
            pass
        else:
            self._ops.storage_instruction()
            while True:
                action = self._ops.user_input()
                if action == "0":
                    break
                elif action == "1":
                    self._ops.insert_required_item_to_storage()
                    self._ops.storage_instruction()
                elif action == "2":
                    self._ops.delete_required_item_from_storage()
                    self._ops.storage_instruction()
                elif action == "3":
                    self._ops.load_item()
                    self._ops.storage_instruction()
                elif action == "4":
                    self._ops.use_item()
                    self._ops.storage_instruction()
                else:
                    self._ops.storage_instruction()
