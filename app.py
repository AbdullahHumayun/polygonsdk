

from flask import Flask
import asyncio
import requests
from flask_cors import CORS
import pandas as pd
import aiohttp
from flask import Flask, render_template, request, jsonify
from cfg import YOUR_API_KEY
from funcs.get_data import get_webull_data
from sdks.stocksera_sdk.stocksera_sdk import StockseraSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from static.py.api_functions import get_top_gainers_data, volume_analysis_endpoint, financial_statement_endpoint,balance_sheet_endpoint, cash_flow_endpoint, balance_sheet_endpoint
from static.py.api_functions import financial_ratios_endpoint, capital_flow_endpoint, process_data, institutional_holdings_endpoint,short_interest_endpoint
from static.py.api_functions import analyst_ratings_endpoint, stock_data_endpoint, get_filtered_contracts,get_near_the_money_symbols,get_price_data,get_top_gainers_data

import asyncio
_stocksera = StockseraSDK()
webull = AsyncWebullSDK()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
app = Flask(__name__)
CORS(app)

@app.route('/api/volume_analysis/<string:ticker>')
async def volume_analysis(ticker):
    return await volume_analysis_endpoint(ticker)
@app.route('/ticker_cards')
def ticker_cards():
    return render_template('ticker_cards.html')
@app.route('/api/top_gainers')
async def get_top_gainers_endpoint():
    return await get_top_gainers_data()
   

@app.route("/snippets")
def snippets():
    return render_template('snippets.html')


@app.route('/api/financial_statement/<string:ticker>')
async def financial_statement(ticker):
    data = await financial_statement_endpoint(ticker=ticker)
    return data


@app.route('/api/stock_data/<string:ticker>')
async def stock_data(ticker):
    data = await stock_data_endpoint(ticker=ticker)
    return data


@app.route('/api/institutional_holdings/<string:ticker>')
async def institutional_holdings(ticker):
    data = await institutional_holdings_endpoint(ticker=ticker)
    return data


@app.route('/api/analyst_ratings/<string:ticker>')
async def analyst_ratings(ticker):
    data = await analyst_ratings_endpoint(ticker)
    return data


@app.route('/api/short_interest/<string:ticker>')
async def short_interest(ticker):
    data = await short_interest_endpoint(ticker=ticker)
    return data


@app.route('/api/cash_flow/<string:ticker>')
async def cash_flow(ticker):

    return await cash_flow_endpoint(ticker=ticker)


@app.route('/api/balance_sheet/<string:ticker>')
async def balance_sheet(ticker):
    

    return await balance_sheet_endpoint(ticker)



@app.route('/api/financial_ratios/<string:ticker>')
async def get_financial_ratios(ticker):

    return await(financial_ratios_endpoint(ticker=ticker))

@app.route('/api/capital_flow/<string:ticker>')
async def get_capital_flow(ticker):
    

    return await(capital_flow_endpoint(ticker))

@app.route('/<ticker>')
def view(ticker):
    # Call the API endpoint to get the data
    response = requests.get(f"https://polygonsdks.herokuapp.com/api/{ticker}")

    if response.status_code == 200:
        data = response.json()
        return render_template('view.html', **data)
    else:
        return render_template('error.html', error="Failed to fetch data")



@app.route('/api/fetch_data', methods=['GET'])
async def fetch_data():
    result = await process_data()
    return jsonify(result)


@app.route('/api/home', methods=['GET'])
def apihome():
    ticker = request.args.get('ticker', '')  # Get the ticker from the query string
    return render_template('api_home.html', ticker=ticker)






@app.route("/signals")
def home():
    return render_template('technical_signals.html')




@app.route("/api/stock-data/<string:ticker>")
async def api_stock_data():
    ticker = ''
    data = await get_webull_data(ticker)
    return jsonify(data)



@app.route('/api_master/home')
def apimaster():
    return render_template('api_master.html')

if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    app.run(debug=True, use_reloader=False)
    loop.close()