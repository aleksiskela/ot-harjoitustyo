from repositories.storage_manager import StorageManager

class Console:
    def __init__(self):
        self._manager = StorageManager()
        self.active_storage = ""

    def start(self):
        print("Welcome to the storage manager")

    def instruction(self):
        print("""\n
        1 = Create new storage
        2 = Delete storage
        3 = View all storages
        4 = Open a storage
        0 = Exit
        """)

    def user_input(self):
        return input("Select action: ")
    
    def create_new_storage(self):
        print("\nCreate new storage")
        name = input("Storage name: ")
        self._manager.create_new_storage(name)
        print(f"{name} created\n")

    def delete_storage(self):
        print("\nRemove storage")
        name = input("Storage name do you wish to delete: ")
        if not self._manager.if_storage_exists(name):
            print("No storage by that name exists")
        else:
            self._manager.delete_storage(name)
            print(f"{name} and its content deleted\n")

    def view_storages(self):
        print("\nAvailable storages:")
        storages = self._manager.view_storages()
        if len(storages) == 0:
            print("No storages created")
        for storage in storages:
            print(storage[0])
        print()

    def insert_required_item_to_storage(self):
        print("\nInsert required item")
        item = input("Item: ")
        min_req = int(input("Minimum number of items: "))
        self._manager.insert_required_item_to_storage(self.active_storage, item, min_req)
        print(item, "inserted")

    def delete_required_item_from_storage(self):
        print("\nDelete a required item from a storage")
        item = input("Item name you wish to delete: ")
        if not self._manager.if_item_in_storage_exists(self.active_storage, item):
            print("No such item in", self.active_storage)
        else:
            self._manager.delete_required_item_from_storage(self.active_storage, item)
            print(f"{item} deleted from {self.active_storage}")

    def open_storage(self):
        storage_name = input("Enter storage name: ")
        if not self._manager.if_storage_exists(storage_name):
            print("Storage by that name does not exist")
            return False
        else:
            self.active_storage = storage_name
            return True

    def storage_instruction(self):
        print(f"\n{self.active_storage} content:")
        all = self._manager.find_items(self.active_storage)
        for item in all:
            print(f"{item[0]} {item[1]}/{item[2]}")
        print("""
        0 = Return to main manu
        1 = Insert required item
        2 = Delete required item
        """)
        
    def exit(self):
        print("Thanks for testing!")