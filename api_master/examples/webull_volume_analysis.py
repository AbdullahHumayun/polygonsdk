import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio


from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

sdk = AsyncWebullSDK()


async def volume_analysis(ticker="AMZN"):


    volume_analysis = await sdk.get_webull_vol_analysis_data(ticker)
    buyvol = float(volume_analysis.buyVolume)
    sellvol = float(volume_analysis.sellVolume)
    neutvol = float(volume_analysis.nVolume)
    totalvol = float(volume_analysis.totalVolume)
    avgprice = volume_analysis.avePrice

    print(f"Buy Volume: {buyvol:,}")
    print(f"Neutral Volume: {neutvol:,}")
    print(f"Sell Volume: {sellvol}")
    print(f"Total Volume: {totalvol:,}")
    print(f"Avg Price: ${avgprice}")


asyncio.run(volume_analysis(ticker="AMZN"))