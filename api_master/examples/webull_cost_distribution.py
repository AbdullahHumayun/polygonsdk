import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio



from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

sdk = AsyncWebullSDK()


async def main():
    ticker = "MSFT"

    #access the function
    cost_dist = await sdk.cost_distribution(ticker)
    

    #use dot-notation to print the attributes

    avg_cost = cost_dist[0].avgCost
    chip70_end = cost_dist[0].chip70End
    chip70_ratio = cost_dist[0].chip70Ratio
    chip70_start = cost_dist[0].chip70Start
    chip90_end = cost_dist[0].chip90End
    chip90_ratio = cost_dist[0].chip90Ratio
    chip90_start = cost_dist[0].chip90Start
    close_price = cost_dist[0].close
    close_profit_ratio = cost_dist[0].closeProfitRatio
    distributions = cost_dist[0].distributions
    ticker_id = cost_dist[0].tickerId
    total_shares = cost_dist[0].totalShares
    avg_cost = cost_dist[0].avgCost


    #output

    print("avgCost:", avg_cost)
    print("chip70End:", chip70_end)
    print("chip70Ratio:", chip70_ratio)
    print("chip70Start:", chip70_start)
    print("chip90End:", chip90_end)
    print("chip90Ratio:", chip90_ratio)
    print("chip90Start:", chip90_start)
    print("close:", close_price)
    print("closeProfitRatio:", close_profit_ratio)
    print("distributions:", distributions)
    print("tickerId:", ticker_id)
    print("totalShares:", total_shares)
    print("avgCost:", avg_cost)

asyncio.run(main())