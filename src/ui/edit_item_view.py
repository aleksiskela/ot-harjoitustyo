from tkinter import ttk, constants,StringVar
from tkcalendar import Calendar
from datetime import date
from ops.operations import operations


class EditItemView:
    def __init__(self, root, handle_select_storage):
        self._root = root
        self._frame = None
        self._handle_select_storage = handle_select_storage

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        today = date.today()
        
        active_item = operations.get_active_item()
        self._temp_amount = StringVar()
        self._temp_amount.set(active_item[1])

        title_n = ttk.Label(master=self._frame, text="Item name")
        title_a = ttk.Label(master=self._frame, text="Amount")
        title_m = ttk.Label(master=self._frame, text="Required amount")
        title_e = ttk.Label(master=self._frame, text="Expiry date")

        name_label = ttk.Label(master=self._frame, text=active_item[0])
        var_label = ttk.Label(master=self._frame, textvariable=self._temp_amount)
        cap_label = ttk.Label(master=self._frame, text=active_item[2])
        exp_label = ttk.Label(master=self._frame, text=date.today())


        mod_label = ttk.Label(master=self._frame, text="Modify amount")
        inc_button = ttk.Button(master=self._frame, text="Increase", command=self.increase_amount)
        dec_button = ttk.Button(master=self._frame, text="Decrease", command=self.decrease_amount)

        date_label = ttk.Label(master=self._frame, text="Set expiry date")
        self._calendar = Calendar(self._frame, selectmode = "day", year=today.year, month=today.month, day=today.day)
        date_button = ttk.Button(master=self._frame, text="Confirm date", command=lambda: self.change_date(self._calendar.get_date()))

        save_button = ttk.Button(master=self._frame, text="Save", command=self.save_changes)
        cancel_button = ttk.Button(master=self._frame, text="Cancel", command=lambda: self._handle_select_storage(operations.get_active_storage()))
        delete_button = ttk.Button(master=self._frame, text="Delete item from storage", command=self.delete_item)

        title_n.grid(row=0, column=0)
        title_a.grid(row=0, column=1)
        title_m.grid(row=0, column=2)
        title_e.grid(row=0, column=3)

        name_label.grid(row=1, column=0)
        var_label.grid(row=1, column=1)
        cap_label.grid(row=1, column=2)
        exp_label.grid(row=1, column=3)


        mod_label.grid(row=2, column=0)
        inc_button.grid(row=2, column=1)
        dec_button.grid(row=2, column=2)

        date_label.grid(row=3, column=0)
        self._calendar.grid(row=3, column=1)
        date_button.grid(row=3, column=2)

        save_button.grid(row=4, column=0)
        cancel_button.grid(row=4, column=1)
        delete_button.grid(row=4, column=2)

    def increase_amount(self):
        old_amount = int(self._temp_amount.get())
        new_amount = old_amount + 1
        self._temp_amount.set(str(new_amount))

    def decrease_amount(self):
        old_amount = int(self._temp_amount.get())
        new_amount = old_amount - 1
        if new_amount < 0:
            new_amount = 0
        self._temp_amount.set(str(new_amount))

    def save_changes(self):
        operations.update_item(self._temp_amount.get())
        self._handle_select_storage(operations.get_active_storage())

    def change_date(self, datestr):
        datelist = datestr.split(".")
        print(datelist)
        std = date(int(datelist[2]),int(datelist[1]),int(datelist[0])).isoformat()
        print(std)

    def delete_item(self):
        operations.delete_item()
        self._handle_select_storage(operations.get_active_storage())

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()