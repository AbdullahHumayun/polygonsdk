import re
import random
# Identify options strategies
def identify_options_strategy(call_options, put_options):
    processed_symbols = set()
    strategies = {"vertical_spread":[], "diagonal_spread":[], "bear_call_spread":[], "bear_put_spread":[], "bull_call_spread":[], "bull_put_spread":[], "butterfly_spread":[], "calendar_spread":[], "straddle":[]}
    options_symbols = call_options + put_options
    for symbol in options_symbols:
        if symbol in processed_symbols:
            continue
        match = re.search(r'O:(\w{1,5})(\d{2})(\d{2})(\d{2})([CP])(\d+)', symbol)
        underlying_symbol, year, month, day, call_put, strike_price = match.groups()
        expiry_date = month + '/' + day + '/' + '20' + year
        strike_price = float(strike_price)/1000
        for symbol_compare in options_symbols:
            if symbol_compare in processed_symbols or symbol_compare == symbol:
                continue
            match = re.search(r'O:(\w{1,5})(\d{2})(\d{2})(\d{2})([CP])(\d+)', symbol_compare)
            underlying_symbol_compare, year_compare, month_compare, day_compare, call_put_compare, strike_price_compare = match.groups()
            expiry_date_compare = month_compare + '/' + day_compare + '/' + '20' + year_compare
            strike_price_compare = float(strike_price_compare)/1000
            if underlying_symbol == underlying_symbol_compare and expiry_date == expiry_date_compare and call_put != call_put_compare:
                if call_put == "C" and strike_price > strike_price_compare:
                    strategies["bear_call_spread"].append(symbol)
                    strategies["bear_call_spread"].append(symbol_compare)
                    processed_symbols.add(symbol)
                    processed_symbols.add(symbol_compare)
                elif call_put == "P" and strike_price < strike_price_compare:
                    strategies["bear_put_spread"].append(symbol)
                    strategies["bear_put_spread"].append(symbol_compare)
                    processed_symbols.add(symbol)
                    processed_symbols.add(symbol_compare)
                elif call_put == "C" and strike_price < strike_price_compare:
                    strategies["bull_call_spread"].append(symbol)
                    strategies["bull_call_spread"].append(symbol_compare)
                    processed_symbols.add(symbol)
                    processed_symbols.add(symbol_compare)
                elif call_put == "P" and strike_price > strike_price_compare:
                    strategies["bull_put_spread"].append(symbol)
                    strategies["bull_put_spread"].append(symbol_compare)
                    processed_symbols.add(symbol)
                    processed_symbols.add(symbol_compare)
                elif underlying_symbol == underlying_symbol_compare and expiry_date != expiry_date_compare:
                    strategies["calendar_spread"].append(symbol)
                    strategies["calendar_spread"].append(symbol_compare)
                    processed_symbols.add(symbol)
                    processed_symbols.add(symbol_compare)
            elif underlying_symbol == underlying_symbol_compare and expiry_date == expiry_date_compare and strike_price != strike_price_compare:
                strategies["diagonal_spread"].append(symbol)
                strategies["diagonal_spread"].append(symbol_compare)
                processed_symbols.add(symbol)
                processed_symbols.add(symbol_compare)
                
    return {strategy: symbols for strategy, symbols in strategies.items() if symbols}


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
        orig_form_list.append("O:" + underlying_symbol + year[-2:] + month + day + call_put + str(strike_price))
    return orig_form_list