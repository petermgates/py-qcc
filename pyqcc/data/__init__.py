from dis import Positions
import pandas as pd
import os

_basepath = os.path.abspath(os.path.dirname(__file__))
pistonrings = pd.read_table(os.path.join(_basepath, 'pistonrings.txt')).values