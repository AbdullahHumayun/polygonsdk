import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.helpers.helpers import chunk_list
from sdks.polygon_sdk.universal_snapshot import CallsOrPuts, UniversalOptionSnapshot, UniversalSnapshot
from cfg import YOUR_API_KEY
opts = PolygonOptionsSDK(YOUR_API_KEY)


opts = PolygonOptionsSDK(YOUR_API_KEY)

polygon = AsyncPolygonSDK(YOUR_API_KEY)
import aiohttp
import asyncio
