import pandas as pd

class EarningsCalendar:
    def __init__(self, data):
        self.ticker = data.get('ticker')
        self.earning_release_id = data.get('earningReleaseId')
        self.values = data.get('values')
        if self.values:
            self.ticker_id = self.values.get('tickerId')
            self.region_id = self.values.get('regionId')
            self.qualifier = self.values.get('qualifier')
            self.eps = self.values.get('eps')
            self.eps_estimate = self.values.get('epsEstimate', None)
            self.year = self.values.get('year')
            self.quarter = self.values.get('quarter')
            self.release_date = self.values.get('releaseDate')
            self.is_live = self.values.get('isLive')
            self.last_release_date = self.values.get('lastReleaseDate')
            self.publish_status = self.values.get('publishStatus')


        self.data_dict = { 
            'Ticker': self.ticker,
            'Earnings Release ID': self.earning_release_id,
            'Qualifier': self.qualifier,
            'EPS': self.eps,
            'Year': self.year,
            'Quarter': self.quarter,
            'Release Date': self.release_date,
            'Is Live': self.is_live,
            'Last Release Date': self.last_release_date,
            'Publish Status': self.publish_status

        }

        df = pd.DataFrame(self.data_dict)