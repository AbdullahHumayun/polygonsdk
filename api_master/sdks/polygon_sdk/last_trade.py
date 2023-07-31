
from sdks.polygon_sdk.list_sets import OPTIONS_EXCHANGES, options_condition_dict
from datetime import datetime
import pandas as pd
class LastTrade:
    def __init__(self, results):

        self.T = results['T']
        self.i = results['i'] if 'i' in results else None
        self.c = [options_condition_dict.get(condition) for condition in results['c']] if 'c' in results else None
        self.t = results['t']
        self.p = results['p'] if 'p' in results else None
        self.q = results['q'] if 'q' in results else None
        self.size = results['s'] if 's' in results else None
        self.xchange = results['x'] if 'x' in results else None

        self.data_dict = { 

            'Ticker': self.T,
            'Conditions': self.c,
            'Timestamp': self.t,
            'Price': self.p,
            'Size': self.size,
            'Exchange': self.xchange

        }
        self.df = pd.DataFrame(self.data_dict)