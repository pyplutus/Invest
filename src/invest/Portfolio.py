from dateutil.parser import parse as to_datetime
from datetime import timedelta
from collections import Counter
import yfinance as yf

class Portfolio ():

    def __init__(self, position, ccy, date, label):
        """position - dict. ex {'EUR' : 100., 'BTC' : 0.01} """

        self.ccy = ccy
        self.position = position
        self.date = get_date(date=date, datetime=True)
        self.portfolio = Counter(position)
        self. label = label

    def price(self, date):
        date = get_date(date)
        price = 0.0
        for key, quantity in self.position.items():
            if key == self.ccy:
                price += quantity
                continue

            fixing = get_fixing(ticker=key, date=date, ccy=self.ccy)
            price += fixing
        return price


    def update(self, adjuster, date):
        """adjuster - dict. ex {'EUR' : 100., 'BTC' : 0.01} """
        for key, quantity in adjuster.items():

            fixing = get_fixing(ticker=key, date=date, ccy=self.ccy)



            assert self.position[self.ccy] - quantity * fx * fixing > 0, 'No enough money'
            self.position[self.ccy] += quantity * fx * fixing
            self.position[key] += quantity





    def __repr__(self):
        return str(self.position)


def get_fixing(ticker, date, ccy):
    tckr = yf.Ticker(ticker)
    if not isinstance(date, str):
        date = date.strftime('%Y-%m-%d')
    fixing = tckr.history(start=date, end=date).Close.values

    if tckr.info['currency'] != ccy:
        fx = get_fx_usd(ccy=ccy, date=date)
    else:
        fx = 1.0

    return fixing * fx

def get_fx_usd(ccy, date):
    fxtckr = yf.Ticker(f'{ccy}=X')
    return fxtckr.history(start=date, end=date).Close.values

def get_date(date, datetime=False):
    dt_date = to_datetime(date) + timedelta(1)
    if datetime:
        return dt_date
    else:
        return dt_date.strftime('%Y-%m-%d')