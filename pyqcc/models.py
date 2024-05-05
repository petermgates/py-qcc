import pandas as pd
import numpy as np
from constants import A3

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
        # self.stats = []

        self._gen_stats()

        # match chart_type:
        #     case 'xbar':
        #         self._gen_xbar()

    def _gen_stats(self):
        numgroups = self.data.shape[0]
        size = self.data.shape[1]
        xbarbar = self.data.mean(axis=1).mean()
        rbar = (self.data.max(axis=1) - self.data.min(axis=1)).mean()
        stdevbar = self.data.std(axis=1).mean()
        A3sbar = A3[size] * stdevbar
        ucl = xbarbar + A3sbar
        lcl = xbarbar - A3sbar
        print(f'UCL:{ucl:.3f}, Centre:{xbarbar:.3f}, LCL:{lcl:.3f}.')

    def _gen_xbar(self):
        print('Generate xbar object.')



# ----------
from data import pistonrings, hardbake
from utils import qcc_groups

diameter = qcc_groups(pistonrings, 'diameter', 'sample')

xbar = Qcc(data=diameter, chart_type='xbar')
# print(xbar.nsigmas)