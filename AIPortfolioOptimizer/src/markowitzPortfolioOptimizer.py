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
# import statsmodels.api as sm
from pandas_datareader import data as wb
from scipy import stats

# Custom Modules
import sys
root_path = os.getcwd()
# Add project folders to root path
sys.path.append(root_path + '/AIPortfolioOptimizer/data')
sys.path.append(root_path + '/AIPortfolioOptimizer/src')
sys.path.append(root_path + '/AIPortfolioOptimizer/utilities')
from loadTickerPriceData import load_price_data



"""
==============================================================================
Functions
------------------------------------------------------------------------------
"""
def normalize_and_plot_data(df):
    """
    Normalize data frame to 100 allows for easy comparison of time series data
      of various price scales.
      
    Argument: Data Frame (df) of time series data
    Returns: Normalized data frame
    """
    print()
    print(50 * '=')
    print('INFO: Normalizing Price Data.')
    norm = (df / df.iloc[2]) * 1
    #Clean data
    norm.replace(np.nan,0.000)                                               
    norm.replace(np.inf,0.000)     
    norm.replace(-np.inf,0.000)  
    print(norm.head(5))
    print('INFO:  Normalizing Price Data Complete!')
    print(50 * '^')
    
    #Plot norm data
    norm['Adj Close'].plot(figsize = (15,8))
    # #Formatting
    plt.ylabel('Normalized Price (USD)')
    plt.xlabel('Date')
    plt.title('Normalized Adj Close Price Plot')
    plt.grid('on','both')
    # plt.gca().get_legend().remove()
    plt.show()
    
    return norm


def log_returns_data(df):
    """
    Define daily log returns function.
    
    Argument: Data Frame (df) of time series data
    Returns: Logrithmic returns data frame (in this case time series price data)
    """
    print()
    print(50 * '=')
    print('INFO: Calculating Log Returns.')
    log_returns =  np.log(df / df.shift(1))    
    #Clean data
    log_returns.replace(np.nan,0.000)                                
    log_returns.replace(np.inf,0.000) 
    log_returns.replace(-np.inf,0.000) 
    print(log_returns.head(5))
    print('INFO:  Log Returns Complete!')
    print(50 * '^')
    return log_returns

def annual_risk_return(df):
    """
    Define annualized risk and returns functions.
    
    Argument: Data Frame (df) of time series data
    Returns: Object of annualized risk and returns
    """
    annual = df.agg(["mean", "std"]).T
    annual.columns = ["Return", "Risk"]
    annual.Return = annual.Return * 252
    annual.Risk = annual.Risk * np.sqrt(252)
    return annual


















#=============================================================================
#=============================================================================
"""
=============================================================================
Load CSV Price Data 
-----------------------------------------------------------------------------   
"""
# Specify root path for csv data files
root_path = os.getcwd()
relative_path = 'AIPortfolioOptimizer/data'
filename = 'PriceData DOW30 From 01 Dec, 2022 To 12 Mar, 2023.csv'
file_path = os.path.join(root_path, relative_path, filename)

# Load csv data file and format data frame
price_data = load_price_data(file_path)

# Pull Ticker Symbols from MultiIndex and put in list
symbols = price_data.columns.levels[1].unique().tolist()
symbols.remove('Unnamed: 0_level_1')
# print(symbols)


"""
#=============================================================================
# Normalize & Plot
#-----------------------------------------------------------------------------
"""
# Normalize data frame to 100 allows for easy comparison of time series data
# of 
norm = normalize_and_plot_data(price_data)



"""
#=============================================================================
# Calculate Log Returns & Risk of Stocks
#-----------------------------------------------------------------------------
"""
#Calculate Daily Returns with log_returns_data() function
log_returns = log_returns_data(price_data)


#Calculate Annualized Risk and Returns with annual_risk_return() funciton
annual =  annual_risk_return(log_returns)
print(annual.head(5))




# """
# *** Equations Below can be utilized vs the annual_risk_return() function.  
#     More visually explicit from a "following" along perspective vs the one
#     line function.  However, functions used to get better familiar with coding
#     in Python.

# #Annualized Returns
# # log_returns_a = log_returns.mean() * 252                                                         
# #Risk - Standard Deviation of Returns   
# #Annualized STD                         
# # log_returns_std = log_returns.std() * np.sqrt(252)   
                           
# """ 
# #Plot Annual Risk and Returns on a Scatter Plot 
# plt.figure(2, figsize = (20,10))
# #Equities
# annual.plot(kind = "scatter", x = "Risk", y = "Return", s = 50, fontsize = 15)
# for i in annual.index:
#     plt.annotate(i, xy=(annual.loc[i,"Risk"]+0.005, annual.loc[i,"Return"]+0.005))
# #Plot Formating
# plt.xlabel("Ann. Risk(std)", fontsize = 15)
# plt.ylabel("Ann. Return", fontsize = 15)  
# plt.title("Stock Risk vs Return", fontsize = 20)
# plt.grid()
# plt.show()











