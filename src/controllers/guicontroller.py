from src.model.ccdata import ccdata
from src.controllers.calcontroller import calcontroller
import json


class guiController:

    def __init__(self):
        self._resuts = []
        self._total_interest = 0.0

    def call_calculate(self, apr, openingbalance, newcharges, payment, period, cctype):
        self._data = ccdata(openingbalance, newcharges, apr, payment, period, cctype)
        cccontroller = calcontroller(self._data)
        self._resuts.append(cccontroller.calculateBalances(1))

    def _obj_dict(self, obj):
        return obj.__dict__

    def calculate_multiple(self, months, apr, openingbalance, newcharges, payment, period, cctype):
        self._data = ccdata(openingbalance, newcharges, apr, payment, period, cctype)
        cccontroller = calcontroller(self._data)
        self.results = cccontroller.calculate_multiple_periods(months)
        # return total interest before controller is destroyed after calculate call completes.
        self._total_interest = cccontroller.total_interest
        return json.dumps(self.results, default=self._obj_dict)

    def get_total_interest(self):
        return self._total_interest



