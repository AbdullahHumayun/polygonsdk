from .mapping_dicts import option_condition_dict, OPTIONS_EXCHANGES
from datetime import datetime
class OptionTrade:
    __slots__ = ['exchange', 'sip_timestamp', 'size', 'price', 'conditions']
    def __init__(self, trade_data):
        self.exchange = trade_data.get('exchange')
        self.size = trade_data.get('size')
        self.price = trade_data.get('price')
        self.sip_timestamp = trade_data.get('sip_timestamp')

        # Convert nanosecond timestamp to datetime
        if self.sip_timestamp is not None:
            self.sip_timestamp = datetime.fromtimestamp(self.sip_timestamp / 1e9)

        self.conditions = trade_data.get('conditions')

        self.conditions = [option_condition_dict.get(condition) if condition is not None else [] for condition in self.conditions]

        self.exchange = OPTIONS_EXCHANGES.get(self.exchange).replace("'", '')