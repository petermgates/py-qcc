import pandas as pd
import numpy as np

class qcc(object):
    '''
    Quality Control Charts
    Base class for qcc models.

    TODO: Additional docstring.
    '''

    def __init__(self, data=None, newdata=None) -> None:
        self.data = data
        self.newdata = newdata
        self.stats = []