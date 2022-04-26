from tkinter import ttk, constants
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

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_storage(self, name):
        operations.create_new_storage(name)
        self._handle_return()
