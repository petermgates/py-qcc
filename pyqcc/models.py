import pandas as pd
import numpy as np
from constants import A3
from tabulate import tabulate

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
        _describe = self.data.mean(axis=1).describe()
        numgroups = _describe['count']
        size = self.data.shape[1]
        xbarbar = _describe['mean']
        rbar = (self.data.max(axis=1) - self.data.min(axis=1)).mean()
        stdevbar = self.data.std(axis=1).mean()
        A3sbar = A3[size] * stdevbar
        lcl = xbarbar - A3sbar
        ucl = xbarbar + A3sbar

        _summary = {
            "Min": [_describe["min"]], "1st Qu.": [_describe['25%']],
            "Median": [_describe['50%']], "Mean": [_describe['mean']],
            "3rd Qu.": [_describe['75%']], "Max.": [_describe['max']],
        }
        _control_lims = {
            "LCL": [lcl],
            "UCL": [ucl],
        }
        _summarystr = tabulate(_summary, headers='keys',
                               tablefmt='plain')
        _controlstr = tabulate(_control_lims, headers='keys',
                               tablefmt='plain', floatfmt='.5f')
        
        outputstr = "\nxbar chart for data\n\n"\
        "Summary of group statistics:\n"\
        f"{_summarystr}\n\n"\
        f"Group sample size: {size:.0f}\n"\
        f"Number of groups: {_describe['count']:.0f}\n"\
        f"Center of group statistics: {_describe['mean']:.5f}\n"\
        f"Standard deviation: {stdevbar:.9f}\n\n"\
        "Control limits:\n"\
        f"{_controlstr}"
        

        print(outputstr)
#         outputstr = f'''
# {"min.":>10s}
# {f"{_describe['min']:.2f}":>10s}                    
#                     '''
        # print(_headers, _values)
        # print(self.data.mean(axis=1).describe()['count'])
        # print(f'LCL:{lcl:.5f}, Centre:{xbarbar:.5f}, UCL:{ucl:.5f}.')

    def _gen_xbar(self):
        print('Generate xbar object.')



# ----------
from data import pistonrings, hardbake
from utils import qcc_groups

diameter = qcc_groups(pistonrings, 'diameter', 'sample')
xbar = Qcc(data=diameter[0:25], chart_type='xbar')
# print(xbar.nsigmas)