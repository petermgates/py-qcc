"""
pyqcc.models
~~~~~~~~~~~~
This module contains the base model classes for the qcc package.
"""
import pandas as pd

class Qcc(object):
    """
    Quality Control Charts
    ~~~~~~~~~~~~~~~~~~~~~~
    The main class for control chart objects.\n
    Specify the data and chart type as a minimum
    """
    def __init__(self,
                 data: pd.DataFrame,
                 chart_type: str,
                 newdata: pd.DataFrame=None,
                 nsigmas: int=3,
                 conflevel: float=0.95
                ) -> object:
        self.data = data
        self.type = chart_type
        self.newdata = newdata
        self.nsigmas = nsigmas
        self.conflevel = conflevel
        self.stats = []

        match chart_type:
            case 'xbar':
                self.gen_xbar()

    def gen_xbar(self):
        print('Generate xbar object.')

from data import pistonrings
from utils import qcc_groups
a = qcc_groups(pistonrings[0:30], 'diameter', 'sample')
xbar = Qcc(data=a, chart_type='xbar')