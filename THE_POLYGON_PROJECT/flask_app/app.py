from flask import Flask
from flask import render_template, jsonify, request
import json

from static.dicts_lists.snippets import snippets
from funcs.get_data import get_webull_data











app = Flask(__name__)
print(app.url_map)
app.debug = True  # Enable debug mode


@app.route('/')
def index():
    return render_template('index.html')


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
            result_data["Cost Distribution"] = market_data[6]

        if market_data is not None and market_data[7]:
            result_data["Institutional Ownership"] = market_data[7]

        if market_data is not None and market_data[8]:
            result_data["Analyst Ratings"] = market_data[8]

        if market_data is not None and market_data[9]:
            result_data["Short Interest"] = market_data[9]

        if market_data is not None and market_data[10]:
            result_data["Latest News"] = market_data[10]

        if request.is_json:
            return jsonify(result_data.get("Stock Data", {}))
        else:
            return render_template("stock_data.html", result_data=result_data)



@app.route('/get-data')
def get_data():
    return render_template('get_data.html')

@app.route("/stock-data")
async def stock_data():
    ticker = ''
    data = await get_webull_data(ticker)
    return jsonify(data)    


@app.route('/snippets')
def render_snippets_template():
    snippets_json = json.dumps(snippets)
    with app.app_context():
        # Pass the snippets JSON to the HTML template
        return render_template('snippets.html', snippets_json=snippets_json)
    




if __name__ == '__main__':
    app.run()