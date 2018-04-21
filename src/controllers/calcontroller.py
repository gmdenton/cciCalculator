from src.model.ccdata import ccdata
from src.model.monthlydata import monthlydata
import datetime
import calendar

class calcontroller(object):

    def __init__(self, ccdat):
        self._total_interest = 0.0
        if isinstance(ccdat, ccdata):
            self._ccdata = ccdat
        else:
            raise TypeError("Parameter ccdat must be of type ccdata")

    @property
    def total_interest(self):
        return self._total_interest

    # sets the amount for new charges that should be used in the interest calculation
    # this is done based on card type as some charge cards don't bill interest to new charges until the next period
    def _set_new_charges(self):
        if self._ccdata.cctype in ("AX", 'DN'):
            nctotal = 0.00
        elif self._ccdata.cctype in ('MC', 'VA'):
            nctotal = self._ccdata.newcharges * self._ccdata.period
        return nctotal

    # Method to calculate the interest that will be charged for a single period.
    def calculate_interest(self):
        obtotal = (self._ccdata.openingbalance - self._ccdata.payment) * self._ccdata.period
        nctotal = self._set_new_charges()
        avgdb = (obtotal + nctotal)/self._ccdata.period
        return (avgdb * self._ccdata.dailyrate) * self._ccdata.period

    # Method to return balance figures for a single period
    def calculate_balances(self, month):
        bal = (self._ccdata.openingbalance + self._ccdata.newcharges)
        interest = self.calculate_interest()
        if self._ccdata.payment > bal + interest:
            self._ccdata.set_payment(bal + interest)
        bal = round(bal - self._ccdata.payment,2)
        mdata = monthlydata(calendar.month_abbr[month], round(bal, 2), round(interest, 2))
        return mdata

    def calculate_multiple_periods(self, months):
        currentmonth = datetime.datetime.now().month
        i = 0
        results = []
        while i < months:
            if currentmonth > 12:
                currentmonth = 1
            lastresult = self.calculate_balances(currentmonth)
            if lastresult.balance == 0:
                break
            results.append(lastresult)
            # update the input based on the last calculation
            self._ccdata.set_openingbalance(round(lastresult.balance, 2))
            self._total_interest = self._total_interest + lastresult.interest
            # Update counter and month Number
            i = i+1
            currentmonth = currentmonth+1
        return results



