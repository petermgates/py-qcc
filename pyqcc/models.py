from dataclasses import dataclass
import pandas as pd
import inspect
from constants import A2, A3, c4, D3, D4
from tabulate import tabulate

class Qcc:
    """The main class for control chart objects."""
    def __init__(self,  
                    data: pd.DataFrame,
                    chart_type: str,
                    newdata: pd.DataFrame=None,
                    nsigmas: int=3,
                    conflevel: float=0.95
                    ) -> object:
            self.data = data
            self.chart_type = chart_type

            self._get_chart()
            
            
    def _get_chart(self):
         match self.chart_type:
            case 'xbar':
                self.chart = Xbar(self.data)
         

class Xbar:
    def __init__(self,
        data: pd.DataFrame,
        title: str = "",
        ) -> object:
        self.data = data
        self.summary = self._summary(self.data)
        self.summary_str = self._summary_str(self.summary)

    def _summary(self, data) -> dict:
         """Group statistics for the data"""
         describe = data.mean().describe()
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

    def _summary_str(self, summary) -> str:
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


from data import pistonrings, flowwidth
from utils import qcc_groups

# diameter = qcc_groups(pistonrings[0:25], 'diameter', 'sample')
xbar = Qcc(data=flowwidth, chart_type='xbar')
print(xbar.chart.summary_str)
# range = Qcc(data=flowwidth, chart_type='r')
# xb = Xbar()