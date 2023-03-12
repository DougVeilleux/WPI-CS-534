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
import os
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
    Define annualized risk and returns functions
    """
    annual = data_df.agg(["mean", "std"]).T
    annual.columns = ["Return", "Risk"]
    annual.Return = annual.Return * 252
    annual.Risk = annual.Risk * np.sqrt(252)
    return annual

def load_price_data(filename):
    """
    Load csv file of price data and format data frame for analysis
    """
    print()
    print(50 * '=')
    print('INFO: Loading Price Data.')
    print('  filename = ' + filename)
    # Read in csv data file
    df = pd.read_csv(filename, header=[0,1])
    # Format data frame
    # Make Date column the index    
    df.set_index(df.columns[0], inplace=True)
    # Replace NaN with ''
    df.replace(np.nan, '', inplace=True)
    
    # Print head of date frame to confirm format is good
    print(df.head(5))
    print('INFO: Complete.')
    print(50 * '^')
    return df







"""
=============================================================================
Load CSV Price Data and Format Data Frame
-----------------------------------------------------------------------------   
"""
# Specify root path for csv data files
root_path = os.getcwd()
relative_path = 'AIPortfolioOptimizer/'
filename = 'PriceData SP500 From 01 Dec, 2022 To 07 Mar, 2023.csv'
file_path = os.path.join(root_path, relative_path, filename)

# Load csv data file and format data frame
price_data = load_price_data(file_path)

# Print head of price data to confirm indexing is correct
print(price_data['High']['AAPL'])























