from datetime import datetime
from datetime import timedelta

def cast_to_datetime(date: str):
    return datetime.strptime(date, '%Y-%m-%d')

class Strategy():

    def __init__(self, condIn, condOut, buysell):
        self.condIn = condIn
        self.buysell = buysell

    def apply(self, portfolio, df, since):
        since = cast_to_datetime(since)

        if since < df.index[0]:
            ValueError(f'NK: you want to start since {since} but available Yahoo dates starts from {df.index[0]}')
        else:
            df = df[since - timedelta(days=int(3/2 * self.cond.interval)) <= df.index]

        for date, row in df.items:
            if self.condIn(date, df):
                self.inPosition = 1
                portfolio.buy

            if self.condOut(date, df):
                self.inPosition = 0