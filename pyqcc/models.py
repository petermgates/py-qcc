"""
pyqcc.models
~~~~~~~~~~~~

This module contains the base model classes for the qcc package.
"""

class Qcc(object):
    def __init__(self, data=None, newdata=None) -> None:
        self.layers = []
        self.data = data
        self.newdata = newdata
        self.stats = []