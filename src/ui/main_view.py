from tkinter import ttk, constants
from ops.operations import operations

class MainView:
    def __init__(self, root, handle_select_storage, handle_create_storage):
        self._root = root
        self._frame = None
        self._handle_select_storage = handle_select_storage
        self._handle_create_storage = handle_create_storage

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        intro_label = ttk.Label(
            master=self._frame, text="Welcome to the Storage manager!")
        intro_label_2 = ttk.Label(
            master=self._frame, text=operations.create_intro_text())
        intro_label.pack()
        intro_label_2.pack()
        storages = operations.get_all_storages()
        for storage in storages:
            self._list_storages(storage)
        self._footer()

    def _list_storages(self, storage):
        storage_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=storage_frame, text=storage)
        button = ttk.Button(master=storage_frame, text="Open storage",
                            command=lambda: self._handle_select_storage(storage))
        label.pack(side=constants.LEFT)
        button.pack(side=constants.RIGHT)

        storage_frame.pack(fill=constants.X)

    def _footer(self):
        button = ttk.Button(
            master=self._frame, text="Create new storage", command=self._handle_create_storage)
        button.pack()