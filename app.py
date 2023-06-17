

from flask import Flask
import asyncio
import requests
import aiohttp
from flask import Flask, render_template, request, jsonify

from funcs.get_data import get_webull_data
from sdks.stocksera_sdk.stocksera_sdk import StockseraSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from static.py.api_functions import get_top_gainers_data, volume_analysis_endpoint, financial_statement_endpoint,balance_sheet_endpoint, cash_flow_endpoint, balance_sheet_endpoint
from static.py.api_functions import financial_ratios_endpoint, capital_flow_endpoint, process_data


import asyncio
_stocksera = StockseraSDK()
webull = AsyncWebullSDK()

app = Flask(__name__)



@app.route('/api/volume_analysis/<string:ticker>')
async def volume_analysis(ticker):
    return await volume_analysis_endpoint(ticker)

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
    response = requests.get(f"http://localhost:5000/api/{ticker}")

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




@app.route('/')
def index():
    return render_template('index.html')





@app.route("/signals")
def home():
    return render_template('technical_signals.html')









@app.route("/stock-data")
async def stock_data():
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