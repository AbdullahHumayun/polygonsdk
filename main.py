from polygon_sdk.get_latest_crypto_data import get_all_crypto_data
import asyncio

async def main():

    x = await get_all_crypto_data()


asyncio.run(main())