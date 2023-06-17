import aiohttp
import asyncio
import csv
import aiofiles
from cfg import YOUR_API_KEY as API_KEY
MAX_SIMULTANEOUS_REQUESTS = 50



    






async def fetch_all_option_contracts(expiration_date=None, expiration_date_lt=None, expiration_date_lte=None,
                                    expiration_date_gt=None, expiration_date_gte=None):
    """
        Fetches all option contracts from the Polygon API based on optional filter parameters.

        Args:
            expiration_date (Optional[str]): A string representing the expiration date (e.g. '2023-06-16') to filter by.
            expiration_date_lt (Optional[str]): A string representing the maximum expiration date (exclusive) to filter by.
            expiration_date_lte (Optional[str]): A string representing the maximum expiration date (inclusive) to filter by.
            expiration_date_gt (Optional[str]): A string representing the minimum expiration date (exclusive) to filter by.
            expiration_date_gte (Optional[str]): A string representing the minimum expiration date (inclusive) to filter by.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing the option contracts that match the given filters.
            Each dictionary contains the keys "ticker" and "underlying_ticker".
        """

    url = f'https://api.polygon.io/v3/reference/options/contracts?limit=1000&apiKey={API_KEY}'
    print(url)
    if expiration_date:
        url += f'&expiration_date={expiration_date}'
    if expiration_date_lt:
        url += f'&expiration_date.lt={expiration_date_lt}'
    if expiration_date_lte:
        url += f'&expiration_date.lte={expiration_date_lte}'
    if expiration_date_gt:
        url += f'&expiration_date.gt={expiration_date_gt}'
    if expiration_date_gte:
        url += f'&expiration_date.gte={expiration_date_gte}'
    
    contracts = []
    
    async with aiohttp.ClientSession() as session:
        while url:
            async with session.get(url) as response:

                data = await response.json()
                contracts.extend([{"ticker": contract["ticker"], "underlying_ticker": contract["underlying_ticker"]} for contract in data["results"]])
                print(data)
                # Check if there's a next URL and append the API key
                next_url = data.get("next_url")
                if next_url:
                    url = f"{next_url}&apiKey={API_KEY}"
                else:
                    url = None
                    
    return contracts

async def get_options_snapshot_async(contract, semaphore):
    """
    Fetches the options snapshot data for a given option contract from the Polygon API.

    Args:
        contract (Dict[str, str]): A dictionary containing the keys "ticker" and "underlying_ticker" for the option contract.
        semaphore (asyncio.Semaphore): A semaphore object to control concurrent access to the API.

    Returns:
        Optional[Dict[str, Any]]: A dictionary representing the snapshot data for the given option contract, or None if the request failed.
    """



    url = f'https://api.polygon.io/v3/snapshot/options/{contract["underlying_ticker"]}/{contract["ticker"]}?apiKey={API_KEY}'
    async with semaphore:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"Fetched snapshot for {contract['ticker']}: {data}")
                        return data["results"]
                    else:
                        print(f"An error occurred while fetching snapshot for {contract['ticker']}: {response.status}, {response.reason}, url={url}")
                        return None
        except aiohttp.ClientConnectorError:
            print(f"Failed to connect to {url}, retrying...")
            await asyncio.sleep(5)
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"Fetched snapshot for {contract['ticker']}: {data}")
                        return data["results"]
                    else:
                        print(f"An error occurred while fetching snapshot for {contract['ticker']}: {response.status}, {response.reason}, url={url}")
                        return None


async def write_snapshot_to_csv(writer, snapshot):
    """
    Write a snapshot of option data to a CSV file using the provided writer.
    :param writer: A CSV DictWriter object
    :param snapshot: A dictionary containing the snapshot of option data
    """
    if snapshot:
    
        details = snapshot["details"]
        greeks = snapshot["greeks"]
        last_quote = snapshot["last_quote"]
        underlying_asset = snapshot["underlying_asset"]
        print(underlying_asset)
        day = snapshot["day"]
        last_trade = snapshot["last_trade"]

        await writer.writerow({
            "ticker": details["ticker"],
            "break_even_price": snapshot.get("break_even_price", None),
            "contract_type": details.get("contract_type", None),
            "exercise_style": details.get("exercise_style", None),
            "expiration_date": details.get("expiration_date", None),
            "shares_per_contract": details.get("shares_per_contract", None),
            "strike_price": details.get("strike_price", None),
            "delta": greeks.get("delta", None),
            "gamma": greeks.get("gamma", None),
            "theta": greeks.get("theta", None),
            "vega": greeks.get("vega", None),
            "implied_volatility": snapshot.get("implied_volatility", None),
            "open_interest": snapshot.get("open_interest", None),
            "ask": last_quote.get("ask", None),
            "ask_size": last_quote.get("ask_size", None),
            "bid": last_quote.get("bid", None),
            "bid_size": last_quote.get("bid_size", None),
            "last_updated": last_quote.get("last_updated", None),
            "midpoint": last_quote.get("midpoint", None),
            "timeframe_quote": last_quote.get("timeframe", None),
            "last_trade_conditions": last_trade.get("conditions", None),
            "last_trade_exchange": last_trade.get("exchange", None),
            "last_trade_price": last_trade.get("price", None),
            "last_trade_sip_timestamp": last_trade.get("sip_timestamp", None),
            "last_trade_size": last_trade.get("size", None),
            "timeframe_trade": last_trade.get("timeframe", None),
            "day_change": day.get("change", None),
            "day_change_percent": day.get("change_percent", None),
            "day_close": day.get("close", None),
            "day_high": day.get("high", None),
            "day_last_updated": day.get("last_updated", None),
            "day_low": day.get("low", None),
            "day_open": day.get("open", None),
            "day_previous_close": day.get("previous_close", None),
            "day_volume": day.get("volume", None),
            "day_vwap": day.get("vwap", None),
            "change_to_break_even": underlying_asset.get("change_to_break_even", None),
            "price": underlying_asset.get("price", None),
            "underlying_ticker": underlying_asset.get("ticker", None),
        
        })
async def get_snapshots(option_contracts, output_file):

    semaphore = asyncio.Semaphore(MAX_SIMULTANEOUS_REQUESTS)
    async with aiofiles.open(output_file, mode='w', newline='') as csvfile:

        fieldnames = ["ticker", "break_even_price", "contract_type", "exercise_style", "expiration_date",
                      "shares_per_contract", "strike_price", "delta", "gamma", "theta", "vega", "implied_volatility",
                      "open_interest", "ask", "ask_size", "bid", "bid_size", "last_updated", "midpoint", "timeframe_quote",
                      "last_trade_conditions", "last_trade_exchange", "last_trade_price", "last_trade_sip_timestamp",
                      "last_trade_size", "timeframe_trade", "day_change", "day_change_percent", "day_close", "day_high",
                      "day_last_updated", "day_low", "day_open", "day_previous_close", "day_volume", "day_vwap",
                      "change_to_break_even", "price", "underlying_ticker", "my_custom_column"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the headers to the CSV file
        writer.writeheader()

        tasks = [
            get_options_snapshot_async(contract, semaphore) for contract in option_contracts
        ]

        snapshots = await asyncio.gather(*tasks)

        for snapshot in snapshots:
            if snapshot:  # Check if the snapshot is not None
                await write_snapshot_to_csv(writer, snapshot)

        return snapshots