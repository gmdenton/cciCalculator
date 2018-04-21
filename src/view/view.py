from src.controllers.guicontroller import guiController


class view(object):

    @property
    def apr(self):
        return self._apr

    @apr.setter
    def apr(self, value):
        self.apr = value

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self.period = value

    @property
    def openingBalance(self):
        return self._openingBalance

    @openingBalance.setter
    def openingBalance(self, value):
        self.openingBalance = value

    @property
    def newCharges(self):
        return self._newcharges

    @newCharges.setter
    def newCharges(self, value):
        self.newCharges = value

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, value):
        self.payment = value

    @property
    def ccType(self):
        return self._cctype

    @ccType.setter
    def ccType(self, value):
        self.ccType = value

    @property
    def noMonths(self):
        return self._noMonths

    @noMonths.setter
    def noMonths(self, value):
        self.noMonths = value


    def get_total_interest(self):
        return self._controller.get_total_interest()


    # Calls calculate function in guiController and returns an array of result data objects
    def do_calculate(self):
        self._controller = guiController()
        return self._controller.calculate_multiple(self.noMonths.get(), self.apr.get(), self.openingBalance.get(), self.newCharges.get(), self.payment.get(),
                                       self.period.get(), self.ccType.get())


    def do_clear(self):
        self.apr.set(0)
        self.openingBalance.set(0.0)
        self.newCharges.set(0.0)
        self.ccType.set("")
        self.payment.set(0.0)
        self.period.set(0)


