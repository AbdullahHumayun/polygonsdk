import aiohttp
import asyncio
from .models import PriceTarget, CountryRiskPremium
from cfg import YOUR_FMP_KEY
import pandas as pd

class fmpSDK:
    def __init__(self):
        self.api_key = YOUR_FMP_KEY



    async def price_target(self, symbol):
        """Fetches the latest price target for a ticker"""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://financialmodelingprep.com/api/v4/price-target?symbol={symbol}&apikey={YOUR_FMP_KEY}") as resp:
                data = await resp.json()
                if data is not None:
                    return PriceTarget(data)
                
    async def country_risk_premium(self):
        """Returns risk premium by country and continent."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://financialmodelingprep.com/api/v4/market_risk_premium?apikey={YOUR_FMP_KEY}") as resp:
                data = await resp.json()
                if data is not None:
                    return CountryRiskPremium(data)
                else:
                    return None


    async def sector_performance(self):
        """Returns sectors by change % on the day."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://financialmodelingprep.com/api/v3/sector-performance?apikey={YOUR_FMP_KEY}") as resp:
                response = await resp.json()
                sector = [i['sector'] if 'sector' in i else None for i in response]
                changesPercentage = [i['changesPercentage'] if 'changesPercentage' in i else None for i in response]
                data_dictionary = { 

                    'Sector': sector,
                    'Change Percentage': changesPercentage
                }
                df = pd.DataFrame(data_dictionary).sort_values('Change Percentage', ascending=False)
                return df