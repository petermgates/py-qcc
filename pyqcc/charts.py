import matplotlib.figure
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
    fig_title = "x-bar Chart of Measurements"
    fig_axis_h = "Subgroup"
    fig_axis_v = "Sample mean"
    def __init__(self,
        data: pd.DataFrame,
        title: str = None,
        ) -> object:
        self.data = data
        if title: self.fig_title = title 
        self.summary_dict = self._summary_dict(self.data)
        self.summary = self._summary(self.summary_dict)
        self.fig = self._set_fig()
        self.ax1 = self._set_chart(self.data, self.fig)

    def _summary_dict(self, data: pd.DataFrame) -> dict:
         """Group statistics for the data"""
         self.describe = data.mean(axis=1).describe()
         self.n = data.shape[1]
         self.rbar = (data.max(axis=1) - data.min(axis=1)).mean()
         self.xbarbar = (data.mean(axis=1)).mean()
         self.stdevbar = data.std(axis=1).mean()
         self.lcl = self.xbarbar - (A2[self.n] * self.rbar)
         self.ucl = self.xbarbar + (A2[self.n] * self.rbar)

         summary = {
              "stats": {
                "Min": [self.describe["min"]], "1st Qu.": [self.describe['25%']],
                "Median": [self.describe['50%']], "Mean": [self.describe['mean']],
                "3rd Qu.": [self.describe['75%']], "Max.": [self.describe['max']],
              },
              "limits": {
                "LCL": [self.lcl],
                "UCL": [self.ucl],
              },
              "group": {
                   "Sample size": self.n,
                   "Num. groups": self.describe['count'],
                   "Center": self.describe['mean'],
                   "Mean std. dev.": self.stdevbar,
              }
         }
         return summary

    def _summary(self, summary: dict) -> str:
            """Formatted multiline string with group statistics."""
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

    def _set_fig(self) -> matplotlib.figure.Figure:
         fig = plt.figure(
              figsize=self.fig_figsize,
              facecolor=self.fig_facecolor,
         )
         fig.suptitle = self.fig_title
         fig.tight_layout(h_pad=self.fig_hpad)
         return fig

    def _set_chart(self, data: pd.DataFrame, fig: object) -> object:
        data = data.mean(axis=1)
        ax1 = fig.add_subplot(2,1,1)
        ax1.set(xlabel=self.fig_axis_h, ylabel=self.fig_axis_v)
        ax1.plot(data, linestyle=':', marker='o')

        ax1.axhline(self.xbarbar, color='green')
        ax1.axhline(self.ucl, color='red', linestyle='--')
        ax1.axhline(self.lcl, color='red', linestyle='--')
             
        return ax1

class Imr(Chart):
    '''
    Individuals and moving range (I-MR or X-MR) control chart.
    '''
    from .constants import d2
    def __init__(self) -> None:
        super(Imr, self).__init__()
        
        # self.summary_stats()
    