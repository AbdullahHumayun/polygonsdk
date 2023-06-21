import pandas as pd


class AuctionResult:
    def __init__(self, auctions):
        self.auctionStatus = [auction.get('auctionStatus') for auction in auctions]
        self.operationId = [auction.get('operationId') for auction in auctions]
        self.operationDate = [auction.get('operationDate') for auction in auctions]
        self.operationType = [auction.get('operationType') for auction in auctions]
        self.operationDirection = [auction.get('operationDirection') for auction in auctions]
        self.method = [auction.get('method') for auction in auctions]
        self.releaseTime = [auction.get('releaseTime') for auction in auctions]
        self.closeTime = [auction.get('closeTime') for auction in auctions]
        self.classType = [auction.get('classType') for auction in auctions]
        self.note = [auction.get('note') for auction in auctions]
        self.totalSubmittedOrigFace = [auction.get('totalSubmittedOrigFace') for auction in auctions]
        self.totalAcceptedOrigFace = [auction.get('totalAcceptedOrigFace') for auction in auctions]
        self.totalSubmittedCurrFace = [auction.get('totalSubmittedCurrFace') for auction in auctions]
        self.totalAcceptedCurrFace = [auction.get('totalAcceptedCurrFace') for auction in auctions]
        self.totalAmtSubmittedPar = [auction.get('totalAmtSubmittedPar') for auction in auctions]
        self.totalAmtAcceptedPar = [auction.get('totalAmtAcceptedPar') for auction in auctions]
        self.settlementDate = [auction.get('settlementDate') for auction in auctions]
        self.lastUpdated = [auction.get('lastUpdated') for auction in auctions]

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)
    


class FXSwaps:
    def __init__(self, operations):
        self.operationType = [operation.get("operationType", []) for operation in operations]
        self.counterparty = [operation.get("counterparty", []) for operation in operations]
        self.currency = [operation.get("currency", []) for operation in operations]
        self.tradeDate = [operation.get("tradeDate", []) for operation in operations]
        self.settlementDate = [operation.get("settlementDate", []) for operation in operations]
        self.maturityDate = [operation.get("maturityDate", []) for operation in operations]
        self.termInDays = [operation.get("termInDays", []) for operation in operations]
        self.amount = [operation.get("amount", []) for operation in operations]
        self.interestRate = [operation.get("interestRate", []) for operation in operations]
        self.isSmallValue = [operation.get("isSmallValue", []) for operation in operations]
        self.lastUpdated = [operation.get("lastUpdated", []) for operation in operations]

        self.dict = {
            'operationType': self.operationType,
            'counterparty': self.counterparty,
            'currency': self.currency,
            'tradeDate': self.tradeDate,
            'settlementDate': self.settlementDate,
            'maturityDate': self.maturityDate,
            'termInDays': self.termInDays,
            'amount': self.amount,
            'interestRate': self.interestRate,
            'isSmallValue': self.isSmallValue,
            'lastUpdated': self.lastUpdated
        }
        

        self.df = pd.DataFrame(self.dict)


class TimeSeries:
    def __init__(self, timeseries):

        self.seriesbreak = [i['seriesbreak'] if i['seriesbreak'] is not None else None for i in timeseries]
        self.keyid = [i['keyid'] if i['keyid'] is not None else None for i in timeseries]
        self.description = [i['description'] if i['description'] is not None else None for i in timeseries]

        self.dict = { 
            'Description': self.description,
            'Key ID': self.keyid,
            'Series Break': self.seriesbreak}
        

        self.df = pd.DataFrame(self.dict)



class TimeSeriesData:
    def __init__(self, timeseries):
        self.asofdate = [i['asofdate'] if 'asofdate' in i else None for i in timeseries]
        self.keyid = [i['keyid'] if 'keyid' in i else None for i in timeseries]
        self.value = [i['value'] if 'value' in i  else None for i in timeseries]
            
        self.dict = { 
            'As of Date': self.asofdate,
            'Key ID': self.keyid,
            'Value': self.value}
        

        self.df = pd.DataFrame(self.dict)

class AsOfDates:
    def __init__(self, timeseries):

        self.seriesbreak = [i['seriesbreak'] if i['seriesbreak'] is not None else None for i in timeseries]
        self.asof = [i['asof'] if i['asof'] is not None else None for i in timeseries]

        self.dict = { 
            'Series Break': self.seriesbreak,
            'As of': self.asof,}

        

        self.df = pd.DataFrame(self.dict)


