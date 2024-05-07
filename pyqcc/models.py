import pandas as pd
import matplotlib.pyplot as plt

from .charts import Xbar


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
    
    def __repr__(self):
         """Return summary statistics when object is printed."""
         plt.show()
         return self.summary


    def _get_chart(self):
         """Return chart properties depending on chart type."""
         match self.chart_type:
            case 'xbar':
                xbar = Xbar(self.data)
                self.summary = xbar.summary
                self.fig = xbar.fig
                self.ax1 = xbar.ax1
         