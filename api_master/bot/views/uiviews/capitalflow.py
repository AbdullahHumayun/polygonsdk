import disnake
import stocksera
import requests
from cfg import YOUR_STOCKSERA_KEY
from utils.webull_tickers import ticker_list
client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)


class CapitalFlow1(disnake.ui.Select):
    def __init__(self, ticker):
        self.ticker=ticker
        r2 = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/ticker?tickerId={ticker}&showHis=true")
        d2 = r2.json()
        latest = d2['latest']
        date = latest['date']
        item = latest['item']
        superlgin=round(float(item["superLargeInflow"]*0.000001), ndigits=2)
        superlgout=round(float(item["superLargeOutflow"]*0.000001), ndigits=2)
        superlgnet=round(float(item["superLargeNetFlow"]*0.000001), ndigits=2)
        lgin = round(float(item["largeInflow"]*0.000001), ndigits=2)
        lgout =round(float(item["largeOutflow"]*0.000001), ndigits=2)
        lgnet = round(float(item["largeNetFlow"]*0.000001), ndigits=2)
        newlgin =round(float(item["newLargeInflow"]*0.000001), ndigits=2)
        newlgout = round(float(item["newLargeOutflow"]*0.000001), ndigits=2)
        newlgnet = round(float(item["newLargeNetFlow"]*0.000001), ndigits=2)
        medin = round(float(item["mediumInflow"]*0.000001), ndigits=2)
        medout = round(float(item["mediumOutflow"]*0.000001), ndigits=2)
        mednet = round(float(item["mediumNetFlow"]*0.000001), ndigits=2)
        smallin = round(float(item["smallInflow"]*0.000001), ndigits=2)
        smallout = round(float(item["smallOutflow"]*0.000001), ndigits=2)
        smallnet = round(float(item["smallNetFlow"]*0.000001), ndigits=2)
        majorin = round(float(item["majorInflow"]*0.000001), ndigits=2)
        majorout = round(float(item["majorOutflow"]*0.000001), ndigits=2)
        majornet = round(float(item["majorNetFlow"]*0.000001), ndigits=2)
        retailin = round(float(item["retailInflow"]*0.000001), ndigits=2)
        retailout = round(float(item["retailOutflow"]*0.000001), ndigits=2)
        retailinratio =round(float(item["retailInflowRatio"]*100), ndigits=2)
        retailoutratio = round(float(item["retailOutflowRatio"]*100), ndigits=2)
        newlginratio =round(float(item["newLargeInflowRatio"]*100), ndigits=2)
        newlgoutratio = round(float(item["newLargeOutflowRatio"]*100), ndigits=2)
        mediuminratio =round(float(item["mediumInflowRatio"]*100),ndigits=2)
        mediumoutratio = round(float(item["mediumOutflowRatio"]*100),ndigits=2)
        smallinratio =round(float(item["smallInflowRatio"]*100),ndigits=2)
        smalloutratio = round(float(item["smallOutflowRatio"]*100),ndigits=2)
        majorinratio =round(float(item["majorInflowRatio"]*100),ndigits=2)
        majoroutratio = round(float(item["majorOutflowRatio"]*100),ndigits=2)
        orderflow = requests.get(f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/stat?count=10&tickerId={ticker}&type=0")
        orderflowd = orderflow.json()
        dateset = orderflowd['dates']
        datelist = [i['date'] for i in dateset]

        date1 = datelist[0]
        sellvol1 = round(float(orderflowd['sellVolume']) * 0.000001, ndigits=2)
        nvol1 = round(float(orderflowd['nVolume']) * 0.000001, ndigits=2)
        buyvol1 = round(float(orderflowd['buyVolume']) * 0.000001, ndigits=2)
        avg1 = orderflowd['avePrice']
        max1 = round(float(orderflowd['maxT']) * 0.000001, ndigits=2)


        super().__init__(
        placeholder=f"🇴 🇷 🇩 🇪 🇷 🔥  🇫 🇱 🇴 🇼 for {ticker}",
        min_values=1,
        max_values=1,
        custom_id=f"flowselect",
        options= [
            disnake.SelectOption( label=f"New Ratio % IN: {newlginratio}%", description=f"New Ratio % OUT: {newlgoutratio}%", ),
            disnake.SelectOption( label="Today's Sell Flow", description=f"🔴{sellvol1} million.", ),
            disnake.SelectOption( label="Today's Buy Flow", description=f"🟢{buyvol1} million.", ),
            disnake.SelectOption( label="Today's Neutral Flow", description=f"⚫{nvol1} million.", ),
            disnake.SelectOption( label=f"NET Super Large Flow:", description=f"{superlgnet} million."),
            disnake.SelectOption( label=f"NET Major Flow:", description=f"{majornet} million."),
            disnake.SelectOption( label=f"NET Large Flow:", description=f"{lgnet} million."),
            disnake.SelectOption( label=f"NET Medium Flow:", description=f"{mednet} million."),
            disnake.SelectOption( label=f"NET Small Flow:", description=f"{smallnet} million.", ),
            disnake.SelectOption( label=f"🟢Retail Flow IN:", description=f"{retailin} million."),
            disnake.SelectOption( label=f"🔴Retail Flow OUT:", description=f"{retailout} million.", ),
            disnake.SelectOption( label=f"New Flow IN:", description=f"{newlgin} million."),
            disnake.SelectOption( label=f"New Flow OUT:", description=f"{newlgout} million.", ),])

    async def callback(self, interaction: disnake.MessageCommandInteraction):
        await interaction.send("Soon dad or mom, soon!")