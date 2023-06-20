import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio



from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

sdk = AsyncWebullSDK()




async def main():
    ticker="NVDA"

    #access the function
    analyst_ratings = await sdk.get_analysis_data(ticker)


    #access attributes with dot notation
    buyrate=analyst_ratings.buy
    holdrate=analyst_ratings.hold
    suggestion=analyst_ratings.rating_suggestion
    num_analysts=analyst_ratings.rating_totals
    sellrate=analyst_ratings.sell
    strongbuy=analyst_ratings.strongbuy
    underperform=analyst_ratings.underperform


    #output

    print("buy:", buyrate)
    print("hold:", holdrate)
    print("rating_suggestion:", suggestion)
    print("rating_totals:", num_analysts)
    print("sell:", sellrate)
    print("strongbuy:", strongbuy)
    print("underperform:", underperform)

asyncio.run(main())