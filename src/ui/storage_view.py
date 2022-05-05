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
        label = ttk.Label(master=self._frame,
                          text=f"{operations.get_active_storage()} opened")
        label.grid(row=0, columnspan=6, padx=5, pady=15)
        self.items = operations.get_all_items()
        self._first_row()
        for item in self.items:
            self._list_items(item)
        self._footer()

    def _first_row(self):
        if len(self.items) == 0:
            label = ttk.Label(master=self._frame, text=
            "Storage is empty.")
            label_2 = ttk.Label(master=self._frame, text="Select 'Edit storage' to add required items.")
            label.grid()
            label_2.grid(pady=5)
        else:
            name_label = ttk.Label(master=self._frame, text="Item")
            amount_label = ttk.Label(master=self._frame, text="Amount")
            exp_label = ttk.Label(master=self._frame, text="Expiry date")
            mon_label = ttk.Label(master=self._frame, text="Status")
            misc_label = ttk.Label(master=self._frame, text="Additional info")

            name_label.grid(row=1, column=0, sticky=constants.W)
            amount_label.grid(row=1, column=1)
            exp_label.grid(row=1, column=2)
            mon_label.grid(row=1, column=3)
            misc_label.grid(row=1, column=4)

            self._frame.grid_columnconfigure(0, minsize=150)
            self._frame.grid_columnconfigure(1, minsize=50)
            self._frame.grid_columnconfigure(2, minsize=100)
            self._frame.grid_columnconfigure(3, minsize=150)
            self._frame.grid_columnconfigure(4, minsize=200)
            self._frame.grid_columnconfigure(5, minsize=100)



    def _list_items(self, item):
        item_frame = ttk.Frame(master=self._frame)

        colors = operations.check_item_status(item[0])

        item_name = item[0]
        item_amount = f"{item[1]} / {item[2]}"
        item_exp = item[3]
        misc = item[5]

        item_name_label = ttk.Label(
            master=item_frame, text=item_name, foreground=colors[2])
        item_amount_label = ttk.Label(
            master=item_frame, text=item_amount, foreground=colors[0])
        item_exp_label = ttk.Label(
            master=item_frame, text=item_exp, foreground=colors[1])
        monitored_message_label = ttk.Label(
            master=item_frame, text=operations.monitored_message(item[4]))
        misc_label = ttk.Label(master=item_frame, text=misc)

        edit_button = ttk.Button(
            master=item_frame, text="Edit item", command=lambda: self.handle_edit_item(item_name))

        item_name_label.grid(row=0, column=0, sticky=constants.W)
        item_amount_label.grid(row=0, column=1)
        item_exp_label.grid(row=0, column=2)
        monitored_message_label.grid(row=0, column=3)
        misc_label.grid(row=0, column=4)
        edit_button.grid(row=0, column=5, sticky=constants.E)

        item_frame.grid_columnconfigure(0, minsize=150)
        item_frame.grid_columnconfigure(1, minsize=50)
        item_frame.grid_columnconfigure(2, minsize=100)
        item_frame.grid_columnconfigure(3, minsize=150)
        item_frame.grid_columnconfigure(4, minsize=200)
        item_frame.grid_columnconfigure(5, minsize=100)

        item_frame.grid(columnspan=6)

    def _footer(self):
        foot_frame = ttk.Frame(master=self._frame)
        edit_button = ttk.Button(
            master=foot_frame, text="Edit storage", command=self.handle_edit_storage)
        return_button = ttk.Button(
            master=foot_frame, text="Back", command=self.handle_return)
        edit_button.grid(row=0, column=1)
        return_button.grid(row=0, column=2)

        foot_frame.grid_rowconfigure(0, pad=10)
        foot_frame.grid(columnspan=6)
