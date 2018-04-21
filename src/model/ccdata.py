from enum import Enum


class cctypes(Enum):
    AmericanExpress = "AX"
    Diners = "DN"
    MasterCard = "MC"
    Visa = "VA"


class ccdata(object):

    def __init__(self, openingbalance, newcharges, rate, payment, period, cctype):
        self._openingbalance = openingbalance
        self._rate = rate
        self._payment = payment
        self._period = period
        self._newcharges = newcharges
        self._cctype = self._validateCCType(cctype)

    def _validateCCType(self, cct):
        if cct in (cctypes.AmericanExpress.value, cctypes.Diners.value, cctypes.MasterCard.value, cctypes.Visa.value) :
            return cct
        else:
            raise ValueError("Unknown or invalid card type supplied")

    @property
    def openingbalance(self):
        return self._openingbalance

    def set_openingbalance(self, value):
        self._openingbalance = value

    @property
    def newcharges(self):
        return self._newcharges

    @property
    def rate(self):
        return self._rate

    @property
    def payment(self):
        return self._payment


    def set_payment(self, value):
        self._payment = value

    @property
    def period(self):
        return  self._period

    @property
    def cctype(self):
        return  self._cctype

    @property
    def dailyrate(self):
        if self._rate <= 0:
            raise ValueError("Interest rate must be greater 0")
        else:
            return (self._rate/365)/100

