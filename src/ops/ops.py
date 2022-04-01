from repositories.storage_manager import StorageManager

if False:
    varasto = StorageManager()
    kaappi = "Kaappi"
    laatikko = "Laatikko"
    varasto.create_new_storage(kaappi)
    varasto.create_new_storage(laatikko)
    varastot = varasto.view_storages()
    for item in varastot:
        print(item[0])


class Console:
    def __init__(self):
        self._manager = StorageManager()

    def start(self):
        print("Welcome to the storage manager")

    def instruction(self):
        print("""\n
        1 = Create new storage
        2 = View available storages
        0 = Exit
        """)

    def user_input(self):
        return input("Select action: ")
    
    def create_new_storage(self):
        print("\nCreate new storage")
        name = input("Storage name: ")
        self._manager.create_new_storage(name)
        print(f"{name} created")

    def view_storages(self):
        print("\nAvailable storages:")
        storages = self._manager.view_storages()
        for storage in storages:
            print(storage[0])

    def exit(self):
        print("Thanks for trying!")