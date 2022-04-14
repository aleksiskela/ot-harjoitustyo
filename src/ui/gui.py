from ui.main_view import MainView
from ui.storage_view import StorageView
from ui.create_storage_view import CreateStorageView
from ui.edit_storage_view import EditStorageView
from ui.edit_item_view import EditItemView
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
        operations.clear_temp_items()
        operations.set_active_item(None)
        self._show_storage_view(storage_name)

    def _handle_return(self):
        operations.set_active_storage(None)
        self._show_main_view()

    def _handle_create_storage(self):
        self._show_create_storage_view()

    def _handle_edit_storage(self):
        self._show_edit_storage()

    def _handle_edit_item(self, item_name):
        operations.set_active_item(item_name)
        self._show_edit_item()

    def _show_main_view(self):
        self.destroy()
        self._active_view = MainView(
            self._root, self._handle_select_storage, self._handle_create_storage)
        self._active_view.pack()

    def _show_storage_view(self, storage_name):
        self.destroy()
        self._active_view = StorageView(
            self._root, storage_name, self._handle_return, self._handle_edit_storage, self._handle_edit_item)
        self._active_view.pack()

    def _show_create_storage_view(self):
        self.destroy()
        self._active_view = CreateStorageView(
            self._root, self._handle_return)
        self._active_view.pack()

    def _show_edit_storage(self):
        self.destroy()
        self._active_view = EditStorageView(self._root, self._handle_select_storage, self._handle_edit_storage, self._handle_return)
        self._active_view.pack()

    def _show_edit_item(self):
        self.destroy()
        self._active_view = EditItemView(self._root, self._handle_select_storage)
        self._active_view.pack()

# class MainView:
#     def __init__(self, root, handle_select_storage, handle_create_storage):
#         self._root = root
#         self._frame = None
#         self._handle_select_storage = handle_select_storage
#         self._handle_create_storage = handle_create_storage

#         self._initialize()

#     def pack(self):
#         self._frame.pack(fill=constants.X)

#     def destroy(self):
#         self._frame.destroy()

#     def _initialize(self):
#         self._frame = ttk.Frame(master=self._root)
#         intro_label = ttk.Label(
#             master=self._frame, text="Welcome to the Storage manager!")
#         intro_label_2 = ttk.Label(
#             master=self._frame, text=operations.create_intro_text())
#         intro_label.pack()
#         intro_label_2.pack()
#         storages = operations.get_all_storages()
#         for storage in storages:
#             self._list_storages(storage)
#         self._footer()

#     def _list_storages(self, storage):
#         storage_frame = ttk.Frame(master=self._frame)
#         label = ttk.Label(master=storage_frame, text=storage)
#         button = ttk.Button(master=storage_frame, text="Open storage",
#                             command=lambda: self._handle_select_storage(storage))
#         label.pack(side=constants.LEFT)
#         button.pack(side=constants.RIGHT)

#         storage_frame.pack(fill=constants.X)

#     def _footer(self):
#         button = ttk.Button(
#             master=self._frame, text="Create new storage", command=self._handle_create_storage)
#         button.pack()


# class StorageView:
#     def __init__(self, root, storage_name, handle_return, handle_edit_storage, handle_edit_item):
#         self._root = root
#         self._frame = None
#         operations.set_active_storage(storage_name)
#         self.handle_return = handle_return
#         self.handle_edit_storage = handle_edit_storage
#         self.handle_edit_item = handle_edit_item

#         self._initialize()

#     def pack(self):
#         self._frame.pack(fill=constants.X)

#     def destroy(self):
#         self._frame.destroy()

#     def _initialize(self):
#         self._frame = ttk.Frame(master=self._root)
#         label = ttk.Label(master=self._frame, text=f"{operations.get_active_storage()} opened")
#         label.grid(row=0, columnspan=2)
#         items = operations.get_all_items()
#         for item in items:
#             self._list_items(item)
#         self._footer()

#     def _list_items(self, item):
#         item_frame = ttk.Frame(master=self._frame)
#         item_name = item[0]
#         item_amount = f"{item[1]}/{item[2]}"
#         item_name_label = ttk.Label(master=item_frame, text=item_name)
#         item_amount_label = ttk.Label(master=item_frame, text=item_amount)
#         edit_button = ttk.Button(master=item_frame, text="Edit item", command=lambda: self.handle_edit_item(item_name))
#         # item_name_label.pack(side=constants.LEFT)
#         # item_amount_label.pack(side=constants.RIGHT)
#         item_name_label.grid(row=0, column=0, sticky=constants.W)
#         item_amount_label.grid(row=0, column=2)
#         edit_button.grid(row=0, column=3, sticky=constants.E)

#         item_frame.grid()
#         # item_frame.pack(fill=constants.X)

#     def _footer(self):
#         foot_frame = ttk.Frame(master=self._frame)
#         edit_button = ttk.Button(master=foot_frame, text="Edit storage", command=self.handle_edit_storage)
#         return_button = ttk.Button(
#             master=foot_frame, text="Back", command=self.handle_return)
#         # edit_button.pack(side=constants.LEFT)
#         # return_button.pack(side=constants.RIGHT)
#         edit_button.grid(row=0, column=1)
#         return_button.grid(row=0, column=2)

#         foot_frame.grid()


# class CreateStorageView:
#     def __init__(self, root, handle_return):
#         self._root = root
#         self._frame = None
#         self._handle_return = handle_return

#         self._initialize()

#     def _initialize(self):
#         self._frame = ttk.Frame(master=self._root)

#         label = ttk.Label(master=self._frame, text="Create new storage")
#         name_label = ttk.Label(master=self._frame, text="Storage name")
#         name_entry = ttk.Entry(master=self._frame)
#         create_button = ttk.Button(master=self._frame, text="Create",
#                                    command=lambda: self._create_storage(name_entry.get()))
#         cancel_button = ttk.Button(master=self._frame, text="Cancel", command=self._handle_return)

#         label.grid(row=0, columnspan=3)
#         name_label.grid(row=1, column=0)
#         name_entry.grid(row=1, column=1)
#         create_button.grid(row=2, column=1, sticky=constants.W)
#         cancel_button.grid(row=2, column=1, sticky=constants.E)

#     def pack(self):
#         self._frame.pack(fill=constants.X)

#     def destroy(self):
#         self._frame.destroy()

#     def _create_storage(self, name):
#         operations.create_new_storage(name)
#         self._handle_return()


# class EditStorageView:
#     def __init__(self, root, handle_select_storage, handle_edit_storage, handle_return):
#         self._root = root
#         self._frame = None
#         self._handle_select_storage = handle_select_storage
#         self._handle_edit_storage = handle_edit_storage
#         self._handle_return = handle_return

#         self._initialize()

#     def _initialize(self):
#         self._frame = ttk.Frame(master=self._root)

#         label_text = f"Add required item for {operations.get_active_storage()}"
#         storage_label = ttk.Label(master=self._frame, text=label_text)
#         name_label = ttk.Label(master=self._frame, text="Item name")
#         min_amount_label = ttk.Label(master=self._frame, text="Minimum amount")

#         storage_label.grid(row=0, column=1)
#         name_label.grid(row=1, column=0)
#         min_amount_label.grid(row=1, column=1)

#         self._entry()
#         if len(operations._temp_items) > 0:
#             temp_label = ttk.Label(master=self._frame, text="Items to be added:")
#             temp_label.grid(row=3, column=0, sticky=constants.E)
#             for item in operations.get_temp_items():
#                 self.list_temp_items(item)

#         self._footer()

#     def _entry(self):
#         entry_frame = ttk.Frame(master=self._frame)
#         item_name_entry = ttk.Entry(master=entry_frame)
#         min_amount_entry = ttk.Entry(master=entry_frame)
#         add_item_button = ttk.Button(master=entry_frame,
#                                     text="Add required item",
#                                     command=lambda: self._add_temp_item((item_name_entry.get(),
#                                                                     min_amount_entry.get())))

#         item_name_entry.grid(row=0, column=0)
#         min_amount_entry.grid(row=0, column=1)
#         add_item_button.grid(row=0, column=2)

#         entry_frame.grid(column=0, columnspan=3)

#     def _footer(self):
#         footer_frame = ttk.Frame(master=self._frame)

#         save_button = ttk.Button(master=footer_frame, text="Save", command=self.save_changes)
#         cancel_button = ttk.Button(master=footer_frame, text="Cancel",
#                                 command=lambda: self._handle_select_storage(operations.get_active_storage()))
#         delete_button = ttk.Button(master=footer_frame, text="Delete storage", command=self._delete_storage)
       
#         save_button.grid(row=0, column=1, sticky=constants.W)
#         cancel_button.grid(row=0, column=2, sticky=constants.E)
#         delete_button.grid(row=0, column=3)

#         footer_frame.grid(column=1, sticky=constants.W)

#     def _add_temp_item(self, item):
#         operations.add_temp_item(item)
#         self.destroy()
#         self._handle_edit_storage()

#     def list_temp_items(self, item):
#         temp_frame = ttk.Frame(master=self._frame)
#         temp_label = ttk.Label(master=temp_frame, text=f"{item[0]}, {item[1]} required")
#         temp_label.grid(column=0, sticky=constants.E)
#         temp_frame.grid(column=0, sticky=constants.E)

#     def save_changes(self):
#         for item in operations.get_temp_items():
#             operations.add_new_required_item(item[0], item[1])
#         self._handle_select_storage(operations.get_active_storage())

#     def _delete_storage(self):
#         operations.delete_storage()
#         self._handle_return()

#     def pack(self):
#         self._frame.pack(fill=constants.X)

#     def destroy(self):
#         self._frame.destroy()



# class EditItemView:
#     def __init__(self, root, handle_select_storage):
#         self._root = root
#         self._frame = None
#         self._handle_select_storage = handle_select_storage

#         self._initialize()

#     def _initialize(self):
#         self._frame = ttk.Frame(master=self._root)
        
#         active_item = operations.get_active_item()
#         self._temp_amount = StringVar()
#         self._temp_amount.set(active_item[1])

#         title_n = ttk.Label(master=self._frame, text="Item name")
#         title_a = ttk.Label(master=self._frame, text="Amount")
#         title_m = ttk.Label(master=self._frame, text="Required amount")

#         name_label = ttk.Label(master=self._frame, text=active_item[0])
#         var_label = ttk.Label(master=self._frame, textvariable=self._temp_amount)
#         cap_label = ttk.Label(master=self._frame, text=active_item[2])


#         mod_label = ttk.Label(master=self._frame, text="Modify amount")
#         inc_button = ttk.Button(master=self._frame, text="Increase", command=self.increase_amount)
#         dec_button = ttk.Button(master=self._frame, text="Decrease", command=self.decrease_amount)

#         date_label = ttk.Label(master=self._frame, text="Update expiry date")
#         date_entry = ttk.Entry(master=self._frame)
#         date_button = ttk.Button(master=self._frame, text="Update")

#         save_button = ttk.Button(master=self._frame, text="Save", command=self.save_changes)
#         cancel_button = ttk.Button(master=self._frame, text="Cancel", command=lambda: self._handle_select_storage(operations.get_active_storage()))
#         delete_button = ttk.Button(master=self._frame, text="Delete item from storage", command=self.delete_item)

#         title_n.grid(row=0, column=0)
#         title_a.grid(row=0, column=1)
#         title_m.grid(row=0, column=2)
#         name_label.grid(row=1, column=0)
#         var_label.grid(row=1, column=1)
#         cap_label.grid(row=1, column=2)
#         mod_label.grid(row=2, column=0)
#         inc_button.grid(row=2, column=1)
#         dec_button.grid(row=2, column=2)

#         date_label.grid(row=3, column=0)
#         date_entry.grid(row=3, column=1)
#         date_button.grid(row=3, column=2)

#         save_button.grid(row=4, column=0)
#         cancel_button.grid(row=4, column=1)
#         delete_button.grid(row=4, column=2)

#     def increase_amount(self):
#         old_amount = int(self._temp_amount.get())
#         new_amount = old_amount + 1
#         self._temp_amount.set(str(new_amount))

#     def decrease_amount(self):
#         old_amount = int(self._temp_amount.get())
#         new_amount = old_amount - 1
#         if new_amount < 0:
#             new_amount = 0
#         self._temp_amount.set(str(new_amount))

#     def save_changes(self):
#         operations.update_item(self._temp_amount.get())
#         self._handle_select_storage(operations.get_active_storage())

#     def delete_item(self):
#         operations.delete_item()
#         self._handle_select_storage(operations.get_active_storage())

#     def pack(self):
#         self._frame.pack(fill=constants.X)

#     def destroy(self):
#         self._frame.destroy()