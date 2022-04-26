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
