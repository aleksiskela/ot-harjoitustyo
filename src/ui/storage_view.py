from tkinter import ttk, constants
from ops.operations import operations

class StorageView:
    def __init__(self, root, storage_name, handle_return, handle_edit_storage, handle_edit_item):
        self._root = root
        self._frame = None
        operations.set_active_storage(storage_name)
        self.handle_return = handle_return
        self.handle_edit_storage = handle_edit_storage
        self.handle_edit_item = handle_edit_item

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=f"{operations.get_active_storage()} opened")
        label.grid(row=0, columnspan=2)
        items = operations.get_all_items()
        for item in items:
            self._list_items(item)
        self._footer()

    def _list_items(self, item):
        item_frame = ttk.Frame(master=self._frame)
        item_name = item[0]
        item_amount = f"{item[1]}/{item[2]}"
        item_name_label = ttk.Label(master=item_frame, text=item_name)
        item_amount_label = ttk.Label(master=item_frame, text=item_amount)
        edit_button = ttk.Button(master=item_frame, text="Edit item", command=lambda: self.handle_edit_item(item_name))
        # item_name_label.pack(side=constants.LEFT)
        # item_amount_label.pack(side=constants.RIGHT)
        item_name_label.grid(row=0, column=0, sticky=constants.W)
        item_amount_label.grid(row=0, column=2)
        edit_button.grid(row=0, column=3, sticky=constants.E)

        item_frame.grid()
        # item_frame.pack(fill=constants.X)

    def _footer(self):
        foot_frame = ttk.Frame(master=self._frame)
        edit_button = ttk.Button(master=foot_frame, text="Edit storage", command=self.handle_edit_storage)
        return_button = ttk.Button(
            master=foot_frame, text="Back", command=self.handle_return)
        # edit_button.pack(side=constants.LEFT)
        # return_button.pack(side=constants.RIGHT)
        edit_button.grid(row=0, column=1)
        return_button.grid(row=0, column=2)

        foot_frame.grid()