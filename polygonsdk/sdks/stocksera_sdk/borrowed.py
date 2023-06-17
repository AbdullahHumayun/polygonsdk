
class BorrowedShares:
    def __init__(self, borrowed_shares_data):

        self.ticker = [i['ticker'] if i['ticker'] is not None else None for i in borrowed_shares_data]
        self.fee =[i['fee'] if i['fee'] is not None else None for i in borrowed_shares_data]
        self.available =[i['available'] if i['available'] is not None else None for i in borrowed_shares_data]
        self.date_updated =[i['date_updated'] if i['date_updated'] is not None else None for i in borrowed_shares_data]


    def to_dict(self):

        data_dict = { 

            'ticker': self.ticker,
            'fee': self.fee,
            'available': self.available,
            'date_updated': self.date_updated
        }


        return data_dict
