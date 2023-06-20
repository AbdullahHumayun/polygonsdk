import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio


from sdks.webull_sdk.webull_sdk import AsyncWebullSDK


sdk = AsyncWebullSDK()


async def main():

    ticker = "META"


    #institutional holdings data
    inst = await sdk.get_institutional_holdings(ticker)
    decrease_count = inst.institution_holding.decrease.institutional_count
    decrease_count_change = inst.institution_holding.decrease.holding_count_change
    increase_count = inst.institution_holding.increase.institutional_count
    increase_count_change = inst.institution_holding.increase.holding_count_change
    new_position_count = inst.institution_holding.new_position.institutional_count
    new_position_count_change = inst.institution_holding.new_position.holding_count_change
    sold_out_count = inst.institution_holding.sold_out.holding_count_change
    sold_out_count_change = inst.institution_holding.sold_out.holding_count_change
    total_count = inst.institution_holding.stat.holding_count
    total_count_change = inst.institution_holding.stat.holding_ratio
    total_ratio = inst.institution_holding.stat.holding_ratio
    total_ratio_change = inst.institution_holding.stat.holding_ratio_change
    total_institutions = inst.institution_holding.stat.institutional_count


    #attribute output
    print("decrease_count:", decrease_count)
    print("decrease_count_change:", decrease_count_change)
    print("increase_count:", increase_count)
    print("increase_count_change:", increase_count_change)
    print("new_position_count:", new_position_count)
    print("new_position_count_change:", new_position_count_change)
    print("sold_out_count:", sold_out_count)
    print("sold_out_count_change:", sold_out_count_change)
    print("total_count:", total_count)
    print("total_count_change:", total_count_change)
    print("total_ratio:", total_ratio)
    print("total_ratio_change:", total_ratio_change)
    print("total_institutions:", total_institutions)


asyncio.run(main())