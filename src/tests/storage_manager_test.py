import unittest
from repositories.storage_manager import StorageManager

class TestStorage_manager(unittest.TestCase):
    def setUp(self):
        self.manager = StorageManager()
    
    def test_create_new_storage(self):
        self.manager.create_new_storage("Testorage")
        output = self.manager.view_storages()

        self.assertEqual(len(output), 1)
        self.assertEqual(output[0][0], "Testorage")