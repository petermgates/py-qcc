import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

from .constants import A2

class Chart(object):
    '''
    Control chart base class. 
    '''
    fig_figsize = (12, 7) # 2d tuple
    fig_facecolor = '#e5e5e5' # str
    fig_hpad = 5
    fig_linewidth = 1


class Xbar(Chart):
    
    def __init__(self,
        data: pd.DataFrame,
        title: str = "",
        ) -> object:
        self.data = data
        self.summary_dict = self._summary_dict(self.data)
        self.summary = self._summary(self.summary_dict)
        self.chart = self._chart(self.data, self.summary_dict)

    def _summary_dict(self, data: pd.DataFrame) -> dict:
         """Group statistics for the data"""
         describe = data.mean(axis=1).describe()
         n = data.shape[1]
         rbar = (data.max(axis=1) - data.min(axis=1)).mean()
         xbarbar = (data.mean(axis=1)).mean()
         stdevbar = data.std(axis=1).mean()
         lcl = xbarbar - (A2[n] * rbar)
         ucl = xbarbar + (A2[n] * rbar)

         summary = {
              "stats": {
                "Min": [describe["min"]], "1st Qu.": [describe['25%']],
                "Median": [describe['50%']], "Mean": [describe['mean']],
                "3rd Qu.": [describe['75%']], "Max.": [describe['max']],
              },
              "limits": {
                "LCL": [lcl],
                "UCL": [ucl],
              },
              "group": {
                   "Sample size": n,
                   "Num. groups": describe['count'],
                   "Center": describe['mean'],
                   "Mean std. dev.": stdevbar,
              }
         }
         return summary

    def _summary(self, summary: dict) -> str:
            _stats_tbl = tabulate(summary['stats'], headers='keys',
                                tablefmt='plain', floatfmt='.5f')
            _limits_tbl = tabulate(summary['limits'], headers='keys',
                                tablefmt='plain', floatfmt='.5f')
            
            summary_str = "\nxbar chart for data\n\n"\
            "Summary of group statistics:\n"\
            f"{_stats_tbl}\n\n"\
            f"Group sample size:  {summary['group']['Sample size']:.0f}\n"\
            f"Number of groups:  {summary['group']['Num. groups']:.0f}\n"\
            f"Center of group statistics:  {summary['group']['Center']:.5f}\n"\
            f"Standard deviation:  {summary['group']['Mean std. dev.']:.9f}\n\n"\
            "Control limits:\n"\
            f"{_limits_tbl}"

            return summary_str

    def _chart(self, data: pd.DataFrame, summary: dict) -> object:
         return None
    

class Imr(Chart):
    '''
    Individuals and moving range (I-MR or X-MR) control chart.
    '''
    from .constants import d2
    def __init__(self) -> None:
        super(Imr, self).__init__()
        
        # self.summary_stats()
    