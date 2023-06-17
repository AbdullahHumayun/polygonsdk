import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from typing import List
from dataclasses import dataclass
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

webull = AsyncWebullSDK()


@dataclass
class Webull:
    def __init__(self, ticker=None):

        self.ticker: str = None
        self.buyVolume: float = None
        self.sellVolume: float = None
        self.nVolume: float = None
        self.totalVolume: float = None
        self.avgPrice: float = None
        self.financiaScore: str = None
        self.largeNet: float = None
        self.largeIn: float = None
        self.largeOut: float = None
        self.majorNet: float = None
        self.majorIn: float = None
        self.majorOut: float = None
        self.majorInRatio: float = None
        self.majorOutRatio: float = None

        self.smallNet: float = None
        self.smallIn: float = None
        self.smallOut: float = None
        self.smallInRatio: float = None
        self.smallOutRatio: float = None
        self.retailIn: float = None
        self.retailOutRatio: float = None
        self.retailInRatio:  float = None
        self.retailOut: float = None
        self.mediumIn: float = None
        self.mediumOut: float = None
        self.mediumNet: float = None
        self.mediumInRatio: float = None
        self.mediumOutRatio: float = None
        self.superIn: float = None
        self.superOut: float = None
        self.superNet: float = None
        self.newLargeIn: float = None
        self.newLargeOut: float = None
        self.newLargeNet: float = None
        self.newLargeInRatio: float = None
        self.newLargeOutRatio: float = None
        self.shortInt: List[float] = []
        self.daysToCover: List[float] = []
        self.avgVolume: List[float] = []
        self.settlementDate: List[float] = []
        self.capAnalysis: str = None

        self.avgCost: float = None
        self.sharesInProfit70End: float = None
        self.sharesInProfit70Ratio: float = None
        self.sharesInProfit70Start: float = None
        self.sharesInProfit90End: float = None
        self.sharesInProfit90Ratio: float = None
        self.sharesInProfit90Start: float = None
        self.Close: float = None
        self.closeProfitRatio: float = None
        self.distributions: float = None
        self.totalShares: float = None

        self.assetType: List[float] = []
        self.change: List[float] = []
        self.change_ratio: List[float] = []
        self.close: List[float] = []
        self.display_symbol: List[str] = []
        self.down_num: List[float] = []
        self.fifty_two_wk_high: List[float] = []
        self.fifty_two_wk_low: List[float] = []
        self.flat_num: List[float] = []
        self.high: List[float] = []
        self.low: List[float] = []
        self.name: List[str] = []
        self.net_asset: List[float] = []
        self.open: List[float] = []
        self.symbol: List[str] = []
        self.total_asset: List[float] = []
        self.up_num: List[float] = []
        self.vibrate_ratio: List[float] = []
        self.volume: List[float] = []

        self.strongBuy: str = None
        self.buyRating: str = None
        self.sellRating: str = None
        self.hodlRating: str = None
        self.underperformRating: str = None
        self.numAnalysts: str = None
        self.overall_rating: str = None

        self.decreaseChange: float = None
        self.decreasedShares: float = None
        self.increaseChange: float = None
        self.increasedShares: float = None
        self.newChange: float = None
        self.newShares: float = None
        self.soldOutChange: float = None
        self.soldOutShares: float = None
        self.totalHeldShares: float = None
        self.totalHeldSharesChange: float = None
        self.totalOwnershipRatioOfFloat: float = None
        self.totalOwnershipRatioOfFloatChange: float = None
        self.totalNumberOfInstitutions: float = None

    async def fetch_data(self, ticker):
        self.ticker = ticker
        await self.volume_analysis(self.ticker)
        await self.financial_score(self.ticker)
        await self.capital_flow(self.ticker)

        await self.short_interest(self.ticker)
        # await self.cost_distribution(self.ticker)
        await self.commodity_etfs()
        await self.industry_etfs()
        await self.index_etfs()
        await self.other_etfs()
        await self.analyst_ratings(self.ticker)
        await self.institutionals(self.ticker)

    def __repr__(self):
        attributes = [f"{attr}={getattr(self, attr)}" for attr in vars(self) if not attr.startswith("__")]
        return f"Webull({', '.join(attributes)})"
    

    @classmethod
    def from_dict(cls, data):
        webull = cls()
        for key, value in data.items():
            setattr(webull, key, value)
        return webull
    

    async def volume_analysis(self, ticker):
        volume_analysis = await webull.get_webull_vol_analysis_data(ticker)

        self.buyVolume = volume_analysis.buyVolume
        self.sellVolume = volume_analysis.sellVolume
        self.nVolume = volume_analysis.nVolume
        self.avgPrice = volume_analysis.avePrice

        
    

    async def financial_score(self, ticker):
        self.financiaScore = await webull.financial_score(ticker)
        
    
    async def capital_flow(self,ticker):
        capitalFlow = await webull.capital_flow(ticker)

        self.largeNet = capitalFlow.largenet
        self.largeIn = capitalFlow.largein
        self.largeOut = capitalFlow.largeout
  

        self.majorNet = capitalFlow.majornet
        self.majorIn = capitalFlow.majorin
        self.majorOut = capitalFlow.majorout
        self.majorInRatio = capitalFlow.majorinratio
        self.majorOutRatio = capitalFlow.majoroutratio

        self.smallNet = capitalFlow.smallnet
        self.smallIn = capitalFlow.smallin
        self.smallOut = capitalFlow.smallout
        self.smallInRatio = capitalFlow.smallinratio
        self.smallOutRatio = capitalFlow.smalloutratio

        self.retailIn = capitalFlow.retailin
        self.retailOutRatio = capitalFlow.retailoutratio
        self.retailInRatio = capitalFlow.retailinratio
        self.retailOut = capitalFlow.retailout

        self.mediumIn = capitalFlow.mediumin
        self.mediumOut = capitalFlow.mediumout
        self.mediumNet = capitalFlow.mediumnet
        self.mediumInRatio = capitalFlow.mediuminratio
        self.mediumOutRatio = capitalFlow.mediumoutratio

        self.superIn = capitalFlow.superin
        self.superOut = capitalFlow.superout
        self.superNet = capitalFlow.supernet

        self.newLargeIn = capitalFlow.newlargein
        self.newLargeOut = capitalFlow.newlargeout
        self.newLargeNet = capitalFlow.newlargenet
        self.newLargeInRatio = capitalFlow.newlargeinratio
        self.newLargeOutRatio = capitalFlow.newlargeoutratio

        


    async def short_interest(self, ticker):
        shortInterest = await webull.get_short_interest(ticker)
        
        self.shortInt = shortInterest.short_int
        self.daysToCover = shortInterest.days_to_cover
        self.avgVolume = shortInterest.avg_volume
        self.settlementDate = shortInterest.settlement


        
    

    # async def cost_distribution(self, ticker):
    #     costDistribution = await webull.cost_distribution(ticker)
        
    #     self.avgCost = [i.avgCost for i in costDistribution]
    #     self.sharesInProfit70End = [i.chip70End for i in costDistribution]
    #     self.sharesInProfit70Ratio = [i.chip70Ratio for i in costDistribution]
    #     self.sharesInProfit70Start = [i.chip70Start for i in costDistribution]
    #     self.sharesInProfit90End = [i.chip90End for i in costDistribution]
    #     self.sharesInProfit90Ratio=[i.chip90Ratio for i in costDistribution]
    #     self.sharesInProfit90Start=[i.chip90Start for i in costDistribution]
    #     self.Close = [i.close for i in costDistribution]
    #     self.closeProfitRatio = [i.closeProfitRatio for i in costDistribution]
    #     self.distributions = [i.distributions for i in costDistribution]
    #     self.totalShares = [i.totalShares for i in costDistribution]

        
    
    async def commodity_etfs(self):
        etfTypes = await webull.get_etf_categories("commodity")
        self.assetType = [i.asset_type for i in etfTypes]
        self.change = [i.change for i in etfTypes]
        self.change_ratio = [i.change_ratio for i in etfTypes]
        self.close = [i.close for i in etfTypes]
        self.display_symbol = [i.display_symbol for i in etfTypes]
        self.down_num = [i.down_num for i in etfTypes]
        self.fifty_two_wk_high = [i.fifty_two_wk_high for i in etfTypes]
        self.fifty_two_wk_low = [i.fifty_two_wk_low for i in etfTypes]
        self.flat_num = [i.flat_num for i in etfTypes]
        self.high = [i.high for i in etfTypes]
        self.low = [i.low for i in etfTypes]
        self.name = [i.name for i in etfTypes]
        self.net_asset = [i.net_asset for i in etfTypes]
        self.open = [i.open for i in etfTypes]
        self.symbol = [i.symbol for i in etfTypes]
        self.total_asset = [i.total_asset for i in etfTypes]
        self.up_num = [i.up_num for i in etfTypes]
        self.vibrate_ratio = [i.vibrate_ratio for i in etfTypes]
        self.volume = [i.volume for i in etfTypes]

        

    async def industry_etfs(self):
        etfTypes = await webull.get_etf_categories("industry")
        self.assetType = [i.asset_type for i in etfTypes]
        self.change = [i.change for i in etfTypes]
        self.change_ratio = [i.change_ratio for i in etfTypes]
        self.close = [i.close for i in etfTypes]
        self.display_symbol = [i.display_symbol for i in etfTypes]
        self.down_num = [i.down_num for i in etfTypes]
        self.fifty_two_wk_high = [i.fifty_two_wk_high for i in etfTypes]
        self.fifty_two_wk_low = [i.fifty_two_wk_low for i in etfTypes]
        self.flat_num = [i.flat_num for i in etfTypes]
        self.high = [i.high for i in etfTypes]
        self.low = [i.low for i in etfTypes]
        self.name = [i.name for i in etfTypes]
        self.net_asset = [i.net_asset for i in etfTypes]
        self.open = [i.open for i in etfTypes]
        self.symbol = [i.symbol for i in etfTypes]
        self.total_asset = [i.total_asset for i in etfTypes]
        self.up_num = [i.up_num for i in etfTypes]
        self.vibrate_ratio = [i.vibrate_ratio for i in etfTypes]
        self.volume = [i.volume for i in etfTypes]

        

    async def index_etfs(self):
        etfTypes = await webull.get_etf_categories("index")
        self.assetType = [i.asset_type for i in etfTypes]
        self.change = [i.change for i in etfTypes]
        self.change_ratio = [i.change_ratio for i in etfTypes]
        self.close = [i.close for i in etfTypes]
        self.display_symbol = [i.display_symbol for i in etfTypes]
        self.down_num = [i.down_num for i in etfTypes]
        self.fifty_two_wk_high = [i.fifty_two_wk_high for i in etfTypes]
        self.fifty_two_wk_low = [i.fifty_two_wk_low for i in etfTypes]
        self.flat_num = [i.flat_num for i in etfTypes]
        self.high = [i.high for i in etfTypes]
        self.low = [i.low for i in etfTypes]
        self.name = [i.name for i in etfTypes]
        self.net_asset = [i.net_asset for i in etfTypes]
        self.open = [i.open for i in etfTypes]
        self.symbol = [i.symbol for i in etfTypes]
        self.total_asset = [i.total_asset for i in etfTypes]
        self.up_num = [i.up_num for i in etfTypes]
        self.vibrate_ratio = [i.vibrate_ratio for i in etfTypes]
        self.volume = [i.volume for i in etfTypes]

        

    async def other_etfs(self):
        etfTypes = await webull.get_etf_categories("other")
        self.assetType = [i.asset_type for i in etfTypes]
        self.change = [i.change for i in etfTypes]
        self.change_ratio = [i.change_ratio for i in etfTypes]
        self.close = [i.close for i in etfTypes]
        self.display_symbol = [i.display_symbol for i in etfTypes]
        self.down_num = [i.down_num for i in etfTypes]
        self.fifty_two_wk_high = [i.fifty_two_wk_high for i in etfTypes]
        self.fifty_two_wk_low = [i.fifty_two_wk_low for i in etfTypes]
        self.flat_num = [i.flat_num for i in etfTypes]
        self.high = [i.high for i in etfTypes]
        self.low = [i.low for i in etfTypes]
        self.name = [i.name for i in etfTypes]
        self.net_asset = [i.net_asset for i in etfTypes]
        self.open = [i.open for i in etfTypes]
        self.symbol = [i.symbol for i in etfTypes]
        self.total_asset = [i.total_asset for i in etfTypes]
        self.up_num = [i.up_num for i in etfTypes]
        self.vibrate_ratio = [i.vibrate_ratio for i in etfTypes]
        self.volume = [i.volume for i in etfTypes]

        

    async def analyst_ratings(self, ticker):
        analystRatings = await webull.get_analysis_data(ticker)

        self.strongBuy = analystRatings.strongbuy
        self.buyRating = analystRatings.buy
        self.sellRating = analystRatings.sell
        self.hodlRating = analystRatings.hold
        self.underperformRating = analystRatings.underperform
        self.numAnalysts = analystRatings.rating_totals
        self.overall_rating = analystRatings.rating_suggestion

        
    async def institutionals(self, ticker):
        institutionHoldings = await webull.get_institutional_holdings(ticker)

        self.decreaseChange = institutionHoldings.institution_holding.decrease.holding_count_change
        self.decreasedShares = institutionHoldings.institution_holding.decrease.institutional_count

        self.increaseChange = institutionHoldings.institution_holding.increase.holding_count_change
        self.increasedShares = institutionHoldings.institution_holding.increase.institutional_count

        self.newChange = institutionHoldings.institution_holding.new_position.holding_count_change
        self.newShares = institutionHoldings.institution_holding.new_position.institutional_count

        self.soldOutChange = institutionHoldings.institution_holding.sold_out.holding_count_change
        self.soldOutShares = institutionHoldings.institution_holding.sold_out.institutional_count

        stats = institutionHoldings.institution_holding.stat

        self.totalHeldShares = stats.holding_count
        self.totalHeldSharesChange = stats.holding_count_change
        self.totalOwnershipRatioOfFloat = stats.holding_ratio
        self.totalOwnershipRatioOfFloatChange = stats.holding_ratio_change
        self.totalNumberOfInstitutions = stats.institutional_count

        



