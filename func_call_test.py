import openai
import json
import pandas as pd
from api_master.cfg import YOUR_OPENAI_KEY, YOUR_API_KEY
from api_master.sdks.webull_sdk.webull_sdk import AsyncWebullSDK

from api_master.sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from api_master.sdks.polygon_sdk.masterSDK import MasterSDK
from api_master.sdks.stocksera_sdk.sdk import StockeraSDK
openai.api_key = YOUR_OPENAI_KEY
import asyncio
opts = PolygonOptionsSDK(YOUR_API_KEY)
poly = AsyncPolygonSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()
master = MasterSDK()

stocksera = StockeraSDK()
# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
ticker = "UPST"
async def analyze_data(ticker):

    price = await opts.get_stock_price(ticker)

    volume_analysis = await webull.get_webull_vol_analysis_data(ticker)

    buyVolume = volume_analysis.buyVolume
    sellVolume = volume_analysis.sellVolume
    nVolume = volume_analysis.nVolume
    avgPrice = volume_analysis.avePrice

    rsi_hour = await poly.get_rsi(ticker, timespan="hour")
    rsi_hour = rsi_hour.rsi_value[0]

    rsi_day = await poly.get_rsi(ticker, timespan="day")
    rsi_day = rsi_day.rsi_value[0]

    rsi_week = await poly.get_rsi(ticker, timespan="week")
    rsi_week = rsi_week.rsi_value[0]

    financials = await webull.calculate_ratios(await webull.get_balancesheet(ticker), await webull.get_financial_statement(ticker), await webull.get_cash_flow(ticker), price)

    tickers = await master.get_near_the_money_single(ticker,threshold=5)
    universal_snap = await opts.get_universal_snapshot(tickers)
        
    stock_data = await webull.get_webull_stock_data(ticker)

    fifty_high = stock_data.fifty_high
    fifty_low = stock_data.fifty_low
    vibration = stock_data.web_vibrate_ratio



    ask=universal_snap.ask
    bid=universal_snap.bid
    bid_size=universal_snap.ask_size
    ask_size=universal_snap.bid_size
    change_percent=universal_snap.change_percent
    volume=universal_snap.volume
    open_interest = universal_snap.open_interest
    implied_volatility=universal_snap.implied_volatility
    gamma=universal_snap.gamma
    vega= universal_snap.vega
    delta=universal_snap.delta
    theta=universal_snap.theta
    strike_price=universal_snap.strike
    expiration = universal_snap.expiry

    return { 
        'Underlying Data': {
        'buyVolume': buyVolume,
        'sellVolume':sellVolume,
        'neutralVolume':nVolume,
        'avgPrice': avgPrice,
        'Stock Price': price,
        'Fifty Two Week High': fifty_high,
        'Fifty Two Week Low': fifty_low,
        'Vibration Ratio': fifty_low},

        'Options Data': { 
            'ask': ask,
            'bid': bid,
            'ask_size': ask_size,
            'bid_size': bid_size,
            'volume': volume,
            'open_interest': open_interest,
            'gamma':gamma,
            'vega':vega,
            'delta':delta,
            'theta':theta,
            'change_percent':change_percent,
            'strike_price':strike_price,
            'expiration':expiration,
            'implied_volatility': implied_volatility,
        },

        'Technical Analysis': {

            'rsi_hour': rsi_hour,
            'rsi_day': rsi_day,
            'rsi_week': rsi_week
        },

        'Latest Earnings Numbers': {
            'Financial Ratios': financials,
        },

        'Option Contracts Near The Money': {
            
            'contracts': tickers
        }
        
    }








async def run_conversation(ticker):
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "user", "content": f"Use all of the data and come up with a solution. Pay close attention to the option IV versus the current price. Things to look for: The lowest IV versus the price. If the lowest IV is lower than the current price = bearish. Also - note the RSI. An rsi near 70 = overbought (bearish). An RSI near 30 is oversold (bullish). A stock trading near 52 week high is bearish. A stock trading near 52 week low is bullish."}]
    functions = [
        {
            "name": "analyze_data",
            "description": "Analyze the given data to determine the likely direction.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": f"The ticker to query. {ticker}",
                    },
                },
                "required": ["ticker"],
                "returns": {"strike_price": "the strike price of the option symbol", "expiration": "the expiration date of the option symbol.", "implied_volatility": "the implied_volatility of the option symbol", "theta": "the theta value", "gamma": "the gamma value", "delta": "the delta value", "vega": "the vega value", "change_percent": "the contract's performance.", "ask": "the ask price", "bid": "the bid price", "ask_size": "the size of the ask", "bid_size": "the size of the bid", "volume": "the volume of the option", "open_interest":"the open interest for the option"}
            },
        },

    ]
    while True:
        # Send user message and get GPT's response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=functions,
            function_call="auto",
        )
        response_message = response["choices"][0]["message"]
        print(response_message)
        
        # Check if GPT wanted to call a function
        if response_message.get("function_call"):
            # Call the function
            available_functions = {
                "analyze_data": analyze_data,
            }
            function_name = response_message["function_call"]["name"]
            function_to_call = available_functions[function_name]
            function_args = json.loads(response_message["function_call"]["arguments"])
            function_response = await function_to_call(
                **function_args,
            )
            print(function_response)
            
            # Convert function_response to a string format
            function_response_str = str(function_response)
            
            # Send the info on the function call and function response to GPT
            messages.append(response_message)  # extend conversation with assistant's reply
            messages.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response_str,
                }
            )
        else:
            # Send the user message and GPT's response to continue the conversation
            messages.append(response_message)  # extend conversation with assistant's reply
        
        # Check if the user wants to stop the conversation
        user_input = input("User: ")
        if user_input.lower() == "stop":
            break  # Exit the loop if the user inputs "Stop"
        
        # Add the user's message to the conversation
        messages.append({"role": "user", "content": user_input})

    return response_message

# Pass a single ticker
ticker = "UPST"
asyncio.run(run_conversation(ticker))