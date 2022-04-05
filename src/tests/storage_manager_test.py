import unittest
from repositories.storage_manager import StorageManager

class TestStorage_manager(unittest.TestCase):
    def setUp(self):
        self.manager = StorageManager()
        self.manager.delete_all()
        self.s = "Testorage"
        self.i = "Testitem"
        self.manager.create_new_storage(self.s)
        self.manager.insert_required_item_to_storage(self.s, self.i, 1)
    
    def test_create_new_storage(self):
        output = self.manager.view_storages()

        self.assertEqual(len(output), 1)
        self.assertEqual(output[0][0], "Testorage")
    
    def test_delete_storage(self):
        self.manager.delete_storage(self.s)
        output = self.manager.view_storages()

        self.assertEqual(len(output), 0)

    # def test_delete_storage_deletes_items_in_storage(self):
    #     self.manager.delete_storage(self.s)
    #     output = self.manager.find_items(self.s)

    #     self.assertEqual(output, None)

    def test_find_storage_id_returns_correct_id(self):
        self.assertEqual(self.manager.find_storage_id(self.s), 1)

    def test_if_storage_exists_return_true_if_storage_does_exist(self):
        self.assertEqual(self.manager.if_storage_exists("Testorage"), True)

    def test_if_storage_exists_return_false_if_storage_does_not_exist(self):
        self.assertEqual(self.manager.if_storage_exists("NotTestorage"), False)
