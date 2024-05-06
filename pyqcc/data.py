'''
Example data sets, taken from the R qcc repo.
Returns pandas dataframes.

Data sourced from the R qcc package sample data and
Introduction to Statistical Process Control by Douglas C. Montgomery,
7th Ed. Wiley, 2012.
'''

import pandas as pd
import os

_basepath = os.path.abspath(os.path.dirname(__file__))
_datapath = 'data/'

# Taken from the R qcc package data 
pistonrings = pd.read_csv(os.path.join(_basepath, _datapath, 'pistonrings.csv'))

# Taken from Montgomery table 6.1 (pre-grouped).
flowwidth = pd.read_csv(os.path.join(_basepath, _datapath, 'flowwidth.csv'), header=None)

# Taken from Montgomery table 6.3.
pistonrings2 = pd.read_csv(os.path.join(_basepath, _datapath, 'pistonrings2.csv'))