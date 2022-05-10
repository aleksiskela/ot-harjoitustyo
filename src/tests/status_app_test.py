import unittest
from ops.status_app import ItemStatus, StorageStatus
from datetime import date, timedelta


class TestItemStatus(unittest.TestCase):
    def setUp(self):
        today = str(date.today())
        yesterday = str(date.today() - timedelta(1))
        tomorrow = str(date.today() + timedelta(1))
        future = str(date.today() + timedelta(10))

        self.item1 = ItemStatus(4, 4, today)
        self.item2 = ItemStatus(0, 1, yesterday)
        self.item3 = ItemStatus(3, 4, tomorrow)
        self.item4 = ItemStatus(0, 0, future)
        self.item5 = ItemStatus(6, 5, "-")

    def test_check_amount_full(self):
        self.assertEqual(self.item1.amount_status, "green")

    def test_check_amount_intermediate(self):
        self.assertEqual(self.item3.amount_status, "orange")

    def test_check_amount_low(self):
        self.assertEqual(self.item2.amount_status, "red")

    def test_check_exp_date_not_set(self):
        self.assertEqual(self.item5.exp_status, None)

    def test_check_exp_date_today(self):
        self.assertEqual(self.item1.exp_status, "orange")

    def test_check_exp_date_future(self):
        self.assertEqual(self.item4.exp_status, "green")

    def test_determine_total_status_orange(self):
        self.assertEqual(self.item1.total_status, "orange")

    def test_determine_total_status_green(self):
        self.assertEqual(self.item5.total_status, "green")

    def test_determine_total_status_red(self):
        self.assertEqual(self.item2.total_status, "red")


class TestStorageStatus(unittest.TestCase):
    def setUp(self):
        today = str(date.today())
        yesterday = str(date.today() - timedelta(1))
        tomorrow = str(date.today() + timedelta(1))
        future = str(date.today() + timedelta(10))

        self.item1 = ["Testitem", 1, 1, future, 1, "-"]
        self.item2 = ["Teststuff", 0, 1, today, 0, "-"]
        self.item3 = ["Testhing", 1, 4, yesterday, 1, "-"]
        self.item4 = ["Testpack", 3, 4, tomorrow, 1, "-"]
        self.item5 = ["Testobject", 2, 2, "-", 1, "-"]

        self.items = [self.item1, self.item2,
                      self.item3, self.item4, self.item5]

    def test_saturated_amount_incs_when_item_not_monitored(self):
        self.assertEqual(StorageStatus([self.item2]).totals, (1, 1))

    def test_saturated_amount_not_incs_when_item_monitored_and_unfull(self):
        self.assertEqual(StorageStatus([self.item3]).totals, (0, 1))

    def test_saturated_amount_incs_when_item_monitored_and_full(self):
        self.assertEqual(StorageStatus([self.item1]).totals, (1, 1))

    def test_days_until_expiry_finds_lowest_value(self):
        self.assertEqual(StorageStatus(
            self.items).days_to_exp, "Expired 1 days ago")

    def test_days_until_expiry_returns_correct_colors(self):
        self.assertEqual(StorageStatus([self.item1]).exp_color, "green")
        self.assertEqual(StorageStatus([self.item4]).exp_color, "orange")
        self.assertEqual(StorageStatus([self.item3]).exp_color, "red")
        self.assertEqual(StorageStatus([self.item5]).exp_color, None)

    def test_determine_totals_color_when_required_items_zero(self):
        self.assertEqual(StorageStatus([]).totals_color, None)

    def test_determine_totals_color(self):
        self.assertEqual(StorageStatus(self.items).totals_color, "red")
        self.assertEqual(StorageStatus(
            [self.item1, self.item1, self.item1, self.item3]).totals_color, "orange")
        self.assertEqual(StorageStatus([self.item1]).totals_color, "green")
