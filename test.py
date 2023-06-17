from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
webull =AsyncWebullSDK()


import asyncio
import aiohttp
import pandas as pd


top_oi_decrease = {
    '1': "1117530682047078541",
    '2': "1117530680151265340",
    '3': "1117530678561624194",
    '4': "1117530676779036693",
    '5': "1117530683506692156",
    '6': "1118258134121717850",
    '7': '1118258136202088618',
    '8': "1118258137888215161",
    '9': "1118258139289112666",
    '10': "1118258140924870817",


}

top_vol_OPTIONS = { 

    '1': '1118318999713878246',
    '2': '1118319017296416778',
    '3': '1118319019099951134',
    '4': '1118319020307918950',
    '5': '1118319021452951592',
    '6': '1118319022665117898',
    '7': '1118319565013798932',
    '8': '1118319566905409657',
    '9': '1118319568532811816',
    '10': '1118319570038571088',
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Authorization": "Mzc1ODYyMjQwNjAxMDQ3MDcw.GE5kZ8.scHZxVpyK8WKEcyCCER_VBfgEzZ79u3HhS4ZEw"
}


async def update_oi_decrease_channel():
    async with aiohttp.ClientSession() as session:
        while True:
            # Retrieve the top options and relevant data
            df, top_options = await webull.top_options_chains("posDecrease")


            for i, row in df.head(10).iterrows():
                symbol = row['underlying_symbol']
                expiry = str(row['expiry'])[6:].replace('-', '▫️')
                strike = str(row['strike']).replace('.', '▫️')

                contract_type = row['direction']
                if contract_type == "call":
                    result = "🟢"

                if contract_type == "put":
                    result = "🔴"            
                channel_id = top_oi_decrease.get(str(i + 1))  # Get the channel ID based on the iteration index

                # Update channel name with symbol and expiration
                new_name = f"{symbol}💲{strike}{result}{expiry}"  # Modify this according to your desired channel name format

                async with session.patch(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers, json={"name": new_name}) as resp:
                    if resp.status != 200:
                        print(f"Error updating channel name: {resp.status}, {await resp.text()}")
                    else:
                        print(f"Successfully updated channel name for {symbol}.")
                    await asyncio.sleep(1)
              # Delay for one minute
async def update_top_volume_channels():
    async with aiohttp.ClientSession() as session:
        while True:
            df2, top_options2 = await webull.top_options_chains('volume')


            for i2, row2 in df2.head(10).iterrows():
                symbol2 = row2['underlying_symbol']
                expiry2 = str(row2['expiry'])[6:].replace('-', '▫️')
                strike2 = str(row2['strike']).replace('.', '▫️')

                contract_type2 = row2['direction']
                if contract_type2 == "call":
                    result2 = "🟢"

                if contract_type2 == "put":
                    result2 = "🔴"            
                channel_id2 = top_vol_OPTIONS.get(str(i2 + 1))  # Get the channel ID based on the iteration index

                # Update channel name with symbol and expiration
                new_name2 = f"{symbol2}💲{strike2}{result2}{expiry2}"  # Modify this according to your desired channel name format

                async with session.patch(f"https://discord.com/api/v9/channels/{channel_id2}", headers=headers, json={"name": new_name2}) as resp2:
                    if resp2.status != 200:
                        print(f"Error updating channel name: {resp2.status}, {await resp2.text()}")
                    else:
                        print(f"Successfully updated channel name for {symbol2}.")
                    await asyncio.sleep(1)

            await asyncio.sleep(360)  # Delay for one minute



async def main():
    while True:
        await update_top_volume_channels(
        
        )
        await update_oi_decrease_channel()


asyncio.run(main())