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
                self._ops.view_storages()
            else:
                self._ops.instruction()