import disnake
import requests
from utils.webull_tickers import ticker_list
from cfg import YOUR_NASDAQ_KEY


class Quote(disnake.ui.Select):
    def __init__(self, ticker:str):
        self.ticker = ticker_list[ticker.upper()]
        
        analyst = requests.get(url=f"https://quoteapi.webullfintech.com/api/securities/stock/{ticker}/recommendation")
        analystd = analyst.json() or None
        rating = requests.get(url=f"https://securitiesapi.webullfintech.com/api/securities/ticker/v5/analysis/{ticker}")
        ratingd = rating.json()
        try:
            ratingtotal = ratingd['rating']#ratings
            ratingtotals = ratingtotal['ratingAnalysisTotals']#ratings
            ratinganalysis = ratingtotal['ratingAnalysis']#ratings
        except KeyError:
            ratingtotal = "N/A"
            ratingtotals = "N/A"
            ratinganalysis = "N/A"

        quote= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ticker={ticker}&includeSecu=1&delay=0&more=1")
        quoted = quote.json() or None
        estimateEarningsDate=quoted[0]["estimateEarningsDate"]#quote
        earningscrush = requests.get(url=f"https://data.nasdaq.com/api/v3/datasets/QOR/{self.values[0]}/data.json?api_key={YOUR_NASDAQ_KEY}")
        earningscrushd = earningscrush.json() or None
        analyst = requests.get(url=f"https://quoteapi.webullfintech.com/api/securities/stock/{ticker}/recommendation")
        analystd = analyst.json() or None
        rating = requests.get(url="https://securitiesapi.webullfintech.com/api/securities/ticker/v5/analysis/913255341")#performance
        ratingd = rating.json()#performance
        ratingtotal = ratingd['rating']#performance
        ratingtotals = ratingtotal['ratingAnalysisTotals']#performance
        ratinganalysis = ratingtotal['ratingAnalysis']#performance
        latestEarningsDate=quoted[0]["latestEarningsDate"]#quote
        fiftyTwoWkHigh=quoted[0]["fiftyTwoWkHigh"]#quote
        fiftyTwoWkLow=quoted[0]["fiftyTwoWkLow"]#quote
        avgvol10= quoted[0]["avgVol10D"]#quote
        high=quoted[0]["high"]#quote
        low=quoted[0]["low"]#quote
        open=quoted[0]["open"]#quote
        close=quoted[0]["close"]#quote
        float10 = float(avgvol10)#quote
        avg10 = round(float10*0.000001, ndigits=2)#quote
        avg3m=quoted[0]["avgVol3M"]#quote
        float3m = float(avg3m)#quote
        avg3mo = round(float3m*0.000001, ndigits=2)#quote

        super().__init__(
            placeholder=f"🏹 🇩  🇦  🇹  🇦 for {self.values[0]} 🏹",
            min_values=1,
            max_values=1,
            custom_id=f"priceselect",
            options= [
        disnake.SelectOption( label=f"Todays Price Levels:", description=f"Open: {open} Current: {close} Low: {low} High: {high}"),
        disnake.SelectOption( label=f"Latest Earnings",description=f"🗓️ {latestEarningsDate}" ),
        disnake.SelectOption( label=f"52 Week High:", description=f"🎯 {fiftyTwoWkHigh}"),
        disnake.SelectOption( label=f"52 Week Low:", description=f"🎯 {fiftyTwoWkLow}", ),
        disnake.SelectOption( label="Average Volume, 10 Days:", description=f"{avg10} million.", ),])

    async def callback(self, interaction:disnake.MessageCommandInteraction):
        pass
