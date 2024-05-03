import pandas as pd
import numpy as np

class Qcc(object):
    '''
    Quality Control Charts.

    Base class for qcc models.

    TODO: Additional docstring.
    '''

    def __init__(self, data=None, newdata=None) -> None:
        self.layers = []
        self.data = data
        self.newdata = newdata
        self.stats = []