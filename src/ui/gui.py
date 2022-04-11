from tkinter import ttk, constants
# from main_view import MainView
from ops.gui_ops import operator


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
        pass


class MainView:
    def __init__(self, root, handle_select_storage, handle_create_storage):
        self._root = root
        self._frame = None
        self._handle_select_storage = handle_select_storage
        self._handle_create_storage = handle_create_storage

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        intro_label = ttk.Label(
            master=self._frame, text="Welcome to the Storage manager!")
        intro_label_2 = ttk.Label(
            master=self._frame, text=operator.create_intro_text())
        intro_label.pack()
        intro_label_2.pack()
        storages = operator.get_all_storages()
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
    def __init__(self, root, storage_name, handle_back):
        self._root = root
        self._frame = None
        self._storage = storage_name
        self.handle_back = handle_back

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=self._storage)
        return_button = ttk.Button(
            master=self._frame, text="Back", command=self.handle_back)
        label.pack()
        return_button.pack()


class CreateNewStorage:
    pass


class EditStorage:
    pass

# class GUI:
#     def __init__(self, root):
#         self._root = root
#         self._frame = None
#         self._ops = Operator()

#     def start(self):
#         self.show_main_view()

#     def destroy_view(self):
#         if self._frame != None:
#             self._frame.destroy()
#         self._frame = None

#     def show_main_view(self):
#         self.destroy_view()
#         self._frame = ttk.Frame(master=self._root)
#         i = 1
#         buttons = {}
#         salute = ttk.Label(master=self._frame, text="Welcome to the Storage Manager")
#         salute_2 = ttk.Label(master=self._frame, text="List of storages:")
#         salute.grid(row=0, column=0, columnspan=2)
#         salute_2.grid(row=1, column=0)
#         storages = self._ops.get_all_storages()
#         for storage in storages:
#             i += 1
#             storage_name = ttk.Label(master=self._frame, text=storage)
#             buttons[storage] = ttk.Button(master=self._frame, text="Open storage", command=lambda: self._handle_storage_selection(storage))
#             storage_name.grid(row=i, column=0, sticky=constants.W)
#             buttons[storage].grid(row=i, column=1)

#     def _handle_storage_selection(self, storage_name):
#         self._ops.set_active_storage(storage_name)
#         print(self._ops._active_storage)
#         self.show_storage_view()

#     def show_storage_view(self):
#         self.destroy_view()
#         self._frame = ttk.Frame(master=self._root)
#         i = 2
#         storage_label = ttk.Label(master=self._frame, text=self._ops.get_active_storage())
#         storage_label.grid(row=0, column=0, columnspan=2)
#         items = self._ops.get_all_items()
#         for item in items:
#             item_name = ttk.Label(master=self._frame, text=f"{item[0]} {item[1]}/{item[2]}")
#             item_name.grid(row=i, column=0, sticky=constants.W)
#             i += 1
