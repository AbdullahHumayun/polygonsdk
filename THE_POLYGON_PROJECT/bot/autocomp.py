
import os
import disnake
from disnake.ext import commands
import json
import typing
from typing import List, Dict
from typing import List
import pandas as pd


def ticker_autocomp(inter,ticker: str):
    if not ticker:
        return ["MUST", "USE", "CAPS"]
    print(f"ticker_autocomp [ticker]: {ticker}")
    tlow = ticker.lower()
    col_list = ["Name"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "tickers.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Name"]
    return [tickers for tickers in df if tickers.lower().startswith(tlow)][:24]



def graphics_autocomp(inter,graphic: str):
    if not graphic:
        return ["MUST", "USE", "CAPS"]
    print(f"graphic_autocomp [graphic]: {graphic}")
    tlow = graphic.lower()
    col_list = ["Graphics"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "images",
        "graphics.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Graphics"]
    return [graphics for graphics in df if graphics.lower().startswith(tlow)][:24]


def document_autocomp(inter,document: str):
    if not document:
        return ["MUST", "USE", "CAPS"]
    print(f"docs_autocomp document]: {document}")
    tlow = document.lower()
    col_list = ["Docs"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "docs_dict.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Docs"]
    return [document for document in df if document.lower().startswith(tlow)][:24]






def tickerlist_autocomp(inter,ticker: str):
    if not ticker:
        return ["TYPE", "SOMETHING", "DAD/MOM!"]
    print(f"ticker_autocomp [ticker]: {ticker}")
    tlow = ticker.lower()
    col_list = ["Name"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "ticker_list.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Name"]
    return [tickers for tickers in df if ticker.lower().startswith(tlow)][:24]

def contracts_autocomp(inter, contract: str):
    if not contract:
        return ["TYPE", "SOMETHING", "DAD/MOM!"]
    print(f"contracts_autocomp [contracts]: {contract}")
    tlow = contract.lower()
    col_list = ["Contracts"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "contracts.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Contracts"]
    return [contracts for contracts in df if contract.lower().startswith(tlow)][:24]

def derivatives_autocomp(inter, derivatives: str):
    if not derivatives:
        return ["TYPE", "SOMETHING", "DAD/MOM!"]
    print(f"derivatives_autocomp [derivatives]: {derivatives}")
    tlow = derivatives.lower()
    col_list = ["Derivatives"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "derivatives_list.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Derivatives"]
    return [derivative for derivative in df if derivatives.lower().startswith(tlow)][:24]


def test_autocomp(inter, contract: str):
    if not contract:
        return ["EXAMPLE SEARCH:", "10.0", "RETURNS CONTRACTS", "WITH 10% IV"]
    print(f"test_autocomp [cied]: {contract}")
    tlow = contract.lower()
    col_list = ["Test"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "test_list.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Test"]
    return [contract for contract in df if contract.lower().startswith(tlow)][:24]

def cited_autocomp(inter, cited: str):
    if not cited:
        return ["TYPE", "SOMETHING", "DAD/MOM!"]
    print(f"cited_autocomp [cied]: {cited}")
    tlow = cited.lower()
    col_list = ["Cited"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "cited_list.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Cited"]
    return [cited for cited in df if cited.lower().startswith(tlow)][:24]

def coin_autocomp(inter, coin: str):
    if not coin:
        return ["TYPE", "SOMETHING", "DAD/MOM!"]
    print(f"cited_autocomp [cied]: {coin}")
    tlow = coin.lower()
    col_list = ["Coin"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "crypto.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Coin"]
    return [coin for coin in df if coin.lower().startswith(tlow)][:24]

def core_autocomp(inter, core: str):
    if not core:
        return [
    "orcl09/30",
    "orcl10/07",
    "orcl10/14",
    "orcl10/21",
    "adbe09/23",
    "adbe09/30",
    "adbe10/07",
    "adbe10/14",
    "adbe10/21",
    "kepALL2022",
    "msb10/21",
    "msb11/18",
        ]
    print(f"option_autocomp [option]: {core}")
    tlow = core.lower()
    col_list = ["Core"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "core_options.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Core"]
    return [cores for cores in df if core.lower().startswith(tlow)][:24]

def options_autocomp(inter, option: str):
    if not option:
        return ["Search By %chance to close ITM"]
    print(f"option_autocomp [option]: {option}")
    tlow = option.lower()
    col_list = ["Options"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "options.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Options"]
    return [options for options in df if options.lower().startswith(tlow)][:24]

def spy_autocomp(inter, spy: str):
    if not spy:
        return ["EXAMPLE INPUT:", "SPY 419"]
    print(f"spy_autocomp [spy]: {spy}")
    tlow = spy.lower()
    col_list = ["Options"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "spy.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Options"]
    return [options for options in df if spy.lower().startswith(tlow)][:24]

def derivativeid_autocomp(inter, derivative_id: str):
    if not derivative_id:
        return ["TYPE", "SOMETHING", "DAD/MOM!"]
    print(f"ticker_derivativeid [derivative_id]: {derivative_id}")
    tlow = derivative_id.lower()
    col_list = ["Name"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "tickers3.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Name"]
    return [derivative_ids for derivative_ids in df if derivative_id.lower().startswith(tlow)][:24]

def definitions_autocomp(inter, definitions: str):
    if not definitions:
        return ["TYPE", "SOMETHING", "DAD/MOM!"]
    print(f"ticker_derivativeid [definitions]: {definitions}")
    tlow = definitions.lower()
    col_list = ["Name"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "definitions.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Name"]
    return [definitions for definitions in df if definitions.lower().startswith(tlow)][:24]

def video_autocomp(inter, video: str):
    if not video:
        return [f"Start", "Typing", "For", "Results!"]
    tlow = video.lower()
    col_list = ["Name"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "videos.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Name"]
    return [video for video in df if video.lower().startswith(tlow)][:24]




def tools_autocomp(inter, tools: str):
    if not tools:
        return [
        "Useful Links🔗",
        "Trader Tools🛠️",
        "Market Glossary📖"
        ]

    print(f"ticker_shortcuts [shortcuts]: {tools}")
    tlow = tools.lower()
    col_list = ["Tools"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "tools.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Tools"]
    return [tools for tools in df]

def videos_autocomp(inter, video: str):
    if not video:
        return [
    "China Videos📹",
    "NSCC Videos📹",
    "FINRA Videos📹",
    "OCC Videos📹",
    "NYSE Videos📹",
    "DTCC Videos📹",
    "NSFR Videos📹",
    "Options 101📹",
    "CBOE Videos📹",
    "ICE Videos📹",
    "ETF Videos📹",
    "SFT Videos📹",
        ]

    print(f"ticker_shortcuts [shortcuts]: {video}")
    tlow = video.lower()
    col_list = ["Videos"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "videos2.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Videos"]
    return [video for video in df]

def data_autocomp(inter, data: str):
    if not data:
        return [
        "Data",
        "BigMac",
        "Unemployment",
        "Inflation",
        "Repo",
        "Income Expenditures",
        "Debt",
        "Economic Indicators",
        "Money Supply",
        "Growth",
        "Interest Rate",
        "Futures",
        "Bitcoin",
        "SEC"
            ]

    print(f"data_shortcuts [shortcuts]: {data}")
    tlow = data.lower()
    col_list = ["Data"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "data.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Data"]
    return [data for data in df]


def type_autocomp(inter, type: str):
    if not type:
        return ["Highest IV 💉",
    "Top Open Interest Increase🛡️",
    "🏃‍♀️ Top Overall Total Open Interest / Volume 🧲",
    "🥃 Contracts with the most Volume",
    "Top Open Interest Decrease⚔️",
    "Top Overall Open Interest🛡️",]
    print(f"type : {type}")
    tlow = type.lower()
    col_list = ["Type"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "types.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Type"]
    return [type for type in df if type.lower().startswith(tlow)][:24]

def technicals_autocomp(inter, pattern: str):
    if not pattern:
        return ["TYPE", "A", "PATTERN!",]
    print(f"pattern : {pattern}")
    tlow = pattern.lower()
    col_list = ["Patterns"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "technicals.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Patterns"]
    return [pattern for pattern in df if pattern.lower().startswith(tlow)][:24]

def gifs_autocomp(inter, pattern: str):
    if not pattern:
        return [
        "Ascending Continuation Triangle",
        "Inside Bar (Bullish)",
        "Gap Down✨",
        "Head and Shoulders Bottom",
        "Double Bottom",
        "Gap Up✨",
        "Gravestone (Bullish)",
        "Engulfing Line (Bullish)",
        "Hammer",
        "Fast Stochastics",
        "Key Reversal Bar (Bullish)",
        "Triple Moving Average Crossover",
        "Pennant (Bearish)",
        "Rounded Top",
        "Rounded Bottom",
        "Double Top",
        "Triple Bottom",
        "Bollinger Bands",
        "Head and Shoulders Top",
        "Double Moving Average Crossover",
        "Price Crosses Moving Average",
        "Moving Average Convergence/Divergence (MACD)✨✨",
        "Momentum✨",
        "Pennant (Bullish)",
        "Top Triangle - Top Wedge",
        "Bottom Triangle - Bottom Wedge",
        "Triple Top",
        "Flag (Bullish)",
        "Engulfing Line (Bearish)",
        "Upside Breakout",
        "Island Top✨",
        "Continuation Wedge (Bullish)",
        "Megaphone Bottom",
        "Hanging Man",
        "Inverted Hammer",
        "Island Bottom✨",
        "Shooting Star",
        "Exhaustion Bar (Bullish)",
        "Continuation Wedge (Bearish)",
        "Megaphone Top",
        "Key Reversal Bar (Bearish)",
        "Two Bar Reversal (Bearish)",
        "Two Bar Reversal (Bullish)",
        "Williams %R",
        "Relative Strength Index (RSI)✨✨",
        "Flag (Bearish)",
        "Continuation Diamond (Bearish)",
        "Short-term KST",
        "Medium-term KST",
        "Downside Breakout",
        "Outside Bar (Bullish)",
        "Commodity Channel Index (CCI)",
        "Continuation Diamond (Bullish)",
        "Symmetrical Continuation Triangle (Bearish)",
        "Symmetrical Continuation Triangle (Bullish)",
        "Descending Continuation Triangle",
        "Diamond Bottom",
        "Outside Bar (Bearish)",
        "Diamond Top",
        "Gravestone (Bearish)",
        "Inside Bar (Bearish)",
        "Exhaustion Bar (Bearish)",
        "Slow Stochastic",
        "Long-term KST",
        ]
    print(f"pattern : {pattern}")
    tlow = pattern.lower()
    col_list = ["Query"]
    file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "gifs.csv",
    )
    df = pd.read_csv(file, usecols=col_list)
    df = df["Query"]
    return [pattern for pattern in df if pattern.lower().startswith(tlow)][0:24]



