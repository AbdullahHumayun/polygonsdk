import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import asyncio 

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from cfg import YOUR_API_KEY

poly = AsyncPolygonSDK(YOUR_API_KEY)
async def pivot_point():



    _ = await poly.get_pivot_points("GME", 1, "day", from_date="2023-05-01", to_date="2023-05-16")
    print(f"RESISTANCE: ${_.resistance1} ${ _.resistance2}")
    print(f"PIVOT POINT: ${_.pivot_point}")
    print(f"SUPPORT: ${_.support1} ${_.support2}")

    

asyncio.run(pivot_point())