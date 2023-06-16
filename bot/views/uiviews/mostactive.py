import requests
import disnake

class MostActive(disnake.ui.Select):
    def __init__(self):



        topactr = requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/ranking/topActive?regionId=6&rankType=volume&pageIndex=1&pageSize=50").json()
        topactrank = topactr['rankType']
        topactupdate = topactr['latestUpdateTime']
        topactdata = topactr['data']
        topact1 = topactdata[0]

        acttick1 = topact1['ticker']
        actchange1 = round(float(acttick1['changeRatio'])*100, ndigits=2)
        actprice1 = acttick1['close']
        actsym1 = acttick1['disSymbol']

        actval1 = topact1['values']
        valrank1 = round(float(actval1['rankValue'])*0.000001,ndigits=2)#volume


        topact2 = topactdata[1]

        acttick2 = topact2['ticker']
        actchange2 = round(float(acttick2['changeRatio'])*100, ndigits=2)
        actprice2 = acttick2['close']
        actsym2 = acttick2['disSymbol']

        actval2 = topact2['values']
        valrank2 = round(float(actval1['rankValue'])*0.000001,ndigits=2)#volume


        topact3 = topactdata[0]

        acttick3 = topact3['ticker']
        actchange3 = round(float(acttick3['changeRatio'])*100, ndigits=2)
        actprice3 = acttick3['close']
        actsym3 = acttick3['disSymbol']

        actval3 = topact3['values']
        valrank3 = round(float(actval3['rankValue'])*0.000001,ndigits=2)#volume


        topact4 = topactdata[0]

        acttick4 = topact4['ticker']
        actchange4 = round(float(acttick1['changeRatio'])*100, ndigits=2)
        actprice4 = acttick4['close']
        actsym4 = acttick4['disSymbol']

        actval4 = topact4['values']
        valrank4 = round(float(actval4['rankValue'])*0.000001,ndigits=2)#volume


        topact5 = topactdata[0]

        acttick5 = topact5['ticker']
        actchange5 = round(float(acttick1['changeRatio'])*100, ndigits=2)
        actprice5 = acttick5['close']
        actsym5 = acttick5['disSymbol']

        actval5 = topact5['values']
        valrank5 = round(float(actval5['rankValue'])*0.000001,ndigits=2)#volume

        topact6 = topactdata[0]

        acttick6 = topact6['ticker']
        actchange6 = round(float(acttick1['changeRatio'])*100, ndigits=2)
        actprice6 = acttick6['close']
        actsym6 = acttick6['disSymbol']

        actval6 = topact6['values']
        valrank6 = round(float(actval6['rankValue'])*0.000001,ndigits=2)#volume



        topact7 = topactdata[0]

        acttick7 = topact7['ticker']
        actchange7 = round(float(acttick1['changeRatio'])*100, ndigits=2)
        actprice7 = acttick7['close']
        actsym7 = acttick7['disSymbol']

        actval7 = topact7['values']
        valrank7 = round(float(actval7['rankValue'])*0.000001,ndigits=2)#volume


        topact8 = topactdata[0]

        acttick8 = topact8['ticker']
        actchange8 = round(float(acttick1['changeRatio'])*100, ndigits=2)
        actprice8 = acttick8['close']
        actsym8 = acttick8['disSymbol']

        actval8 = topact8['values']
        valrank8 = round(float(actval8['rankValue'])*0.000001,ndigits=2)#volume

        topact9 = topactdata[0]

        acttick9 = topact9['ticker']
        actchange9 = round(float(acttick1['changeRatio'])*100, ndigits=2)
        actprice9 = acttick9['close']
        actsym9 = acttick9['disSymbol']

        actval9 = topact9['values']
        valrank9 = round(float(actval9['rankValue'])*0.000001,ndigits=2)#volume


        topact10 = topactdata[0]

        acttick10 = topact10['ticker']
        actchange10 = round(float(acttick1['changeRatio'])*100, ndigits=2)
        actprice10 = acttick10['close']
        actsym10 = acttick10['disSymbol']

        actval10 = topact10['values']
        valrank10 = round(float(actval10['rankValue'])*0.000001,ndigits=2)#volume



        super().__init__(
            placeholder="",
            min_values=1,
            max_values=1,
            custom_id="mostactiveSel",
            options=[ 
                disnake.SelectOption(label=f"{actsym1} | Change on Day: {actchange1}%", description=f"Volume: {valrank1}"),
                disnake.SelectOption(label=f"{actsym2} | Change on Day: {actchange2}%", description=f"Volume: {valrank2}"),
                disnake.SelectOption(label=f"{actsym3} | Change on Day: {actchange3}%", description=f"Volume: {valrank3}"),
                disnake.SelectOption(label=f"{actsym4} | Change on Day: {actchange4}%", description=f"Volume: {valrank4}"),
                disnake.SelectOption(label=f"{actsym5} | Change on Day: {actchange5}%", description=f"Volume: {valrank5}"),
                disnake.SelectOption(label=f"{actsym6} | Change on Day: {actchange6}%", description=f"Volume: {valrank6}"),
                disnake.SelectOption(label=f"{actsym7} | Change on Day: {actchange7}%", description=f"Volume: {valrank7}"),
                disnake.SelectOption(label=f"{actsym8} | Change on Day: {actchange8}%", description=f"Volume: {valrank8}"),
                disnake.SelectOption(label=f"{actsym9} | Change on Day: {actchange9}%", description=f"Volume: {valrank9}"),
                disnake.SelectOption(label=f"{actsym10} | Change on Day: {actchange10}%", description=f"Volume: {valrank10}"),
            ]
        )


    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nSoon dad! Soon! For now - display only for quick referencing!```")