import unittest
from ops.operations import operations as o
from datetime import date


class TestOperations(unittest.TestCase):
    def setUp(self):
        o.delete_all()
        o.clear_temp_items()
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

    def test_check_if_storage_exists(self):
        self.assertEqual(o.check_if_storage_already_exists("Testorage"), True)
        self.assertEqual(o.check_if_storage_already_exists("Other"), False)

    def test_check_storage_name_when_str_is_empty(self):
        self.assertEqual(o.check_storage_name(""), True)

    def test_check_storage_name_when_str_ok(self):
        self.assertEqual(o.check_storage_name("TestContainer"), None)

    def test_check_if_item_in_storage(self):
        self.assertEqual(o.check_if_item_already_in_storage("Testitem"), True)
        self.assertEqual(o.check_if_item_already_in_storage("Else"), False)

    def test_get_active_storage(self):
        self.assertEqual(o.get_active_storage(), "Testorage")

    def test_get_active_item(self):
        self.assertEqual(o.get_active_item(), ("Testitem", 0, 2, "-", 1, "-"))

    def test_check_status(self):
        o.update_expiry_date(date.today())
        self.assertEqual(o.check_item_status(
            "Testitem"), ("red", "orange", "red"))

    def test_check_status_omits_non_monitored(self):
        o.update_monitored_status(0)
        self.assertEqual(o.check_item_status("Testitem"), (None, None, None))

    def test_check_updates(self):
        o.update_amount(3)
        o.update_minimum_amount(3)
        o.update_expiry_date(date(2030, 1, 1))
        o.update_misc("Testinfo")
        o.update_monitored_status(0)
        self.assertEqual(o.get_active_item(), ("Testitem",
                         3, 3, "2030-01-01", 0, "Testinfo"))

    def test_add_required_item(self):
        o.add_new_required_item("Teststuff", 2, 1)
        self.assertEqual(len(o.get_all_items()), 2)
        self.assertEqual(o.get_all_items()[1][0], "Teststuff")

    def test_monitored_message(self):
        self.assertEqual(o.monitored_message(1), "Monitored")
        self.assertEqual(o.monitored_message(0), "Not monitored")

    def test_delete_item(self):
        o.delete_item()
        self.assertEqual(len(o.get_all_items()), 0)

    def test_add_temp_item(self):
        o.add_temp_item(("Teststuff", 3, 1))
        self.assertEqual(len(o.get_temp_items()), 1)
        self.assertEqual(o.get_temp_items(), [("Teststuff", 3, 1)])

    def test_clear_temp_items(self):
        o.add_temp_item(("Teststuff", 3, 1))
        o.clear_temp_items()
        self.assertEqual(len(o.get_temp_items()), 0)

    def test_check_item_input_ok(self):
        self.assertEqual(o.check_temp_item_input("Teststuff", "2"), None)

    def test_check_item_input_req_is_str(self):
        self.assertEqual(o.check_temp_item_input("Teststuff", "x"), "Required amount must be an integer")

    def test_check_item_input_req_is_neg(self):
        self.assertEqual(o.check_temp_item_input("Teststuff", "-2"), "Required amount cannot be negative")

    def test_check_item_input_name_is_empty(self):
        self.assertEqual(o.check_temp_item_input("", 1), "Item name must contain at least one character")

    def test_check_item_input_item_already_in_db(self):
        self.assertEqual(o.check_temp_item_input("Testitem", 1), "Testitem already listed for Testorage")

    def test_check_item_input_item_already_in_temp(self):
        o.add_temp_item(("Teststuff", 3, 1))
        self.assertEqual(o.check_temp_item_input("Teststuff", 1), "Teststuff already to be added")

    def test_check_storage_status(self):
        self.assertEqual(o.check_storage_status("Testorage"), [(0, 1), "Expiry date not defined", ["red", "red", None]])
