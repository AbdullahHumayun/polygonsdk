from datetime import datetime
from .mapping_dicts import OPTIONS_EXCHANGES
import pandas as pd
class OptionQuote:
    """Class representing option quotes."""

    __slots__ = ['ask_exchange', 'bid_exchange', 'ask_price', 'bid_price', 'ask_size', 'bid_size', 'sequence_number', 'sip_timestamp']

    def __init__(self, results):
        """
        Initialize an OptionQuote object.

        Args:
            results (list): List of result dictionaries containing option quote data.
        """
        self.ask_exchange = [OPTIONS_EXCHANGES.get(result.get('ask_exchange'), '') for result in results]
        self.bid_exchange = [OPTIONS_EXCHANGES.get(result.get('bid_exchange'), '') for result in results]
        self.ask_price = [result.get('ask_price') for result in results]
        self.bid_price = [result.get('bid_price') for result in results]
        self.ask_size = [result.get('ask_size') for result in results]
        self.bid_size = [result.get('bid_size', None) for result in results]
        self.sequence_number = [result.get('sequence_number') for result in results]
        self.sip_timestamp = [datetime.fromtimestamp(result.get('sip_timestamp') / 1e9).strftime('%Y-%m-%d %H:%M:%S') for result in results]


        self.data_dict = {

            'Ask Exchange': self.ask_exchange,
            'Bid Exchange': self.bid_exchange,
            'Ask Price': self.ask_price,
            'Bid Price': self.bid_price,
            'Ask Size': self.ask_size,
            'Ask Price': self.ask_price,
            'Timestamp': self.sip_timestamp
        }


        self.df = pd.DataFrame(self.data_dict)
    def to_dict(self):
        """
        Convert OptionQuote object to a dictionary.

        Returns:
            dict: Dictionary representation of the OptionQuote object.
        """
        return {slot: getattr(self, slot) for slot in self.__slots__}