import re

def human_readable(string):
    try:
        match = re.search(r'O:(\w{1,5})(\d{2})(\d{2})(\d{2})([CP])(\d+)', string) #looks for the options symbol in O: format
        underlying_symbol, year, month, day, call_put, strike_price = match.groups()
    except TypeError:
        underlying_symbol = f"AMC"
        year = "23"
        month = "02"
        day = "17"
        call_put = "CALL"
        strike_price = "380000"
    
    expiry_date = month + '/' + day + '/' + '20' + year
    if call_put == 'C':
        call_put = 'Call'
    else:
        call_put = 'Put'
    strike_price = '${:.2f}'.format(float(strike_price)/1000)
    return "{} {} {} Expiring {}".format(underlying_symbol, strike_price, call_put, expiry_date)




    

def parse_options(symbols):
    call_options = []
    put_options = []
    for symbol in symbols:
        match = re.search(r'O:(\w{1,5})(\d{2})(\d{2})(\d{2})([CP])(\d+)', symbol)
        try:
            underlying_symbol, year, month, day, call_put, strike_price = match.groups()
            expiry_date = month + '/' + day + '/' + '20' + year
            strike_price = float(strike_price)/1000
        except AttributeError:
            continue
        
        if call_put == 'C':
            call_options.append(symbol)
        else:
            put_options.append(symbol)
    return call_options, put_options



def orig_form(human_readable_list):
    orig_form_list = []
    for human_readable_string in human_readable_list:
        match = re.search(r'(\w{1,5}) \$([\d.]+) (Call|Put) Expiring (\d{2}/\d{2}/\d{4})', human_readable_string)
        underlying_symbol, strike_price, call_put, expiry_date = match.groups()
        strike_price = int(float(strike_price)*1000)
        year = expiry_date[-4:]
        month, day = expiry_date[:2], expiry_date[3:5]
        call_put = 'C' if call_put == 'Call' else 'P'
        orig_form_list.append(underlying_symbol + year[-2:] + month + day + call_put + str(strike_price))
    return orig_form_list


def map_options_exchanges(exchange):
    exchange_map = {
    300:'NYSE American Options',
    301:'Boston Options Exchange',
    302:'Chicago Board Options Exchange',
    303:'MIAX Emerald, LLC',
    304:'Cboe EDGX Options',
    307:'Nasdaq Global Markets Exchange Group',
    308:'International Securities Exchange, LLC',
    309:'Nasdaq MRX Options Exchange',
    312:'MIAX International Securities Exchange, LLC',
    313:'NYSE Arca, Inc. - Options',
    314:'Options Price Reporting Authority',
    315:'MIAX Pearl, LLC - Options',
    316:'Nasdaq Options Market',
    319:'Nasdaq BX - Options',
    322:'Cboe C2 Options Exchange',
    323:'Nasdaq Philadelphia Exchange, LLC - Options',
    325:'Cboe BZX Options Exchange'}
    return exchange_map.get(exchange, "Invalid ID")

def map_exchanges(id):
    exchange = { 
    1: 'NYSE American, LLC',
    2: 'Nasdaq OMX BX, Inc.',
    3: 'NYSE National, Inc.',
    4: 'FINRA NYSE TRF',
    4: 'FINRA Nasdaq TRF Carteret',
    4: 'FINRA Nasdaq TRF Chicago',
    4: 'FINRA Alternative Display Facility',
    5: 'Unlisted Trading Privileges',
    6: 'International Securities Exchange, LLC - Stocks',
    7: 'Cboe EDGA',
    8: 'Cboe EDGX',
    9: 'NYSE Chicago, Inc.',
    10: 'New York Stock Exchange',
    11: 'NYSE Arca, Inc.',
    12: 'Nasdaq',
    13: 'Consolidated Tape Association',
    14: 'Long-Term Stock Exchange',
    15: 'Investors Exchange',
    16: 'Cboe Stock Exchange',
    17: 'Nasdaq Philadelphia Exchange LLC',
    18: 'Cboe BYX',
    19: 'Cboe BZX',
    20: 'MIAX Pearl',
    21: 'Members Exchange',
    62: 'OTC Equity Security',
        }
    return exchange.get(id, "Invalid ID")