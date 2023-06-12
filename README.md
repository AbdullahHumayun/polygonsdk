



A terminal is being built: [polygonsdks](https://polygonsdks.herokuapp.com/)

# Welcome to the Polygon.io toolkit

This is a tool-kit designed for polygon.io users as well as anyone looking to integrate real-time data feeds into their personal Discord servers.

I'll be automating the creation process over-time, such as webhook and channel creation, as well as incorporating a stream-lined way to recieve

Discord feeds based upon your personal preference.


To view more in-depth README - please see the *read-me* folder.


Any questions can be sent to chuckdustin12@gmail.com and I'll do my best to reply promptly.


Here's a general walkthrough:


### STEP 1:
---
Visit https://www.polygon.io if you're wanting to work with their robust real-time data. Use code FUDSTOP at checkout to recieve a 10% discount.


Once you have your API key, you can place it in "cfg.py" after downloading or cloning the repo. Replace "YOUR POLYGON API KEY GOES HERE" with your API KEY.

---


### STEP 2:
---
You'll see five files in the root directory -

- 1. get_latest_crypto_data.py
- 2. get_latest_forex_data.py
- 3. get_latest_indices_data.py
- 4. get_latest_options_data.py
- 5. get_latest_ticker_data.py

Once you have your key, and depending on the service you chose - you can select the corresponding file and run it to generate a fresh spreadsheet of market-wide data.

For example - if you chose the stocks subscription - you would select *get_latest_ticker_data.py* and run it after placing your APIKEY into "cfg.py".

Once you have the file - you can then immediately utilize the *simulated_markets* sub-folder found in the *examples* folder to run a simulated options market or stock market data-stream using the latest data.

You can find real-time market stream examples in the *realtime_markets* folder.

If interested in the Discord aspect of this project - please see the discord readme inside of the *read-me* folder.

