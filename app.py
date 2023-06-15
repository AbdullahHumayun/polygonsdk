

from flask import Flask
from flask import Flask, render_template, request, jsonify
from static.py.website_components import components, load_content
from funcs.get_data import get_webull_data
from static.py.snippets import helpers, rest_api

import asyncio
app = Flask(__name__)





async def generate_html():
    await asyncio.sleep(1)  # Simulated loading delay
    title = 'Dynamic Web Page'
    css = 'styles.css'
    js = 'script.js'
    div_content = '<h1>Welcome to my dynamic web page!</h1><p>Loaded asynchronously.</p>'

    template = str(components)

    html_content = template.format(title=title, css=css, js=js, div_content=div_content)

    # Write the generated HTML content to a file
    with open('auto.html', 'w') as file:
        file.write(html_content)

    return html_content

@app.route('/auto')
async def auto():
    html_content = await generate_html()
    return html_content
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/markets')
def stock_page():
    return render_template('markets.html')

@app.route('/stock_commands')
def stock_commands():
    return render_template('stock_commands.html')



@app.route("/signals")
def home():
    return render_template('technical_signals.html')

@app.route("/mosh")
def mosh():
    return render_template('mosh.html')

@app.route("/snippets")
def snippets():
    return render_template('snippets.html')



@app.route("/about")
def about():
    return render_template('about.html')



@app.route("/snip")
def snip():
    return render_template('snip.html')

@app.route('/test')
def test():
    return render_template('test_scripts.html', helpers=helpers, rest_api=rest_api)

@app.route("/dropdowns")
def dropdowns():
    return render_template('dropdowns.html')

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