from .charts import Charts
from ..constants import d2

class Imr(Charts):
    '''
    Individuals and moving range (I-MR or X-MR) control chart.
    '''
    def __init__(self) -> None:
        super(Imr, self).__init__()
    
    