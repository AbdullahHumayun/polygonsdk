import pandas as pd

class Quote:
    def __init__(self, results):

        self.ask_exchange = [i['ask_exchange'] if 'ask_exchange' in i else None for i in results]
        self.ask_price = [i['ask_price'] if 'ask_price' in i else None for i in results]
        self.ask_size = [i['ask_size'] if 'ask_size' in i else None for i in results]
        self.bid_exchange = [i['bid_exchange'] if 'bid_exchange' in i else None for i in results]
        self.bid_price = [i['bid_price'] if 'bid_price' in i else None for i in results]
        self.bid_size = [i['bid_size'] if 'bid_size' in i else None for i in results]
        self.participant_timestamp = [i['participant_timestamp'] if 'participant_timestamp' in i else None for i in results]
        self.sequence_number = [i['sequence_number'] if 'sequence_number' in i else None for i in results]
        self.sip_timestamp = [i['sip_timestamp'] if 'sip_timestamp' in i else None for i in results]


        self.data_dict = { 

            'ask_exchange': self.ask_exchange,
            'ask_price': self.ask_price,
            'ask_size': self.ask_size,
            'bid_exchange': self.bid_exchange,
            'bid_price': self.bid_price,
            'bid_size': self.bid_size,
            'participant_timestamp': self.participant_timestamp,
            'sequence_number': self.sequence_number,
            'sip_timestamp': self.sip_timestamp
        }


        self.df = pd.DataFrame(self.data_dict)