from tkinter import Toplevel, ttk, constants
from ops.operations import operations


class CreateStorageView:
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
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._handle_return)

        label.grid(row=0, columnspan=3)
        name_label.grid(row=1, column=0)
        name_entry.grid(row=1, column=1)
        create_button.grid(row=2, column=1, sticky=constants.W)
        cancel_button.grid(row=2, column=1, sticky=constants.E)

    def _error_popup(self):
        popup = Toplevel(master=self._frame)
        popup.title("Input error")
        popup_label = ttk.Label(
            master=popup, text="A storage by the same name already exists")
        popup_label.grid(padx=10, pady=10)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_storage(self, name):
        if operations.check_if_storage_already_exists(name):
            self._error_popup()
        else:
            operations.create_new_storage(name)
            self._handle_return()
