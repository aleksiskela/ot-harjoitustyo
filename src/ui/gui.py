from tkinter import ttk, constants
# from main_view import MainView
from ops.operations import operations


class GUI:
    def __init__(self, root):
        self._root = root
        self._active_view = None

    def start(self):
        self._show_main_view()

    def destroy(self):
        if self._active_view:
            self._active_view.destroy()
        self._active_view = None

    def _handle_select_storage(self, storage_name):
        self._show_storage_view(storage_name)

    def _handle_return(self):
        self._show_main_view()

    def _handle_create_storage(self):
        self._show_create_storage_view()

    def _show_main_view(self):
        self.destroy()
        self._active_view = MainView(
            self._root, self._handle_select_storage, self._handle_create_storage)
        self._active_view.pack()

    def _show_storage_view(self, storage_name):
        self.destroy()
        self._active_view = StorageView(
            self._root, storage_name, self._handle_return)
        self._active_view.pack()

    def _show_create_storage_view(self):
        self.destroy()
        self._active_view = CreateNewStorage(
            self._root, self._handle_return)
        self._active_view.pack()


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
        self._bottomline()

    def _list_storages(self, storage):
        storage_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=storage_frame, text=storage)
        button = ttk.Button(master=storage_frame, text="Open storage",
                            command=lambda: self._handle_select_storage(storage))
        label.pack(side=constants.LEFT)
        button.pack(side=constants.RIGHT)

        storage_frame.pack(fill=constants.X)

    def _bottomline(self):
        button = ttk.Button(
            master=self._frame, text="Create new storage", command=self._handle_create_storage)
        button.pack()


class StorageView:
    def __init__(self, root, storage_name, handle_return):
        self._root = root
        self._frame = None
        self._storage = storage_name
        self.handle_return = handle_return

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=self._storage)
        return_button = ttk.Button(
            master=self._frame, text="Back", command=self.handle_return)
        label.pack()
        return_button.pack()


class CreateNewStorage:
    def __init__(self, root, handle_return):
        self._root = root
        self._frame = None
        self._handle_return = handle_return

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Create new storage")
        name_label = ttk.Label(master=self._frame, text="Storage name")
        name_entry = ttk.Entry(master=self._frame)
        create_button = ttk.Button(master=self._frame, text="Create",
                                   command=lambda: self._create_storage(name_entry.get()))

        label.grid(row=0, columnspan=3)
        name_label.grid(row=1, column=0)
        name_entry.grid(row=1, column=1)
        create_button.grid(row=1, column=2)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_storage(self, name):
        operations.create_new_storage(name)
        self._handle_return()


class EditStorage:
    pass
