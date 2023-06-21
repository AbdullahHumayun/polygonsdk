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



class SecuredReferenceRates:
    def __init__(self, refrates):

        self.effectiveDate = [i['effectiveDate'] if i['effectiveDate'] is not None else None for i in refrates]
        self.rate_type= [i['type'] if i['type'] is not None else None for i in refrates]
        self.average30day= [i['average30day'] if 'average30day' in i else None for i in refrates]
        self.average90day= [i['average90day'] if 'average90day' in i else None for i in refrates]
        self.average180day= [i['average180day'] if 'average180day' in i else None for i in refrates]
        self.index= [i['index'] if 'index' in i else None for i in refrates]
        self.revisionIndicator= [i['revisionIndicator'] if i['revisionIndicator'] is not None else None for i in refrates]


        self.data_dict = { 

            'Effective Date': self.effectiveDate,
            'Rate Type': self.rate_type,
            'Average 30 Day': self.average30day,
            'Average 90 Day': self.average90day,
            'Average 180 Day': self.average180day,
            'Index': self.index,
            'Revision Indicator': self.revisionIndicator
        }


        self.df = pd.DataFrame(self.data_dict)


class UnsecuredReferenceRates:
    def __init__(self, refrates):
        self.effectiveDate = [i['effectiveDate'] if i['effectiveDate'] is not None else None for i in refrates]
        self.rate_type= [i['type'] if i['type'] is not None else None for i in refrates]
        self.percent = [i["percent"] if 'percent' in i else None for i in refrates]
        self.percentPercentile1 = [i["percentPercentile1"] if "percentPercentile1" else None for i in refrates]
        self.percentPercentile25 = [i["percentPercentile25"] if "percentPercentile25" in i  else None for i in refrates]
        self.percentPercentile75 = [i["percentPercentile75"] if "percentPercentile75" in i  else None for i in refrates]
        self.percentPercentile99 = [i["percentPercentile99"] if "percentPercentile99" in i  else None for i in refrates]
        self.revisionIndicator= [i['revisionIndicator'] if 'revisionIndicator' in i else None for i in refrates]
        self.TargetRateFrom = [i["targetRateFrom"] if "targetRateFrom" in i  else None for i in refrates]
        self.TargetRateTo = [i["targetRateTo"] if "targetRateTo" in i else None for i in refrates]
        self.VolumeInBillions = [i["volumeInBillions"] if i["volumeInBillions"]  else None for i in refrates]
        self.FootNoteID = [i["footnoteId"] if "footnoteId" in i else None for i in refrates]


  # Create the dictionary containing all attributes
        self.dict = {
            "effectiveDate": self.effectiveDate,
            "rate_type": self.rate_type,
            "percent": self.percent,
            "percentPercentile1": self.percentPercentile1,
            "percentPercentile25": self.percentPercentile25,
            "percentPercentile75": self.percentPercentile75,
            "percentPercentile99": self.percentPercentile99,
            "revisionIndicator": self.revisionIndicator,
            "TargetRateFrom": self.TargetRateFrom,
            "TargetRateTo": self.TargetRateTo,
            "VolumeInBillions": self.VolumeInBillions,
            "FootNoteID": self.FootNoteID
        }


        self.df = pd.DataFrame(self.dict)