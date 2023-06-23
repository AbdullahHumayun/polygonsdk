from datetime import datetime
import _discord.emojis as e

def check_macd_crossing(macd, signal, histogram):
    # The threshold for close to crossing can be set based on desired sensitivity
    threshold = 0.01
    
    # Check if the MACD line is greater than the signal line and the difference between the two is less than the threshold
    if macd > signal and abs(macd - signal) < threshold:
        return True
    else:
        return False


def check_macd_turn(macd_value, signal_value, threshold=0.01):
    if macd_value - signal_value > threshold:
        return "MACD is close to turning green"
    else:
        return "MACD is not close to turning green"


def check_rsi(rsi):
    if rsi <= 30:
        return f"RSI is oversold with an RSI of {rsi}"
    elif rsi >= 70:
        return f"RSI is overbought with an RSI of {rsi}"
    else:
        return f"RSI is neither overbought or oversold @ {rsi}"




def check_stock_spread(bid, ask, threshold=0.10):
    if bid is not None and ask is not None:
        spread = ask - bid
        if spread <= threshold:
            return True
        else:
            return False
        


def check_bullish_status(macd, rsi, sma, ema):
    """
    Determines the bullish status based on the MACD, RSI, SMA, and EMA values.

    Args:
        macd (float): The Moving Average Convergence Divergence (MACD) value.
        rsi (float): The Relative Strength Index (RSI) value.
        sma (float): The Simple Moving Average (SMA) value.
        ema (float): The Exponential Moving Average (EMA) value.
        timeframe (int, optional): The timeframe in minutes. Defaults to 1.

    Returns:
        list: A list of strings representing the bullish status based on the input values. The first element represents the EMA status, the second element represents the RSI status, and the third element represents the MACD status.
    """
    ema_status = "Neutral"
    if ema < sma:
        ema_status = "Bearish"
    elif ema > sma:
        ema_status = "Bullish"

    rsi_status = "Invalid RSI value"
    if rsi >= 70:
        rsi_status = "Extremely Bearish"
    elif rsi >= 51:
        rsi_status = "Bearish"
    elif rsi >= 30 and rsi <= 49:
        rsi_status = "Bullish"
    elif rsi < 30:
        rsi_status = "Extremely Bullish"
    elif rsi == 50:
        rsi_status = "Neutral"

    macd_status = "Neutral"
    if macd < 0:
        macd_status = "Bearish"
    elif macd > 0:
        macd_status = "Bullish"

    return [ema_status, rsi_status, macd_status]
def check_trend(ema, sma):
    """
    Determines trend based on the EMA and SMA values.

    Args:
        ema (float): The Exponential Moving Average (EMA) value.
        sma (float): The Simple Moving Average (SMA) value.

    Returns:
        str: The trend based on the EMA and SMA values. Can be one of the following: "Bullish", "Bearish", or "Neutral".
    """
    threshold = 0.005 * (ema + sma) / 2
    if ema > sma:
        if (ema - sma) > threshold:
            return "Bullish"
        else:
            return "Neutral"
    elif sma > ema:
        if (sma - ema) > threshold:
            return "Bearish"
        else:
            return "Neutral"
    else:
        return "Neutral"

def check_sentiment(m5_rsi, m10_rsi): ##needs improvement
    """
    Determines sentiment based on the 5-minute and 10-minute RSI values.

    Args:
        m5_rsi (float): The 5-minute RSI value.
        m10_rsi (float): The 10-minute RSI value.

    Returns:
        str: The sentiment based on the RSI values. Can be one of the following: "Bullish", "Bearish", or "Neutral".
    """
    bullish = 0
    bearish = 0
    if m5_rsi > 70:
        bearish += 1
    elif m5_rsi < 30:
        bullish += 1
    if m10_rsi > 70:
        bearish += 1
    elif m10_rsi < 30:
        bullish += 1
    if bullish > bearish:
        return "Bullish"
    elif bearish > bullish:
        return "Bearish"
    else:
        return "Neutral"
    

def check_price_deviation(price, vwap):
    deviation = (vwap - price) / vwap
    if deviation >= 0.15:
        return "True"
    else:
        return "False"

def check_unusual_option(volume, open_interest):
    if volume >= open_interest:
        return True
    else:
        return False

def check_vega(option_vega):
    if 0.02 <= option_vega <= 0.04:
        return True
    else:
        return False

def check_theta(option_theta):
    if 0.00100000 <= option_theta <= 0.001749327:
        return True
    else:
        return False

def check_gamma(gamma):
    if 0.09 <= gamma <= 0.50:
        return True
    else:
        return False
    


def days_left_until_expiration(expiration_date):
    expiration = datetime.strptime(expiration_date, "%Y-%m-%d")
    today = datetime.now()
    delta = expiration - today
    return delta.days
def check_implied_volatility(implied_volatility):
    if 0.16 <= implied_volatility <= 0.38:
        return True
    else:
        return False
def interpret_crypto_condition(condition):
    if condition == 0:
        return f"{e.confirmed} Regular Trade"
    elif condition == 1:
        return f"{e.redcheck} Sell Side - The asset was sold at the prevailing best bid price on an exchange."
    elif condition == 2:
        return f"{e.greencheck} Buy Side - The asset was bought at the prevailing best ask price on an exchange."
def check_delta(delta):
    if 0.6 <= delta <= 0.85:
        return True
        
    elif -0.85 <= delta <= -0.6:
        return False