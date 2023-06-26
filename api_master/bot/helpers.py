from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
polygon = AsyncPolygonSDK(YOUR_API_KEY)
import disnake

def get_result(rsi_value):
    if rsi_value > 70:
        color = disnake.Colour.dark_red()
        result = "🐻"
    elif rsi_value <= 30:
        color = disnake.Colour.dark_green()
        result = "🐂"
    else:
        color = disnake.Colour.dark_grey()
        result = "⬜"
    return color, result
