import aiohttp
class CapitalFlow:
    """
    A class representing capital flow data for a stock.

    Attributes:
        superin (str): The amount of super large inflow formatted with commas.
        superout (str): The amount of super large outflow formatted with commas.
        supernet (str): The amount of super large net flow formatted with commas.
        largein (str): The amount of large inflow formatted with commas.
        largeout (str): The amount of large outflow formatted with commas.
        largenet (str): The amount of large net flow formatted with commas.
        newlargein (str): The amount of new large inflow formatted with commas.
        newlargeout (str): The amount of new large outflow formatted with commas.
        newlargenet (str): The amount of new large net flow formatted with commas.
        newlargeinratio (str): The new large inflow ratio formatted as a percentage with 2 decimal places.
        newlargeoutratio (str): The new large outflow ratio formatted as a percentage with 2 decimal places.
        mediumin (str): The amount of medium inflow formatted with commas.
        mediumout (str): The amount of medium outflow formatted with commas.
        mediumnet (str): The amount of medium net flow formatted with commas.
        mediuminratio (str): The medium inflow ratio formatted as a percentage with 2 decimal places.
        mediumoutratio (str): The medium outflow ratio formatted as a percentage with 2 decimal places.
        smallin (str): The amount of small inflow formatted with commas.
        smallout (str): The amount of small outflow formatted with commas.
        smallnet (str): The amount of small net flow formatted with commas.
        smallinratio (str): The small inflow ratio formatted as a percentage with 2 decimal places.
        smalloutratio (str): The small outflow ratio formatted as a percentage with 2 decimal places.
        majorin (str): The amount of major inflow formatted with commas.
        majorinratio (str): The major inflow ratio formatted as a percentage with 2 decimal places.
        majorout (str): The amount of major outflow formatted with commas.
        majoroutratio (str): The major outflow ratio formatted as a percentage with 2 decimal places.
        majornet (str): The amount of major net flow formatted with commas.
        retailin (str): The amount of retail inflow formatted with commas.
        retailinratio (str): The retail inflow ratio formatted as a percentage with 2 decimal places.
        retailout (str): The amount of retail outflow formatted with commas.
        retailoutratio (str): The retail outflow ratio formatted as a percentage with 2 decimal places.

    Methods:
        async def capital_flow(id: str) -> CapitalFlow:
            Returns an instance of the CapitalFlow class for a given stock ticker ID.
            The data is fetched asynchronously using aiohttp.
    """

    def __init__(self, item):
        self.superin = "{:,}".format(item.get('superLargeInflow', 0))
        self.superout = "{:,}".format(item.get('superLargeOutflow', 0))
        self.supernet = "{:,}".format(item.get('superLargeNetFlow', 0))
        self.largein = "{:,}".format(item.get('largeInflow', 0))
        self.largeout = "{:,}".format(item.get('largeOutflow', 0))
        self.largenet = "{:,}".format(item.get('largeNetFlow', 0))
        self.newlargein = "{:,}".format(item.get('newLargeInflow', 0))
        self.newlargeout = "{:,}".format(item.get('newLargeOutflow', 0))
        self.newlargenet = "{:,}".format(item.get('newLargeNetFlow', 0))
        self.newlargeinratio = "{:,.2f}".format(float(item.get('newLargeInflowRatio', 0)) * 100)
        self.newlargeoutratio = "{:,.2f}".format(float(item.get('newLargeOutflowRatio', 0)) * 100)
        self.mediumin = "{:,}".format(item.get('mediumInflow', 0))
        self.mediumout = "{:,}".format(item.get('mediumOutflow', 0))
        self.mediumnet = "{:,}".format(item.get('mediumNetFlow', 0))
        self.mediuminratio = "{:,.2f}".format(float(item.get('mediumInflowRatio', 0)) * 100)
        self.mediumoutratio = "{:,.2f}".format(float(item.get('mediumOutflowRatio', 0)) * 100)
        self.smallin = "{:,}".format(item.get('smallInflow', 0))
        self.smallout = "{:,}".format(item.get('smallOutflow', 0))
        self.smallnet = "{:,}".format(item.get('smallNetFlow', 0))
        self.smallinratio = "{:,.2f}".format(float(item.get('smallInflowRatio', 0)) * 100)
        self.smalloutratio = "{:,.2f}".format(float(item.get('smallOutflowRatio', 0)) * 100)
        self.majorin = "{:,}".format(item.get('majorInflow', 0))
        self.majorinratio = "{:,.2f}".format(float(item.get('majorInflowRatio', 0)) * 100)
        self.majorout = "{:,}".format(item.get('majorOutflow', 0))
        self.majoroutratio = "{:,.2f}".format(float(item.get('majorOutflowRatio', 0)) * 100)
        self.majornet = "{:,}".format(item.get('majorNetFlow', 0))
        self.retailin = "{:,}".format(item.get('retailInflow', 0))
        self.retailinratio = "{:,.2f}".format(float(item.get('retailInflowRatio', 0)) * 100)
        self.retailout = "{:,}".format(item.get('retailOutflow', 0))
        self.retailoutratio = "{:,.2f}".format(float(item.get('retailOutflowRatio', 0)) * 100)



    async def fetch_data(self, id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/ticker?tickerId={id}&showHis=true") as response:
                r = await response.json()
                latest = r.get('latest', None)
                if latest is not None:
                    item = latest.get('item', None)
                    if item is not None:
                        self.superin = item.get('superLargeInflow', 0)
                        self.superout = item.get('superLargeOutflow', 0)
                        self.supernet = item.get('superLargeNetFlow', 0)
                        self.largein = item.get('largeInflow', 0)
                        self.largeout = item.get('largeOutflow', 0)
                        self.largenet = item.get('largeNetFlow', 0)
                        self.newlargein = item.get('newLargeInflow', 0)
                        self.newlargeout = item.get('newLargeOutflow', 0)
                        self.newlargenet = item.get('newLargeNetFlow', 0)
                        self.newlargeinratio = round(float(item.get('newLargeInflowRatio', 0)) * 100, 2)
                        self.newlargeoutratio = round(float(item.get('newLargeOutflowRatio', 0)) * 100, 2)
                        self.mediumin = item.get('mediumInflow', 0)
                        self.mediumout = item.get('mediumOutflow', 0)
                        self.mediumnet = item.get('mediumNetFlow', 0)
                        self.mediuminratio = round(float(item.get('mediumInflowRatio', 0)) * 100, 2)
                        self.mediumoutratio = round(float(item.get('mediumOutflowRatio', 0)) * 100, 2)
                        self.smallin = item.get('smallInflow', 0)
                        self.smallout = item.get('smallOutflow', 0)
                        self.smallnet = item.get('smallNetFlow', 0)
                        self.smallinratio = round(float(item.get('smallInflowRatio', 0)) * 100, 2)
                        self.smalloutratio = round(float(item.get('smallOutflowRatio', 0)) * 100, 2)
                        self.majorin = item.get('majorInflow', 0)
                        self.majorinratio = round(float(item.get('majorInflowRatio', 0)) * 100, 2)
                        self.majorout = item.get('majorOutflow', 0)
                        self.majoroutratio = round(float(item.get('majorOutflowRatio', 0)) * 100, 2)
                        self.majornet = item.get('majorNetFlow', 0)
                        self.retailin = item.get('retailInflow', 0)
                        self.retailinratio = round(float(item.get('retailInflowRatio', 0)) * 100, 2)
                        self.retailout = item.get('retailOutflow', 0)
                        self.retailoutratio = round(float(item.get('retailOutflowRatio', 0)) * 100, 2)