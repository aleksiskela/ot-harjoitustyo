from datetime import date, timedelta


class ItemStatus:
    def __init__(self, amount, min_amount, expdate):
        self._amount = amount
        self._min_amount = min_amount
        self._expdate = expdate
        self.amount_status = None
        self.exp_status = None
        self.total_status = None
        self.remaining_days = None

        self._check_amount()
        self._check_expdate()
        self._determine_total_status()

    def _check_amount(self):
        if self._amount < 3/4*self._min_amount:
            self.amount_status = "red"
        elif self._amount >= self._min_amount:
            self.amount_status = "green"
        else:
            self.amount_status = "orange"

    def _check_expdate(self):
        if self._expdate != "-":
            temp = self._expdate.split("-")
            expdate = date(int(temp[0]), int(temp[1]), int(temp[2]))
            delta = expdate - date.today()

            if delta > timedelta(0):
                self.exp_status = "green"
            elif delta == timedelta(0):
                self.exp_status = "orange"
            elif delta < timedelta(0):
                self.exp_status = "red"

    def _determine_total_status(self):
        self.total_status = "green"
        if self.amount_status == "orange" or self.exp_status == "orange":
            self.total_status = "orange"
        if self.amount_status == "red" or self.exp_status == "red":
            self.total_status = "red"

class StorageStatus:
    def __init__(self, all_items):
        self._all_items = all_items
        self.totals = ()
        self.days_to_exp = None

        self.storage_color = None
        self.totals_color = None
        self.exp_color = None


        self._total_amount()
        self._days_until_expiry()
        self._determine_colors()

        self.colors = [self.storage_color, self.totals_color, self.exp_color]


    def _total_amount(self):
        saturated_amount = 0
        total_items = len(self._all_items)
        for item in self._all_items:
            if item[4] == 0:
                saturated_amount += 1
            else:
                if item[1] >= item[2]:
                    saturated_amount += 1
        self.totals = saturated_amount, total_items

    def _days_until_expiry(self):
        deltae = []
        for item in self._all_items:
            if item[3] != "-":
                temp = item[3].split("-")
                expdate = date(int(temp[0]), int(temp[1]), int(temp[2]))
                delta = expdate - date.today()
                deltae.append(delta.days)
        if len(deltae) == 0:
            self.days_to_exp = "Expiry date not defined"
            self.exp_color = None
        else:
            lowest_delta = min(deltae)
            if lowest_delta >= 0:
                self.days_to_exp = f"Expires in {lowest_delta} days"
                self.exp_color = "green"
                if lowest_delta < 3:
                    self.exp_color = "orange"
            else:
                self.days_to_exp = f"Expired {abs(lowest_delta)} days ago"
                self.exp_color = "red"


    def _determine_colors(self):
        if self.totals[1] == 0:
            self.totals_color == None
        else:
            if self.totals[0]/self.totals[1] < 0.75:
                self.totals_color = "red"
            elif self.totals[0]/self.totals[1] >= 1:
                self.totals_color = "green"
            else:
                self.totals_color = "orange"

        self.storage_color = "green"
        if self.totals_color == "orange" or self.exp_color == "orange":
            self.storage_color = "orange"
        if self.totals_color == "red" or self.exp_color == "red":
            self.storage_color = "red"
