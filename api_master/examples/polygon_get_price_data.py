import aiohttp
from cfg import YOUR_API_KEY


async def get_price_data(ticker: str):
    if ticker.startswith('SPX') or ticker.startswith("VIX"):
        ticker = ticker.replace(f"{ticker}", f"I:{ticker}")
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey={YOUR_API_KEY}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return
                data = await resp.json()
                results = data['results'] if 'results' in data else None
                value = results[0]['value']
                return value
    else:
        ticker = ticker
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey={YOUR_API_KEY}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return
                data = await resp.json()
                results = data['results'] if 'results' in data else None
                price = results[0]['session']['close']
                return price