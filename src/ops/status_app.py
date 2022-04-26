from datetime import date


class ItemStatus:
    def __init__(self, amount, min_amount, expdate):
        self._amount = amount
        self._min_amount = min_amount
        self._expdate = expdate
        self.status = None

        self._check_amount()

    def _check_amount(self):
        if self._amount < self._min_amount:
            self.status = "red"
        else:
            self.status = "green"

    def _check_expdate(self):
        pass
