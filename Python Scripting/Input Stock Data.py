import pandas_datareader.data as web
from matplotlib import style
import matplotlib.pyplot as plt
import pandas as pd

import datetime as dt

style.use('ggplot')


Start = dt.datetime(2021, 2, 1)
End = dt.datetime(2021, 3, 1)
stocks = 'TSLA'

def get_data(ticker):
        df = web.DataReader(ticker, 'google', Start, End)
        print(df)


get_data(stocks)
