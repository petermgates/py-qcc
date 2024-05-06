import pandas as pd
import numpy as np
from constants import A2, A3, c4, D3, D4
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
        # self.type = chart_type
        # self.newdata = newdata
        # self.nsigmas = nsigmas
        # self.conflevel = conflevel
        
        self._gen_qcc(chart_type)


    def _gen_qcc(self, chart_type):

        _describe = self.data.mean(axis=1).describe()
        group_size = self.data.shape[1]
        stdevbar = self.data.std(axis=1).mean()

        match chart_type:
            case 'xbar':
                centre, lcl, ucl = self._stats_xbar()
                print(centre, lcl, ucl)
            case 'r':
                centre, lcl, ucl, = self._stats_r()
                print(centre, lcl, ucl)

        summary = {
            "stats":{
                "Min": [_describe["min"]], "1st Qu.": [_describe['25%']],
                "Median": [_describe['50%']], "Mean": [_describe['mean']],
                "3rd Qu.": [_describe['75%']], "Max.": [_describe['max']],
            },
            "limits":{
                "LCL": [lcl],
                "UCL": [ucl],
            }
        }
        # _control_lims = {
        #     "LCL": [lcl],
        #     "UCL": [ucl],
        # }

        _stats_str = tabulate(summary['stats'], headers='keys',
                               tablefmt='plain', floatfmt='.5f')
        _limits_str = tabulate(summary['limits'], headers='keys',
                               tablefmt='plain', floatfmt='.5f')
        
        self.summary_str = "\nxbar chart for data\n\n"\
        "Summary of group statistics:\n"\
        f"{_stats_str}\n\n"\
        f"Group sample size:  {group_size:.0f}\n"\
        f"Number of groups:  {_describe['count']:.0f}\n"\
        f"Center of group statistics:  {_describe['mean']:.5f}\n"\
        f"Standard deviation:  {stdevbar:.9f}\n\n"\
        "Control limits:\n"\
        f"{_limits_str}"


    def _stats_xbar(self):
        n = self.data.shape[1]
        rbar = (self.data.max(axis=1) - self.data.min(axis=1)).mean()
        xbarbar = (self.data.mean(axis=1)).mean()
        lcl = xbarbar - (A2[n] * rbar)
        ucl = xbarbar + (A2[n] * rbar)
        return xbarbar, lcl, ucl

    def _stats_r(self):
        n = self.data.shape[1] # TODO: handle variable sample numbers
        rbar = (self.data.max(axis=1) - self.data.min(axis=1)).mean()
        lcl = rbar * D3[n]
        ucl = rbar * D4[n]
        return rbar, lcl, ucl 


    def _stats_s(self, size, _describe):
        sizes = self.data.count(axis=1)
        stdevbar = self.data.std(axis=1).round(4).mean()
        # stdevbar = self.data.std(axis=1).apply(
        #     lambda si: (si / c4[size]) / _describe['count']).sum()
        print(f'stdevbar: {stdevbar}')
        A3sbar = A3[size] * stdevbar
        lcl = _describe['mean'] - A3sbar
        ucl = _describe['mean'] + A3sbar
        return lcl, ucl

    def _gen_xbar(self):
        print('Generate xbar object.')



# ----------
from data import pistonrings, flowwidth
from utils import qcc_groups

# diameter = qcc_groups(pistonrings[0:25], 'diameter', 'sample')
# print(diameter)
xbar = Qcc(data=flowwidth, chart_type='xbar')
range = Qcc(data=flowwidth, chart_type='r')
# # print(xbar.nsigmas)