"""
getTickerSymbolsHTML.py

Script to pull Ticker Symbol Data from specified website.
"""
import pandas as pd


"""
==============================================================================
Functions
------------------------------------------------------------------------------
"""
def dup_delete(x):
    """
    Delete duplicate values from dict input
    :param x: dict
    :return: list
    """
    return list(dict.fromkeys(x))

def get_tickers(index):
    """
    Enter the desired index (SP500, NASDAQ, DOW30) to get equities information
    and symbols
    :param index: Enter 'SP500', 'NASDAQ', or 'DOW30'
    :return: a list of the ticker symbols from the desired index
    """

    if(index.upper() == 'SP500'):
        # Get S&P 500 Tickers
        table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
        table = table.sort_values('Symbol')
        tickers = table.Symbol.to_list()
        tickers = [i.replace('.', '-') for i in tickers]
        return tickers


tickers = get_tickers('SP500')
print(tickers)