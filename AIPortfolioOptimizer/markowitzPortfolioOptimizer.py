"""
markowitzPortfolioOptimizer.py

1) Read in .csv price data
2) Calculate Returns and Risk
3) Optimize Portfolio to Max Sharpe Ratio via Monte Carlo Sim

"""


"""
=============================================================================
Import Modules
-----------------------------------------------------------------------------
"""
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import statsmodels.api as sm

from pandas_datareader import data as wb
from scipy import stats

"""
==============================================================================
Functions
------------------------------------------------------------------------------
"""
def normalize_data(data_df):
    """
    Define data normalizing function
    """
    return data_df / data_df.iloc[0] * 100

def log_returns_data(data_df):
    """
    Define daily log returns function
    """
    return np.log(data_df / data_df.shift(1))

def annual_risk_return(data_df):
    """
    # define annualized risk and returns functions
    """
    annual = data_df.agg(["mean", "std"]).T
    annual.columns = ["Return", "Risk"]
    annual.Return = annual.Return * 252
    annual.Risk = annual.Risk * np.sqrt(252)
    return annual

def load_price_data(filename, index_col='Date'):
    print()
    print(50 * '=')
    print('INFO: Loading Price Data.')
    print('  filename = ' + filename)
    # Read in csv data file
    price_data = pd.read_csv(filename, index_col)
    price_data.info()
    print(price_data.head(10))
    print(price_data.loc['Date'])
    print('INFO: Complete.')
    print(50 * '^')


"""
=============================================================================
Load CSV Price Data and Format Data Frame
-----------------------------------------------------------------------------   
"""
filename = 'PriceData SP500 From 01 Dec, 2022 To 07 Mar, 2023.csv'
price_data = load_price_data(filename)

# print('Set index to Date')
# price_data['Date'] = pd.to_datetime(price_data['Date'])
# price_data.set_index('Date', inplace=True)
# price_data_start =  price_data['Date'][2]
# price_data_end = price_data['Date'][len(price_data)-1]
# print(str(price_data_start), str(price_data_end))































