import requests
from time import sleep
import disnake
import stocksera
from api_master.cfg import YOUR_STOCKSERA_KEY
client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)

class ShortInt(disnake.ui.Select):
    def __init__(self):
        d = client.short_interest()
        shortint1 = d[0]
        sirank1 = shortint1['Rank']
        siticker1 = shortint1['Ticker']
        sidate1 = float(round(shortint1['Short Interest'])*0.000001,ndigits=2)
        siavgvol1 = float(round(shortint1['Average Volume'])*0.000001,ndigits=2)
        sidtc1 = shortint1['Days To Cover']
        sipshort1 = shortint1['%Float Short']

        shortint2 = d[1]
        sirank2 = shortint2['Rank']
        siticker2 = shortint2['Ticker']
        sidate2 = float(round(shortint2['Short Interest'])*0.000001,ndigits=2)
        siavgvol2 = float(round(shortint2['Average Volume'])*0.000001,ndigits=2)
        sidtc2 = shortint2['Days To Cover']
        sipshort2 = shortint2['%Float Short']



        shortint3 = d[2]
        sirank3 = shortint3['Rank']
        siticker3 = shortint3['Ticker']
        sidate3 = float(round(shortint3['Short Interest'])*0.000001,ndigits=2)
        siavgvol3 = float(round(shortint3['Average Volume'])*0.000001,ndigits=2)
        sidtc3 = shortint3['Days To Cover']
        sipshort3 = shortint3['%Float Short']



        shortint4 = d[3]
        sirank4 = shortint4['Rank']
        siticker4 = shortint4['Ticker']
        sidate4 = float(round(shortint4['Short Interest'])*0.000001,ndigits=2)
        siavgvol4 = float(round(shortint4['Average Volume'])*0.000001,ndigits=2)
        sidtc4 = shortint4['Days To Cover']
        sipshort4 = shortint4['%Float Short']




        shortint5 = d[4]
        sirank5 = shortint5['Rank']
        siticker5 = shortint5['Ticker']
        sidate5 = float(round(shortint5['Short Interest'])*0.000001,ndigits=2)
        siavgvol5 = float(round(shortint5['Average Volume'])*0.000001,ndigits=2)
        sidtc5 = shortint5['Days To Cover']
        sipshort5 = shortint5['%Float Short']



        shortint6 = d[5]
        sirank6 = shortint6['Rank']
        siticker6 = shortint6['Ticker']
        sidate6 = float(round(shortint6['Short Interest'])*0.000001,ndigits=2)
        siavgvol6 = float(round(shortint6['Average Volume'])*0.000001,ndigits=2)
        sidtc6 = shortint6['Days To Cover']
        sipshort6 = shortint6['%Float Short']




        shortint7 = d[6]
        sirank7 = shortint7['Rank']
        siticker7 = shortint7['Ticker']
        sidate7 = float(round(shortint7['Short Interest'])*0.000001,ndigits=2)
        siavgvol7 = float(round(shortint7['Average Volume'])*0.000001,ndigits=2)
        sidtc7 = shortint7['Days To Cover']
        sipshort7 = shortint7['%Float Short']




        shortint8 = d[7]
        sirank8 = shortint8['Rank']
        siticker8 = shortint8['Ticker']
        sidate8 = float(round(shortint8['Short Interest'])*0.000001,ndigits=2)
        siavgvol8 = float(round(shortint8['Average Volume'])*0.000001,ndigits=2)
        sidtc8 = shortint8['Days To Cover']
        sipshort8 = shortint8['%Float Short']


        shortint9 = d[8]
        sirank9 = shortint9['Rank']
        siticker9 = shortint9['Ticker']
        sidate9 = float(round(shortint9['Short Interest'])*0.000001,ndigits=2)
        siavgvol9 = float(round(shortint9['Average Volume'])*0.000001,ndigits=2)
        sidtc9 = shortint9['Days To Cover']
        sipshort9 = shortint9['%Float Short']


        shortint10 = d[9]
        sirank10 = shortint10['Rank']
        siticker10 = shortint10['Ticker']
        sidate10 = float(round(shortint10['Short Interest'])*0.000001,ndigits=2)
        siavgvol10 = float(round(shortint10['Average Volume'])*0.000001,ndigits=2)
        sidtc10 = shortint10['Days To Cover']
        sipshort10 = shortint10['%Float Short']


        shortint11 = d[10]
        sirank11 = shortint11['Rank']
        siticker11 = shortint11['Ticker']
        sidate11 = float(round(shortint11['Short Interest'])*0.000001,ndigits=2)
        siavgvol11 = float(round(shortint11['Average Volume'])*0.000001,ndigits=2)
        sidtc11 = shortint11['Days To Cover']
        sipshort11 = shortint11['%Float Short']


        shortint12 = d[11]
        sirank12 = shortint12['Rank']
        siticker12 = shortint12['Ticker']
        sidate12 = float(round(shortint12['Short Interest'])*0.000001,ndigits=2)
        siavgvol12 = float(round(shortint12['Average Volume'])*0.000001,ndigits=2)
        sidtc12 = shortint12['Days To Cover']
        sipshort12 = shortint12['%Float Short']


        shortint13 = d[12]
        sirank13 = shortint13['Rank']
        siticker13 = shortint13['Ticker']
        sidate13 = float(round(shortint13['Short Interest'])*0.000001,ndigits=2)
        siavgvol13 = float(round(shortint13['Average Volume'])*0.000001,ndigits=2)
        sidtc13 = shortint13['Days To Cover']
        sipshort13 = shortint13['%Float Short']


        shortint14 = d[13]
        sirank14 = shortint14['Rank']
        siticker14 = shortint14['Ticker']
        sidate14 = float(round(shortint14['Short Interest'])*0.000001,ndigits=2)
        siavgvol14 = float(round(shortint14['Average Volume'])*0.000001,ndigits=2)
        sidtc14 = shortint14['Days To Cover']
        sipshort14 = shortint14['%Float Short']


        shortint15 = d[14]
        sirank15 = shortint15['Rank']
        siticker15 = shortint15['Ticker']
        sidate15 = float(round(shortint15['Short Interest'])*0.000001,ndigits=2)
        siavgvol15 = float(round(shortint15['Average Volume'])*0.000001,ndigits=2)
        sidtc15 = shortint15['Days To Cover']
        sipshort15 = shortint15['%Float Short']


        shortint16 = d[15]
        sirank16 = shortint16['Rank']
        siticker16 = shortint16['Ticker']
        sidate16 = float(round(shortint16['Short Interest'])*0.000001,ndigits=2)
        siavgvol16 = float(round(shortint16['Average Volume'])*0.000001,ndigits=2)
        sidtc16 = shortint16['Days To Cover']
        sipshort16 = shortint16['%Float Short']


        shortint17 = d[16]
        sirank17 = shortint17['Rank']
        siticker17 = shortint17['Ticker']
        sidate17 = float(round(shortint17['Short Interest'])*0.000001,ndigits=2)
        siavgvol17 = float(round(shortint17['Average Volume'])*0.000001,ndigits=2)
        sidtc17 = shortint17['Days To Cover']
        sipshort17 = shortint17['%Float Short']


        shortint18 = d[17]
        sirank18 = shortint18['Rank']
        siticker18 = shortint18['Ticker']
        sidate18 = float(round(shortint18['Short Interest'])*0.000001,ndigits=2)
        siavgvol18 = float(round(shortint18['Average Volume'])*0.000001,ndigits=2)
        sidtc18 = shortint18['Days To Cover']
        sipshort18 = shortint18['%Float Short']


        shortint19 = d[18]
        sirank19 = shortint19['Rank']
        siticker19 = shortint19['Ticker']
        sidate19 = float(round(shortint19['Short Interest'])*0.000001,ndigits=2)
        siavgvol19 = float(round(shortint19['Average Volume'])*0.000001,ndigits=2)
        sidtc19 = shortint19['Days To Cover']
        sipshort19 = shortint19['%Float Short']


        shortint20 = d[19]
        sirank20 = shortint20['Rank']
        siticker20 = shortint20['Ticker']
        sidate20 = float(round(shortint20['Short Interest'])*0.000001,ndigits=2)
        siavgvol20 = float(round(shortint20['Average Volume'])*0.000001,ndigits=2)
        sidtc20 = shortint20['Days To Cover']
        sipshort20 = shortint20['%Float Short']


        shortint21 = d[20]
        sirank21 = shortint21['Rank']
        siticker21 = shortint21['Ticker']
        sidate21 = float(round(shortint21['Short Interest'])*0.000001,ndigits=2)
        siavgvol21 = float(round(shortint21['Average Volume'])*0.000001,ndigits=2)
        sidtc21 = shortint21['Days To Cover']
        sipshort21 = shortint21['%Float Short']



        shortint22 = d[21]
        sirank22 = shortint22['Rank']
        siticker22 = shortint22['Ticker']
        sidate22 = float(round(shortint22['Short Interest'])*0.000001,ndigits=2)
        siavgvol22 = float(round(shortint22['Average Volume'])*0.000001,ndigits=2)
        sidtc22 = shortint22['Days To Cover']
        sipshort22 = shortint22['%Float Short']


        shortint23 = d[22]
        sirank23 = shortint23['Rank']
        siticker23 = shortint23['Ticker']
        sidate23 = float(round(shortint23['Short Interest'])*0.000001,ndigits=2)
        siavgvol23 = float(round(shortint23['Average Volume'])*0.000001,ndigits=2)
        sidtc23 = shortint23['Days To Cover']
        sipshort23 = shortint23['%Float Short']


        shortint24 = d[23]
        sirank24 = shortint24['Rank']
        siticker24 = shortint24['Ticker']
        sidate24 = float(round(shortint24['Short Interest'])*0.000001,ndigits=2)
        siavgvol24 = float(round(shortint24['Average Volume'])*0.000001,ndigits=2)
        sidtc24 = shortint24['Days To Cover']
        sipshort24 = shortint24['%Float Short']



        super().__init__(
            placeholder="",
            minvalues=5,
            max_values=5,
            custom_id="shortintsel",
            options=[ 
                disnake.SelectOption(label=f"{sirank1}| {siticker1} | {sipshort1}", description=f"Avg Volume: {siavgvol1} | Days to Dover: {sidtc1} | Date: {sidate1}"),
                disnake.SelectOption(label=f"{sirank2}| {siticker2} | {sipshort2}", description=f"Avg Volume: {siavgvol2} | Days to Dover: {sidtc2} | Date: {sidate2}"),
                disnake.SelectOption(label=f"{sirank3}| {siticker3} | {sipshort3}", description=f"Avg Volume: {siavgvol3} | Days to Dover: {sidtc3} | Date: {sidate3}"),
                disnake.SelectOption(label=f"{sirank4}| {siticker4} | {sipshort4}", description=f"Avg Volume: {siavgvol4} | Days to Dover: {sidtc4} | Date: {sidate4}"),
                disnake.SelectOption(label=f"{sirank5}| {siticker5} | {sipshort5}", description=f"Avg Volume: {siavgvol5} | Days to Dover: {sidtc5} | Date: {sidate5}"),
                disnake.SelectOption(label=f"{sirank6}| {siticker6} | {sipshort6}", description=f"Avg Volume: {siavgvol6} | Days to Dover: {sidtc6} | Date: {sidate6}"),
                disnake.SelectOption(label=f"{sirank7}| {siticker7} | {sipshort7}", description=f"Avg Volume: {siavgvol7} | Days to Dover: {sidtc7} | Date: {sidate7}"),
                disnake.SelectOption(label=f"{sirank8}| {siticker8} | {sipshort8}", description=f"Avg Volume: {siavgvol8} | Days to Dover: {sidtc8} | Date: {sidate8}"),
                disnake.SelectOption(label=f"{sirank9}| {siticker9} | {sipshort9}", description=f"Avg Volume: {siavgvol9} | Days to Dover: {sidtc9} | Date: {sidate9}"),
                disnake.SelectOption(label=f"{sirank10}| {siticker10} | {sipshort10}", description=f"Avg Volume: {siavgvol10} | Days to Dover: {sidtc10} | Date: {sidate10}"),
                disnake.SelectOption(label=f"{sirank11}| {siticker11} | {sipshort11}", description=f"Avg Volume: {siavgvol11} | Days to Dover: {sidtc11} | Date: {sidate11}"),
                disnake.SelectOption(label=f"{sirank12}| {siticker12} | {sipshort12}", description=f"Avg Volume: {siavgvol12} | Days to Dover: {sidtc12} | Date: {sidate12}"),
                disnake.SelectOption(label=f"{sirank13}| {siticker13} | {sipshort13}", description=f"Avg Volume: {siavgvol13} | Days to Dover: {sidtc13} | Date: {sidate13}"),
                disnake.SelectOption(label=f"{sirank14}| {siticker14} | {sipshort14}", description=f"Avg Volume: {siavgvol14} | Days to Dover: {sidtc14} | Date: {sidate14}"),
                disnake.SelectOption(label=f"{sirank15}| {siticker15} | {sipshort15}", description=f"Avg Volume: {siavgvol15} | Days to Dover: {sidtc15} | Date: {sidate15}"),
                disnake.SelectOption(label=f"{sirank16}| {siticker16} | {sipshort16}", description=f"Avg Volume: {siavgvol16} | Days to Dover: {sidtc16} | Date: {sidate16}"),
                disnake.SelectOption(label=f"{sirank17}| {siticker17} | {sipshort17}", description=f"Avg Volume: {siavgvol17} | Days to Dover: {sidtc17} | Date: {sidate17}"),
                disnake.SelectOption(label=f"{sirank18}| {siticker18} | {sipshort18}", description=f"Avg Volume: {siavgvol18} | Days to Dover: {sidtc18} | Date: {sidate18}"),
                disnake.SelectOption(label=f"{sirank19}| {siticker19} | {sipshort19}", description=f"Avg Volume: {siavgvol19} | Days to Dover: {sidtc19} | Date: {sidate19}"),
                disnake.SelectOption(label=f"{sirank20}| {siticker20} | {sipshort20}", description=f"Avg Volume: {siavgvol20} | Days to Dover: {sidtc20} | Date: {sidate20}"),
                disnake.SelectOption(label=f"{sirank21}| {siticker21} | {sipshort21}", description=f"Avg Volume: {siavgvol21} | Days to Dover: {sidtc21} | Date: {sidate21}"),
                disnake.SelectOption(label=f"{sirank22}| {siticker22} | {sipshort22}", description=f"Avg Volume: {siavgvol22} | Days to Dover: {sidtc22} | Date: {sidate22}"),
                disnake.SelectOption(label=f"{sirank23}| {siticker23} | {sipshort23}", description=f"Avg Volume: {siavgvol23} | Days to Dover: {sidtc23} | Date: {sidate23}"),
                disnake.SelectOption(label=f"{sirank24}| {siticker24} | {sipshort24}", description=f"Avg Volume: {siavgvol24} | Days to Dover: {sidtc24} | Date: {sidate24}"),

            ]
        )




class ShortIntView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(ShortInt())
        self.add_item()



        




