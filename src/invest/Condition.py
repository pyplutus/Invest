
class Condition():

    def __call__(self, date, df):
        pass

class Maximum(Condition):
    "Check whethever we reached the local maximum on self.interval period"

    def __init__(self, interval=30):
        """
        :param interval: period in past we compute max
        """
        assert isinstance(interval, int), 'interval should be of int type - number of days'
        self.interval = interval

    def __call__(self, date, df):
        "Check whether condition is true or false at date 'date' for market data 'df' "
        pos = df.index.get_loc(date)
        dfmin = df.iloc[pos-self.interval : pos+1]
        if dfmin[date] == dfmin.max():
            return True
        else:
            return False

class Double(Condition):
    "Check if the price is doubled"

    def __init__(self, reference_price):
        self.ref = reference_price

    def __call__(self, date, df):
        pass


class Correction(Condition):

    def __call__(self, df):
        pass
