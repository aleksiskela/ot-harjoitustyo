import unittest
from ops.operations import operations as o


class TestOperations(unittest.TestCase):
    def setUp(self):
        o.delete_all()
        o.create_new_storage("Testorage")
        o.set_active_storage("Testorage")
        o.add_new_required_item("Testitem", 2, 1)
        o.set_active_item("Testitem")

    def test_create_new_storage(self):
        sample = o.get_all_storages()

        self.assertEqual(len(sample), 1)
        self.assertEqual(sample[0], "Testorage")

    def test_delete_active_storage(self):
        o.delete_storage()
        self.assertEqual(len(o.get_all_storages()), 0)

    def test_create_intro_text_when_storages_exist(self):
        self.assertEqual(o.create_intro_text(), "Available storages:")

    def test_create_intro_text_when_no_storages_exist(self):
        o.delete_storage()
        self.assertEqual(o.create_intro_text(),
                         "No storages created yet. Start by creating one.")

    def test_get_active_storage(self):
        self.assertEqual(o.get_active_storage(), "Testorage")

    def test_get_active_item(self):
        self.assertEqual(o.get_active_item(), ("Testitem", 0, 2, "-", 1, "-"))

    def test_check_status(self):
        self.assertEqual(o.check_item_status("Testitem"), "red")

    def test_add_required_item(self):
        pass
