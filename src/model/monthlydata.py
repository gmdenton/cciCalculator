

class monthlydata(object):

    def __init__(self, month, principal, interest):
        self._month = month
        self._principal = principal
        self._interest = interest
        self._balance = self.principal + self._interest

    @property
    def month(self):
        return self._month

    @property
    def principal(self):
        return self._principal

    @property
    def interest(self):
        return self._interest

    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        return  str(self.__dict__)





