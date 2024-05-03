'''
Example data sets, taken from the R qcc repo.
Returns pandas dataframes.
'''

import pandas as pd
import os

_basepath = os.path.abspath(os.path.dirname(__file__))
_datapath = 'data/'

pistonrings = pd.read_csv(os.path.join(_basepath, _datapath, 'pistonrings.csv'))