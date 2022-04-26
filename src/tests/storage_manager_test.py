import unittest
from repositories.storage_manager import StorageManager


class TestStorage_manager(unittest.TestCase):
    def setUp(self):
        self.manager = StorageManager()
        self.manager.delete_all()
        self.s = "Testorage"
        self.i = "Testitem"
        self.manager.create_new_storage(self.s)
        self.manager.insert_required_item_to_storage(self.s, self.i, 1, 1)

    def test_create_new_storage(self):
        output = self.manager.view_storages()

        self.assertEqual(len(output), 1)
        self.assertEqual(output[0][0], "Testorage")

    def test_delete_storage(self):
        self.manager.delete_storage(self.s)
        output = self.manager.view_storages()

        self.assertEqual(len(output), 0)

    def test_if_item_exists_return_true(self):
        output = self.manager.if_item_in_storage_exists(
            "Testorage", "Testitem")
        self.assertEqual(output, True)

    def test_if_item_exists_returns_false(self):
        self.assertEqual(self.manager.if_item_in_storage_exists(
            "Testorage", "NotTestitem"), False)

    def test_find_storage_id_returns_correct_id(self):
        self.assertEqual(self.manager.find_storage_id(self.s), 1)

    def test_if_storage_exists_return_true_if_storage_does_exist(self):
        self.assertEqual(self.manager.if_storage_exists("Testorage"), True)

    def test_if_storage_exists_return_false_if_storage_does_not_exist(self):
        self.assertEqual(self.manager.if_storage_exists("NotTestorage"), False)

    def test_find_items_returns_correct_values(self):
        output = self.manager.find_all_items_in_storage("Testorage")
        self.assertEqual(output, [("Testitem", 0, 1, "-", 1, "-")])

    def test_delete_required_item(self):
        self.manager.delete_required_item_from_storage("Testorage", "Testitem")
        self.assertEqual(
            self.manager.find_all_items_in_storage("Testorage"), [])
