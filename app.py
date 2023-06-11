from flask import Flask
from flask import Flask, render_template, request, jsonify

from .flask_app.funcs.get_data import get_webull_data




app = Flask(__name__)








@app.route('/')
def index():
    return render_template('index.html')


@app.route('/snippets')
def snippets():
    return render_template('snippets.html')


@app.route("/submit", methods=["POST", "GET"])
async def submit_form():
    if request.method == "POST":
        if request.is_json:
            json_data = request.get_json()
            ticker = json_data["ticker"]
        else:
            ticker = request.form["ticker"]

        *market_data, = await get_webull_data(ticker)

        result_data = {}

        if market_data is not None and market_data[0]:
            result_data["Stock Data"] = market_data[0]

        if market_data is not None and market_data[1]:
            result_data["Volume Analysis"] = market_data[1]

        if market_data is not None and market_data[2]:
            result_data["Financials"] = market_data[2]

        if market_data is not None and market_data[3]:
            result_data["Cash Flow"] = market_data[3]

        if market_data is not None and market_data[4]:
            result_data["Balance Sheet"] = market_data[4]

        if market_data is not None and market_data[5]:
            result_data["Capital Flow"] = market_data[5]

        if market_data is not None and market_data[6]:
            result_data["Institutional Ownership"] = market_data[6]

        if market_data is not None and market_data[7]:
            result_data["Analyst Ratings"] = market_data[7]

        if market_data is not None and market_data[8]:
            result_data["Short Interest"] = market_data[8]


        if request.is_json:
            return jsonify(result_data.get("Stock Data", {}))
        else:
            return render_template("stock_data.html", result_data=result_data)




@app.route("/stock-data")
async def stock_data():
    ticker = ''
    data = await get_webull_data(ticker)
    return jsonify(data)




if __name__ == '__main__':
    app.run()