import disnake
import requests


class ShortInterest(disnake.ui.Select):
    def __init__(self):
        url = "https://webull.p.rapidapi.com/stock/get-short-interest"

        querystring = {"tickerId":"913255598"}

        headers = {
            "X-RapidAPI-Key": "YOUR_RAPID_API_KEY",
            "X-RapidAPI-Host": "webull.p.rapidapi.com"
        }

        shortintr = requests.request("GET", url, headers=headers, params=querystring).json()

        shortint1= shortintr[0]
        setdate1=shortint1['settlementDate']
        si1=round(float(shortint1['shortInterst'])*0.000001,ndigits=2)
        avgvol1=round(float(shortint1['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc1=shortint1['daysToCover']


        shortint2= shortintr[1]
        setdate2=shortint2['settlementDate']
        si2=round(float(shortint2['shortInterst'])*0.000001,ndigits=2)
        avgvol2=round(float(shortint2['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc2=shortint2['daysToCover']


        shortint3= shortintr[2]
        setdate3=shortint3['settlementDate']
        si3=round(float(shortint3['shortInterst'])*0.000001,ndigits=2)
        avgvol3=round(float(shortint3['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc3=shortint3['daysToCover']


        shortint4= shortintr[3]
        setdate4=shortint4['settlementDate']
        si4=round(float(shortint4['shortInterst'])*0.000001,ndigits=2)
        avgvol4=round(float(shortint4['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc4=shortint4['daysToCover']

        shortint5= shortintr[4]
        setdate5=shortint5['settlementDate']
        si5=round(float(shortint5['shortInterst'])*0.000001,ndigits=2)
        avgvol5=round(float(shortint5['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc5=shortint5['daysToCover']

        shortint6= shortintr[5]
        setdate6=shortint6['settlementDate']
        si6=round(float(shortint6['shortInterst'])*0.000001,ndigits=2)
        avgvol6=round(float(shortint6['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc6=shortint6['daysToCover']

        shortint7= shortintr[6]
        setdate7=shortint7['settlementDate']
        si7=round(float(shortint7['shortInterst'])*0.000001,ndigits=2)
        avgvol7=round(float(shortint7['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc7=shortint7['daysToCover']

        shortint8= shortintr[7]
        setdate8=shortint8['settlementDate']
        si8=round(float(shortint8['shortInterst'])*0.000001,ndigits=2)
        avgvol8=round(float(shortint8['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc8=shortint8['daysToCover']

        shortint9= shortintr[8]
        setdate9=shortint9['settlementDate']
        si9=round(float(shortint9['shortInterst'])*0.000001,ndigits=2)
        avgvol9=round(float(shortint9['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc9=shortint9['daysToCover']

        shortint10= shortintr[9]
        setdate10=shortint10['settlementDate']
        si10=round(float(shortint10['shortInterst'])*0.000001,ndigits=2)
        avgvol10=round(float(shortint10['avgDailyShareVolume'])*0.000001,ndigits=2)
        dtc10=shortint10['daysToCover']


        super().__init__(
            placeholder="🇭 🇮 🇬 🇭 🩳  🇸 🇭 🇴 🇷 🇹 🇸",
            min_values=5,
            max_values=5,
            custom_id="shortintselect",
            options=[
            disnake.SelectOption(label=f"{setdate1} | Short Int: {si1}", description=f"Avg Volume: {avgvol1} | Days to Cover: {dtc1}"),
            disnake.SelectOption(label=f"{setdate2} | Short Int: {si2}", description=f"Avg Volume: {avgvol2} | Days to Cover: {dtc2}"),
            disnake.SelectOption(label=f"{setdate3} | Short Int: {si3}", description=f"Avg Volume: {avgvol3} | Days to Cover: {dtc3}"),
            disnake.SelectOption(label=f"{setdate4} | Short Int: {si4}", description=f"Avg Volume: {avgvol4} | Days to Cover: {dtc4}"),
            disnake.SelectOption(label=f"{setdate5} | Short Int: {si5}", description=f"Avg Volume: {avgvol5} | Days to Cover: {dtc5}"),
            disnake.SelectOption(label=f"{setdate6} | Short Int: {si6}", description=f"Avg Volume: {avgvol6} | Days to Cover: {dtc6}"),
            disnake.SelectOption(label=f"{setdate7} | Short Int: {si7}", description=f"Avg Volume: {avgvol7} | Days to Cover: {dtc7}"),
            disnake.SelectOption(label=f"{setdate8} | Short Int: {si8}", description=f"Avg Volume: {avgvol8} | Days to Cover: {dtc8}"),
            disnake.SelectOption(label=f"{setdate9} | Short Int: {si9}", description=f"Avg Volume: {avgvol9} | Days to Cover: {dtc9}"),
            disnake.SelectOption(label=f"{setdate10} | Short Int: {si10}", description=f"Avg Volume: {avgvol10} | Days to Cover: {dtc10}"),

            ]
        )

    async def callback(self, interaction:disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nDropdown for quick data references! No usage for clicking the results!!```")