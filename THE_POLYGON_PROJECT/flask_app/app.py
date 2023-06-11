from flask import Flask
from flask import render_template, jsonify
import json

from static.dicts_lists.snippets import snippets
from funcs.get_data import get_webull_data











app = Flask(__name__)
print(app.url_map)
app.debug = True  # Enable debug mode






@app.route('/snippets')
def render_snippets_template():
    snippets_json = json.dumps(snippets)
    with app.app_context():
        # Pass the snippets JSON to the HTML template
        return render_template('snippets.html', snippets_json=snippets_json)
    


@app.route("/stock-data")
async def stock_data():
    ticker = ''
    data = await get_webull_data(ticker)
    return jsonify(data)    


if __name__ == '__main__':
    app.run()