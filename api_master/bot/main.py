import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _discord import emojis as e
import aiosonic
from mybot import ChannelsView
from sdks.polygon_sdk.list_sets import subscriptions as subs, sublist1
from func_call.func_view import FuncCall
from sdks.helpers.helpers import chunked
from disnake import File,Embed
from polygonIO.master_control import MasterControl
from func_call.stock_functions import fc_stock_functions
from cfg import thirty_days_from_now_str
import json
from new_views.viewmenus import ServerView
from cogs.analysis import Analysis
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from views.learnviews import AlertMenus
import pandas as pd
from sdks.helpers.helpers import chunked
from dataAnalyzer import DataAnalyzer
from cfg import seven_days_from_now_str, technicals_webhooks

from cogs.ss import SS
from cfg import hex_colors

from views.mainview import MainView
import asyncio
from sdks.datamaster import DataMaster
from cogs.learn import Learn
from cogs.fmp import FMP
import numpy as np
import disnake
from menus.embedmenus import PageSelect
from sdks.helpers.helpers import human_readable
from disnake.ext import commands

from autocomp import command_autocomp, ticker_autocomp
from cfg import two_years_from_now_str, today_str, thirty_days_ago_str
import aiohttp
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot,CallsOrPuts
from sdks.fudstop_sdk.fudstop_sdk import fudstopSDK
from menus.embedmenus import AlertMenus
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from cogs.skews import Skew

from tabulate import tabulate

from disnake.ext import commands

from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from _discord import emojis



fudstop_ = fudstopSDK()

from sdks.polygon_sdk.masterSDK import MasterSDK
mastery = MasterControl()

import aiohttp
import asyncio
import requests
from cfg import YOUR_API_KEY

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from polygonIO.master_control import MasterControl
from disnake.ext import commands
import disnake
from sdks.polygon_sdk.list_sets import sublist1

import pandas as pd
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from cfg import YOUR_DISCORD_BOT_TOKEN, YOUR_API_KEY,today_str, seven_days_from_now_str
from new_views.mainview import MainView
from autocomp import ticker_autocomp
from mybot import PersistentViewBot
from tabulate import tabulate
bot = PersistentViewBot(command_prefix="!", intents=disnake.Intents.all)
master = MasterControl()
opts = PolygonOptionsSDK(YOUR_API_KEY)

from new_views.atm_options import AtmOptionsSelect, AtmOptionsView



poly = AsyncPolygonSDK(YOUR_API_KEY)



import disnake
from disnake.ext import commands

from cfg import YOUR_API_KEY, YOUR_DISCORD_BOT_TOKEN



import csv
master = MasterSDK()
polygon = AsyncPolygonSDK(YOUR_API_KEY)
poly_options = PolygonOptionsSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()
from tabulate import tabulate
skew_cmds = Skew(bot=bot)
analysis_cmds = Analysis(bot)
learn_cmds = Learn(bot)
ss_cmds = SS(bot)
fmp_cmds = FMP(bot)


leftover={}
class MyBotYo(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=disnake.Intents.all())
        self.function_map = {
            "1": self.run_in_executor(webull.financial_score),
            "2": self.run_in_executor(webull.cost_distribution),
            "3": self.run_in_executor(webull.fifty_two_high_and_lows),
            "4": self.run_in_executor(webull.get_webull_stock_data),
            "5": self.run_in_executor(webull.get_balancesheet),
            "6": self.run_in_executor(webull.get_cash_flow),
            "7": self.run_in_executor(webull.get_financial_statement),
            "8": self.run_in_executor(webull.get_webull_vol_analysis_data),
            # add more functions here
        }
        self.conversation_history = {}

        
    def run_in_executor(self, func):
        async def wrapper(ticker):
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(None, func, ticker)
        return wrapper


@bot.command()
async def welcome(ctx):
    embed = disnake.Embed(title=f"Welcome to FUDSTOP!", description=f"```py\nTo begin - select the channels you want from the list of channels below.```")
    embed.add_field(name=f"➖OPTION VOLUME➖", value=f'> 1k➖5k volume\n> 5k➖10k volume\n> 10k➕ volume')
    embed.add_field(name=f"➖STOCK VOLUME➖", value=f"> 500➖1k volume\n \
                                                        > 1k➖5k volume\n \
                                                        > 5k➖10k volume\n \
                                                        > 20k➖50k volume\n \
                                                        > 50k➖100k volume\n \
                                                        > 100k➕ volume")
    embed.add_field(name=f"TECHNICAL📈SIGNALS", value=f"> os🐂minute🐂rsi\n \
                                        > ob🐻minute🐻rsi\n\n  \
                                        > os🐂hour🐂rsi\n  \
                                        > ob🐻hour🐻rsi\n\n  \
                                        > ob🐻day🐻rsi\n  \
                                        > os🐂day🐂rsi\n \n \
                                        > os🐂week🐂rsi\n  \
                                        > ob🐻week🐻rsi\n\n  \
                                        > super🐻overbought \
                                        > super🐂oversold")
    embed.add_field(name=f"🔮AI BOTS 🔮- TradyTics", value='> analyst🔮grades\n \
                                                            > breakouts🔮\n \
                                                            > bullseye🔮\n \
                                                            > darkpool🔮\n \
                                                            > golden🔮sweeps\n \
                                                            > crypto🔮signals\n \
                                                            > scalps🔮\n \
                                                            > insider🔮trades\n \
                                                            > ai🔮news\n \
                                                            > option🔮sweeps\n')

    embed.add_field(name=f'❗STOCK CONDITIONS❗', value='> financially🩸deficient\n \
                                                        > contingent🪃\n \
                                                        > retail🐐bid🐐ask\n \
                                                        > 🧹sweeps\n\ \
                                                        > ssr🪃\n \
                                                        > late📛filing\n \
                                                        > below📛req\n \
                                                        > bankrupt📛delinquent\n')
    embed.add_field(name=f'❗OPTIONS FEEDS❗', value=f"> spy🔻puts\n \
                                                        > spy🌲calls\n \
                                                        > spx🌲calls\n \
                                                        > spx🔻puts\n \
                                                        > zero⭕dte\n \
                                                        > unusual💥options\n \
                                                        > vwap💹options")
    

    embed.add_field(name="➖➖➖", value=f"➖➖➖", inline=False)
    
    embed.add_field(name=f"❗STOCK FEEDS❗", value=f"> squeeze💦potential\n \
                    > 🆕52_low\n \
                    > 🆕52_high\n \
                    > near🔻52🔻low\n \
                    > near🔺52🔺high\n \
                    > above⏫avg⏫vol\n \
                    > below⏬avg⏬vol\n \
                    > fire🔥sale\n \
                    > accumulation🚀\n \
                    > earnings💰today"
                    
                    )
    embed.add_field(name=f"📶 OPENBB 🇫 🇪 🇪 🇩 🇸🔔", value=f"> fd📶buys_sells\n \
        > fd📶opening_flow\n \
        > fd📶unusual_options\n \
        > fd📶goldensweep\n")
    

    embed.add_field(name=f"💫Momentum💫Scalps💫", value=f"> downside💫day⏬\n \
    upside💫day⏫\n \
    upside💫hour⏫\n \
    downside💫hour⏬")

    embed.add_field(name="➖➖➖", value=f"➖➖➖", inline=False)

    embed.add_field(name=f"❗OPTIONS EXCHANGES❗", value="> nyse🏭american\n \
                    > nyse🏭arca\n \
                    > nasdaq🏭global\n \
                    > nasdaq🏭mrx\n \
                    > nasdaq🏭philly\n \
                    > nasdaq🏭bx\n \
                    > cboe🏭bzx\n \
                    > cboe🏭c2\n \
                    > boston🏭exchange\n \
                    > miax🏭emerald\n \
                    > miax🏭pearl\n \
                    > cboe🏭edgx")
    

    embed.add_field(name=f"❗STOCK EXCHANGES❗", value=f"> finra🏛adf\n \
                    > ise🏛\n \
                    > nyse🏛\n \
                    > nyse🏛american\n \
                    > nyse🏛chicago\n \
                    > nyse🏛arca\n \
                    > nasdaq🏛\n \
                    > nasdaq🏛philly\n \
                    > members🏛exchange\n \
                    > investors🏛exchange\n \
                    > miax🏛pearl\n \
                    > cboe🏛edga\n \
                    > cboe🏛edgx\n \
                    > cboe🏛byx\n \
                    > cboe🏛bzx")




    await ctx.send(embed=embed)

# @bot.event
# async def on_ready():
#     # Assuming the guild ID is provided in the URL
#     guild_id = 888488311927242753
#     guild = bot.get_guild(guild_id)
#     if guild is None:
#         print(f"Unable to find the guild with ID {guild_id}")
#         return



#     for channel_name, channel_id in leftover.items():
#         # Get the channel object
#         channel = guild.get_channel(channel_id)
#         if channel is None:
#             print(f"Unable to find the channel with ID {channel_id}")
#             continue

#         # Create permissions for the role
#         permissions = disnake.Permissions(
#             read_messages=True,
#             read_message_history=True,
#             send_messages=True,
#             # Add any other necessary permissions here
#         )

#         # Create the role with the given permissions
#         # Create the role
#         try:
#             role = await guild.create_role(name=channel_name)
#             print(f"Role {channel_name} created successfully.")
#         except disnake.Forbidden:
#             print(f"Bot does not have permission to create role {channel_name}")
#             continue
#         except disnake.HTTPException:
#             print(f"Failed to create role {channel_name}")
#             continue

#         # Set the channel permissions for the role
#         overwrite = disnake.PermissionOverwrite(
#             read_messages=True,
#             read_message_history=True,
#             send_messages=True,
#             use_application_commands=True,
#             create_forum_threads=True,
#             create_public_threads=True,
#             manage_channels=False,
#             manage_permissions=False,
#             send_messages_in_threads=True,
#             add_reactions=True,
#             attach_files=True,
#             embed_links=True,
#             use_external_emojis=True,
#             external_stickers=True
#             # Add any other necessary permissions here
#         )
#         await channel.set_permissions(role, overwrite=overwrite)
#         print(f"Permissions set for role {channel_name} in channel {channel_name}")


@bot.command()
async def print_roles(ctx):
    for role in ctx.guild.roles:
        print(f"'{role.name}':'{role.id}',")
@bot.command()
async def m(ctx):
    await ctx.send(view=ServerView())



async def get_all_data(ticker):
    data_master = await DataMaster.create(ticker)
    
    return data_master


@bot.slash_command()
async def list_channels(inter: disnake.AppCmdInter):
    guild = inter.guild
    channels = guild.channels
    channel_dict = {}
    for channel in channels:
        channel_dict[channel.name] = channel.id
    print(channel_dict)


async def get_skews(ticker: str):
    data = await master.tabulate_options()
    data = data.drop(['Call IV%', 'Put IV%', 'Call Change', 'Put Change'], axis=1)  # Remove Call IV% and Put IV% columns
    data = data.rename(columns={'Low IV Call Strike': 'Res.', 'Low IV Put Strike': 'Supt.', 'Put OI': 'pOI', 'Call OI': 'cOI'})  # Rename columns

    # Remove "2023-" from the date results
    data['Exp'] = data['Exp'].str.replace(r'^2023-', '', regex=True)
    # Reorder columns
    columns = ['Sym', 'Exp', 'pOI', 'cOI','Supt.', 'Price',  'Res.']
    data = data[columns]
    # Create a new metric "depth"
    data['depth'] = data['Supt.'] - data['Res.']

    # Sort by the new metric
    data = data.sort_values(by='depth')
    data['Play'] = data.apply(lambda row: '🔴🔥' if row['Price'] > row['Res.'] and row['Price'] > row['Supt.'] else
                                       '🟢🔥' if row['Price'] < row['Res.'] and row['Price'] < row['Supt.'] else
                                       '🔴' if row['Price'] > row['Res.'] else
                                       '🟢' if row['Price'] < row['Supt.'] else
                                       '◽', axis=1)
    data = data.drop(columns=['depth'])

    # Convert DataFrame to JSON
    json_data = data.to_json(orient='records')

    return json_data
def paginate_dataframe(data, items_per_page=10):
    return [data[i:i+items_per_page] for i in range(0, len(data), items_per_page)]


@bot.slash_command()
async def atm_options(inter: disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
    """Returns ATM options to query further in the form of a select menu"""
    await inter.response.defer()
    atm = await master.get_near_the_money_single(ticker)

    data = str(atm).split(',')  # Split into list


    menus = []  # List to hold all select menus
    current_menu = AtmOptionsSelect()  # Start the first select menu

    for i, option in enumerate(data):
        if i != 0 and i % 25 == 0:  # If we've added 25 options
            menus.append(current_menu)  # Add the current menu to menus
            current_menu = AtmOptionsSelect()  # Start a new select menu

        # Add option to the current select menu
        current_menu.add_option(label=option, value=f"{human_readable(option) if option.startswith('O:') else option}_{i}")

    menus.append(current_menu)  # Add the last select menu to menus

    # Add menus to view and send view
    view = disnake.ui.View()
    for menu in menus:
        view.add_item(menu)

    await inter.edit_original_message("Please select an option:", view=view)

        
@bot.command()
async def channels(ctx):
    await ctx.send(view=ChannelsView())



@bot.slash_command()
async def atm_trades(inter: disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=ticker_autocomp)):
    """Returns all trades for the ATM options for a ticker."""
    await inter.response.defer()
    atm_options = await master.get_near_the_money_single(ticker, exp_greater_than=today_str, exp_less_than=seven_days_from_now_str)
    atm_options = str(atm_options).split(',')
    dfs = []  # A list to store each DataFrame
    for option in atm_options:
        trades = await opts.get_all_trades(option)
        df = pd.DataFrame(trades.data_dict)  # Convert the dictionary to a DataFrame
        df['OptionSymbol'] = human_readable(option)  # Add a new column for the option symbol
        dfs.append(df)  # Append the DataFrame to the list

    all_trades_df = pd.concat(dfs, ignore_index=True)  # Concatenate all DataFrames
    all_trades_df = all_trades_df.sort_values('OptionSymbol', ascending=False)
    print(all_trades_df)
    table = tabulate(all_trades_df, keys='headers', tablefmt='fancy')
    all_trades_df.to_csv('all_trades.csv')
    embed = disnake.Embed(title=f"All Trades - {ticker}", description=f"```py\nView the spreadsheet above to view all of the ATM option trades for {ticker}.```")
    await inter.edit_original_message(embed=embed, file=disnake.File("all_trades.csv"))






#clear read channels = 
#https://discord.com/api/v9/read-states/ack-bulk

@bot.command()
async def check(ctx):
# Assuming sublist1 is a list of tickers
    tickers = sublist1
    
    bulls,bears= await poly.get_upside_downside(tickers)
    print("Bearish:")
    bears = tabulate(bears, headers='keys', tablefmt='fancy', showindex=False)

    print("\nBullish:")
    bulls = tabulate(bulls, headers='keys', tablefmt='fancy', showindex=False)
        
    embed = disnake.Embed(title=f"Upside/Downside Results", description=f"**BULLISH**:\n```{bears}```\n**BEARISH:**\n```{bulls}```")
    embed.set_footer(text=f"Showing upside/downside candidates on the hourly.")
    await ctx.send(embed=embed)



@bot.slash_command()
async def fudstop(inter: disnake.AppCmdInter, ticker: str = commands.Param(autocomplete=ticker_autocomp)):
    """All In One"""
    
    await inter.response.defer()
    atm_options = await master.get_near_the_money_single(ticker)
    print(atm_options)
    _ = await master.get_universal_snapshot(atm_options)
    # Filter the dataframe for rows where 'C/P' is 'C' (for calls)
    calls_df = pd.DataFrame(_.skew_df)
    print(calls_df)
    calls_df = calls_df[calls_df['C/P'] == 'call'].sort_values('strike', ascending=True)
    calls_df['exp'] = calls_df['exp'].str.replace(r'^2023-', '', regex=True)

    # Convert the 'IV' column to numeric and percentage
    calls_df['iv'] = pd.to_numeric(calls_df['iv'], errors='coerce') * 100

    # Create a new 'skew' column filled with ' ' (empty space)
    calls_df['skew'] = ' '

    # Find the index of the row with the smallest IV for calls and puts
    lowest_iv_index_calls = calls_df['iv'].idxmin()
    calls_df['iv'] = calls_df['iv'].round(6)

    # Set the skew value to '<---' for the row with the lowest IV call
    calls_df.at[lowest_iv_index_calls, 'skew'] = '<---Skew'
    highest_vol_calls = calls_df['vol'].idxmax()
    calls_df.at[highest_vol_calls, 'skew'] = '<--TopVol' 

    calls_df.at[highest_vol_calls, 'skew'] = '<--TopOI' 


    df_divider = pd.DataFrame([['➖'] * calls_df.shape[1]], columns=calls_df.columns)

    # Filter the dataframe for rows where 'C/P' is 'P' (for puts)
    puts_df = pd.DataFrame(_.skew_df)
    puts_df = puts_df[puts_df['C/P'] == 'put'].sort_values('strike', ascending=False)
    puts_df['skew'] = ' '
    puts_df['iv'] = pd.to_numeric(puts_df['iv'], errors='coerce') * 100
    puts_df['exp'] = puts_df['exp'].str.replace(r'^2023-', '', regex=True)

    lowest_iv_index_puts = puts_df['iv'].idxmin()
    puts_df['iv'] = puts_df['iv'].round(6)
    puts_df.at[lowest_iv_index_puts, 'skew'] = '<--Skew'


    df_divider2 = pd.DataFrame([['➖'] * puts_df.shape[1]], columns=puts_df.columns)
    puts_df = puts_df.head(15)
    calls_df = calls_df.head(15)


    
    df_combined = pd.concat([calls_df, df_divider, df_divider2, puts_df], axis=0, ignore_index=True)

    tabulated_df = tabulate(df_combined, headers='keys', tablefmt='fancy', showindex=False)

    logo = await poly.get_polygon_logo(ticker)

    embed = disnake.Embed(title=f"Chain Monitor", description=f"```py\n{tabulated_df}```", color=disnake.Colour.random())
    
    embed.set_footer(text=f"View more data by selecting the category you want.", icon_url=logo)
    view = MainView(ticker,bot)


    await inter.edit_original_message(embed=embed, view=view)





@bot.slash_command()
async def chain(inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
    """Returns the ticker chain in real-time"""

    await inter.response.defer()
    counter = 0
    while True:
        counter = counter + 1
        atm_options = await master.get_near_the_money_single(ticker)
        print(atm_options)
        _ = await master.get_universal_snapshot(atm_options)
        # Filter the dataframe for rows where 'C/P' is 'C' (for calls)
        calls_df = pd.DataFrame(_.skew_df)
        calls_df = calls_df[calls_df['C/P'] == 'call'].sort_values('strike', ascending=True)
        calls_df['exp'] = calls_df['exp'].str.replace(r'^2023-', '', regex=True)

        # Convert the 'IV' column to numeric
        calls_df['iv'] = pd.to_numeric(calls_df['iv'], errors='coerce')

        # Create a new 'skew' column filled with ' ' (empty space)
        calls_df['skew'] = ' '
        
        ticker_name = calls_df['ticker'].iloc[0]  # Replace with the appropriate column name and dataframe if necessary

        # Find the index of the row with the smallest IV for calls and puts
        lowest_iv_index_calls = calls_df['iv'].idxmin()
        
        # Set the skew value to '<---' for these rows
        calls_df.at[lowest_iv_index_calls, 'skew'] = '<---🛡️'
        
        string = "Expiring"
        ticker_exp = calls_df['exp'].iloc[0]
        ticker_price = calls_df['Price'].iloc[0]
        df_divider = pd.DataFrame([['****'] * calls_df.shape[1]], columns=calls_df.columns)
        


        # Filter the dataframe for rows where 'C/P' is 'P' (for puts)
        puts_df = pd.DataFrame(_.skew_df)
        puts_df = puts_df[puts_df['C/P'] == 'put'].sort_values('strike', ascending=False)
        puts_df['skew'] = ' '
        puts_df['iv'] = pd.to_numeric(puts_df['iv'], errors='coerce')
        puts_df['exp'] = puts_df['exp'].str.replace(r'^2023-', '', regex=True)
        
        lowest_iv_index_puts = puts_df['iv'].idxmin()
        puts_df.at[lowest_iv_index_puts, 'skew'] = '<---⚔️'
        df_divider2 = pd.DataFrame([['****'] * puts_df.shape[1]], columns=puts_df.columns)

        
        ticker_row_index = len(calls_df) 
        ticker_row_index2 =len(calls_df) 
        


        # Your existing code
        puts_df = puts_df.drop(['name', 'ticker', 'price', 'mid'], axis=1)
        calls_df = calls_df.drop(['name', 'ticker', 'price', 'mid'], axis=1)
        df_divider = df_divider.drop(['name', 'ticker', 'price', 'mid'], axis=1)
        df_divider2 = df_divider2.drop(['name', 'ticker', 'price', 'mid'], axis=1)
        df_combined = pd.concat([calls_df, df_divider, puts_df], axis=0, ignore_index=True)
        df_combined.rename(columns={'call': 'c', 'put': 'p'})
        df_combined.at[ticker_row_index, 'exp'] = ticker_name
        df_combined.at[ticker_row_index, 'iv'] = ticker_price
        tabulated_df = tabulate(df_combined, headers='keys', tablefmt='fancy', showindex=False)
    
        

        embed = disnake.Embed(title=f"Chain Monitor", description=f"```py\n{tabulated_df}```")
        embed.add_field(name=f"Info:", value=f"> **Showing live chain for {ticker}**.\n> **Note: The '<---' is always pointing to the lowest IV strike price.**\n\n> 🛡️ = Support\n> ⚔️ = Resistance")

        await inter.edit_original_message(embed=embed)
        if counter == 100:
            break


@bot.slash_command()
async def oi(inter: disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=ticker_autocomp)):
    """Fetches OI for the nearest 5 options."""
    await inter.response.defer()
    counter = 0
    while True:
        counter = counter + 1
        calls,puts, results, data = await master.get_near_the_money_oi(ticker)
        data = data.drop(['Call IV%', 'Put IV%', 'Call Change', 'Put Change'], axis=1)  # Remove Call IV% and Put IV% columns
        data = data.rename(columns={'Low IV Call Strike': 'Res.', 'Low IV Put Strike': 'Supt.', 'Put OI': 'pOI', 'Call OI': 'cOI'})  # Rename columns


        # Remove "202sym3-" from the date results
        data['Exp'] = data['Exp'].str.replace(r'^2023-', '', regex=True)
        # Reorder columns
        columns = ['Sym', 'Exp', 'pOI', 'cOI','Supt.', 'Price', 'Res.']
        data = data[columns]
        # Create a new metric "depth"
        data['depth'] = data['Supt.'] - data['Res.']

        # Sort by the new metric
        data = data.sort_values(by='depth')
        data['Play'] = data.apply(lambda row: '🔴🔥' if row['Price'] > row['Res.'] and row['Price'] > row['Supt.'] else
                                        '🟢🔥' if row['Price'] < row['Res.'] and row['Price'] < row['Supt.'] else
                                        '🔴' if row['Price'] > row['Res.'] else
                                        '🟢' if row['Price'] < row['Supt.'] else
                                        '◽', axis=1)
        data = data.drop(columns=['depth'])
        calls = calls.applymap(lambda x: f'{x:,}' if isinstance(x, (int, float)) else x)
        puts = puts.applymap(lambda x: f'{x:,}' if isinstance(x, (int, float)) else x)
        embed = disnake.Embed()
        call_table = tabulate(calls, headers='keys', tablefmt='fancy', showindex=False)

        view = disnake.ui.View()
        
        put_table = tabulate(puts, headers='keys', tablefmt='fancy', showindex=False)
        embed.title=f"OI {ticker} | {results.underlying_price[0]}"
        embed.description=f"```py\nThink of OI as a shield. High OI for calls = resistance. High OI for puts = Support.```"
        embed.add_field(name=f"<a:_:1043589872885174292> ATM Calls:", value=f"```py\n{call_table}```", inline=False)

        embed.add_field(name=f"<a:_:1043589715145805934> ATM Puts: ", value=f"```py\n{put_table}```", inline=False)
        embed.add_field(name=f"Live Option Price:", value=f"> Bid: **${results.bid[0]}**\n> Mid: **${results.midpoint[0]}**\n> Ask: **${results.ask[0]}**")
        try:
            embed.add_field(name=f"Live Greeks:", value=f"> Delta: **{round(float(results.delta[0]),2)}**\n> Gamma: **{round(float(results.gamma[0]),2)}**\n> Theta: **{round(float(results.theta[0]),2)}**\n> Vega: **{round(float(results.vega[0]),2)}**")
        except TypeError:
            continue
        embed.add_field(name=f"Live Trades:", value=f"> Last Size: **{results.trade_size[0]}**\n> Price: **{results.trade_size[0]}**\n> Ticker: **${(results.strike[0])}** **{results.contract_type[0]}** **{results.expiry[0]}**")
        embed.add_field(name=f"Live Skew:", value=f"```py\n{data}```", inline=False)
        embed.color=disnake.Colour.dark_magenta()

        button = disnake.ui.Button(style=disnake.ButtonStyle.red, emoji=f"🛑")
        button.callback = lambda interaction: interaction.response.edit_message(f"> **Run Again -->**\n\n> </oi:1131482453857546260>")
        view.add_item(button)
        embed.set_footer(text=f"Live {ticker} price: ${results.underlying_price[0]}")
        
        await inter.edit_original_message(embed=embed, view=view)

        if counter == 150:
            await bot.reload.conjugate()

# @bot.slash_command()
# async def allskew(inter:disnake.AppCmdInter):
#     """Scans and returns all skews with a depth of 5 or more, or -5 or less."""
#     await inter.response.defer()
#     tasks = []

#     async def process_ticker(ticker, skews_outside_range):
#         x = await master.get_near_the_money_single(ticker, exp_greater_than=today_str, exp_less_than=seven_days_from_now_str)
#         if x is None:
#             return False

#         skew = await master.find_skew(x)

#         if 'Close' not in skew.columns or 'strike' not in skew.columns:
#             return False

#         skew['depth'] = skew['Strike'] - skew['Price']
        
#         mask = (skew['depth'] < -7.5) | (skew['depth'] > 7.5)
#         selected_columns = skew[mask][['sym', 'Price', 'strike', 'exp', 'depth', 'IV']]
#         selected_columns['exp'] = selected_columns['Exp'].str[5:]
#         selected_columns['IV'] = (selected_columns['IV'] * 100).round(5)
#         selected_columns['Direction'] = np.where(selected_columns['Price'] > selected_columns['Skew'], '🔥', '🟢')
#         skews_outside_range.extend(selected_columns.to_dict('records'))


#     counter = 0
#     print(counter)
#     skews_outside_range = []
#     while True:
#         counter = counter  + 1
#         subs = ['PTON', 'MTCH', 'SBUX', 'AZN', 'KHC', 'EBIX', 'ENPH', 'BTAI', 'BEKE', 'APA', 'CMG', 'HPQ', 'NNDM', 'SWN', 'KMI', 'SQQQ', 'SGEN', 'LNC', 'GFI', 'XOP', 'LOW', 'CHWY', 'DRI', 'TEVA', 'AMZN', 'BBY', 'WMB', 'ZM', 'AFRM', 'BYND', 'PARA', 'AMD', 'SAVE', 'UNG', 'FTCH', 'DM', 'C', 'TWLO', 'RUN', 'DNN', 'PBR', 'TSM', 'CIM', 'CCL', 'ORCL', 'DB', 'VFC', 'EEM', 'PDD', 'CPRI', 'GSAT', 'MGM', 'VLO', 'GT', 'MCD', 'MDB', 'AR', 'KO', 'NLY', 'FSLR', 'JWN', 'STNE', 'MRK', 'U', 'FCEL', 'IYR', 'UBS', 'VMW', 'ZIM', 'AMC', 'IQ', 'MRNA', 'EOSE', 'NKE', 'KWEB', 'XLE', 'MA', 'XLI', 'KR', 'DIS', 'FIS', 'IONQ', 'PG', 'NEM', 'TMC', 'AMGN', 'BCS', 'PAA', 'DOCU', 'ISEE', 'JBLU', 'CRWD', 'CMCSA', 'LAZR', 'CLOV', 'TLT', 'MARA', 'FUBO', 'IEF', 'HAL', 'NCLH', 'SPWR', 'CHPT', 'FDX', 'STLA', 'CRBU', 'AUPH', 'IBM', 'BA', 'MRVL', 'LABU', 'MP', 'MMM', 'MSFT', 'MT', 'TBT', 'ETSY', 'XHB', 'COTY', 'APLD', 'LCID', 'CLF', 'SIRI', 'SNDL', 'EWZ', 'NEE', 'RIO', 'TNA', 'JNJ', 'GENI', 'TFC', 'HD', 'KOLD', 'TECK', 'UAL', 'NKLA', 'SLV', 'LULU', 'DD', 'MET', 'GOLD', 'Z', 'BBBYQ', 'CVNA', 'EWJ', 'SABR', 'LVS', 'ASTS', 'SVXY', 'SLB', 'DOW', 'X', 'BBD', 'PLUG', 'COIN', 'ABT', 'ALB', 'UBER', 'GM', 'SCHW', 'XRT', 'RIOT', 'CBL', 'ABNB', 'RIVN', 'PINS', 'BITO', 'RUT', 'DDOG', 'DNA', 'TIP', 'SE', 'TDOC', 'CSCO', 'HL', 'GOEV', 'KRE', 'FUTU', 'XLU', 'SOXL', 'EFA', 'KEY', 'TRUP', 'NDX', 'LQD', 'GDX', 'SLG', 'GME', 'LLY', 'EWU', 'COST', 'QQQ', 'MRO', 'BMBL', 'AAL', 'PEP', 'NIO', 'LUV', 'IAT', 'XLV', 'SNAP', 'BMY', 'BTU', 'XLF', 'RCL', 'DOCN', 'AAP', 'MVIS', 'LRCX', 'UPS', 'INTC', 'HOOD', 'PAAS', 'SMH', 'MPW', 'WBA', 'BRK B', 'SPXS', 'PENN', 'NVDA', 'HUM', 'BITF', 'JPM', 'BP', 'ROKU', 'TSLA', 'JOBY', 'CZR', 'XP', 'LEVI', 'BIDU', 'SPX', 'WFC', 'SPCE', 'PACW', 'SOXS', 'EWG', 'JETS', 'BAC', 'AG', 'DWAC', 'UNH', 'DAL', 'FXI', 'HTZ', 'AGNC', 'PCG', 'CCJ', 'HYG', 'ZS', 'FFIE', 'NYCB', 'GILD', 'INVZ', 'MANU', 'MS', 'LEN', 'BTG', 'SHOP', 'CVX', 'IWM', 'DIA', 'XOM', 'COF', 'UUP', 'RTX', 'RIG', 'GS', 'AEM', 'BBIO', 'OPEN', 'COP', 'IEI', 'JMIA', 'TZA', 'USO', 'UVXY', 'VOD', 'ZION', 'WBD', 'ACB', 'KGC', 'OSTK', 'MELI', 'GE', 'BUD', 'CLSK', 'SBSW', 'EPD', 'MOS', 'SHEL', 'SU', 'MSOS', 'AI', 'XLP', 'TXN', 'XLK', 'VBIV', 'UVIX', 'ONON', 'SMCI', 'ON', 'BABA', 'ITB', 'MULN', 'LUMN', 'T', 'DVN', 'PSNY', 'CVS', 'GLD', 'ATVI', 'SPXU', 'TMUS', 'VXX', 'DASH', 'ABBV', 'CRM', 'PANW', 'DUK', 'ARKK', 'BOIL', 'AMAT', 'TTD', 'ABR', 'PFE', 'OXY', 'WMT', 'OKTA', 'RBLX', 'MU', 'ALLY', 'GOOGL', 'SOUN', 'UPST', 'QS', 'AVGO', 'XSP', 'GNRC', 'SQ', 'MQ', 'LYFT', 'AXP', 'HZNP', 'PLTR', 'WYNN', 'NFLX', 'XBI', 'QCOM', 'AA', 'F', 'NU', 'CARR', 'MSTR', 'TLRY', 'SPY', 'HBI', 'SNOW', 'NVAX', 'AAPL', 'JD', 'EQT', 'W', 'BX', 'FNGS', 'SOFI', 'SIMO', 'VIX', 'CGC', 'PYPL', 'XPEV', 'XLY', 'PATH', 'PACB', 'VZ', 'MMAT', 'DISH', 'CROX', 'WDC', 'TMF', 'EBAY', 'MO', 'CPNG', 'LI', 'ENVX', 'META', 'NOK', 'BVN', 'ETRN', 'V', 'MDT', 'TSLL', 'FCX', 'TSN', 'VALE', 'M', 'TELL', 'NET', 'GOOG', 'BB', 'USB', 'ET', 'BILI', 'HUT', 'TQQQ', 'FSR', 'DKNG', 'TGT', 'CAT', 'ADBE']

#         tickers = subs


#         # Now get option data concurrently
#         option_data_tasks = [
#             poly_options.get_option_data(ticker, await process_ticker(ticker, skews_outside_range)) for ticker in tickers
#         ]
#         results = await asyncio.gather(*option_data_tasks)
#         print(results)

#         # Filter out None results and add valid results to data_list
#         data_list = [result for result in results if result is not None]
#         data_list = sorted(data_list, key=lambda x: x[6], reverse=True)

#         # Create a new list that only includes the parts you want to display
#         display_data = [row[:7] for row in data_list]

#         # Now, display_data contains the data you want to display for all tickers.
#         # Format it into a table and send it in discord chat.
#         table = tabulate(display_data, headers=['Symbol', 'Skew', ' ', 'Price', 'Expiry', 'IV', 'Vol','Skew Metric'], tablefmt='fancy')

#         embed = disnake.Embed(
#             title=f"All - Skew",
#             description=f"```\n" + table + "\n```",
#             color=disnake.Colour.random()
#         )
#         embed.set_footer(text=f"{counter} | Data Provided by Polygon.io | Implemented by FUDSTOP")
#         await inter.edit_original_message(embed=embed)  # Send the table in a code block

#         if counter == 100:
#             await inter.send(f"> **Click to Run:**\n> </allskew:1121980575276879983>")
#             break

from cfg import konviction
@bot.slash_command()
async def full_skew(inter: disnake.AppCmdInter, ticker: str = commands.Param(autocomplete=ticker_autocomp)):
    """View skews for the next 60 days. PC Format with more columns."""
    MAX_CONCURRENCY = 60
    await inter.response.defer()
    ticker = ticker.upper()

    async def fetch_data(session, tickers):
        async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&apiKey={YOUR_API_KEY}") as response:
            try:
                near_money = await response.json(content_type=None)
                near_money_results = near_money['results']
                atm_data = UniversalSnapshot(near_money_results)
                return atm_data.df.sort_values('IV', ascending=True)
            except Exception as e:
                print(f"Error processing tickers: {tickers}. Error: {e}")
                return pd.DataFrame()

    async def process_option_data(grouped_df, session, sem):
        tasks = []
        for _, group in grouped_df:
            group_tickers = group['ticker'].tolist()
            if not group_tickers:
                continue
            tickers_string = ','.join(group_tickers)
            task = asyncio.create_task(fetch_data(session, tickers_string))
            tasks.append(task)

        results = []
        async with sem:
            for future in asyncio.as_completed(tasks):
                result = await future
                results.append(result)

        return results

    async with aiohttp.ClientSession() as session:
        sem = asyncio.Semaphore(MAX_CONCURRENCY)
        counter = 0
        counter = counter + 1
        price = await master.get_price(ticker)
        lower_strike = round(price) * 0.97
        upper_strike = round(price) * 1.03
        print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

        initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2027-12-31&limit=250&apiKey={YOUR_API_KEY}"
        results = await polygon._request_all_pages(initial_url)

        if results is not None:
            option_data = UniversalOptionSnapshot(results)
            calls = option_data.df[option_data.df['C/P'] == 'call']
            puts = option_data.df[option_data.df['C/P'] == 'put']

            calls_grouped = calls.groupby('exp')
            puts_grouped = puts.groupby('exp')

            calls_results = await process_option_data(calls_grouped, session, sem)
            calls_results_df = pd.concat(calls_results)
            calls_grouped = calls_results_df.groupby('Exp', as_index=False)

            puts_results = await process_option_data(puts_grouped, session, sem)
            puts_results_df = pd.concat(puts_results)
            puts_grouped = puts_results_df.groupby('Exp', as_index=False)

            calls_first_rows = calls_grouped.first()
            puts_first_rows = puts_grouped.first()

            calls_selected_columns_df = calls_first_rows[['Exp', 'IV', 'Skew', 'Price', 'Vol', 'OI']]
            puts_selected_columns_df = puts_first_rows[['Exp', 'IV', 'Skew', 'Price', 'Vol', 'OI']]
            calls_selected_columns_df['Exp'] = calls_selected_columns_df['Exp'].apply(lambda x: x[2:])
            puts_selected_columns_df['Exp'] = puts_selected_columns_df['Exp'].apply(lambda x: x[2:])
            calls_selected_columns_df['IV'] = (calls_selected_columns_df['IV'] * 100).round(4) if not TypeError else None
            puts_selected_columns_df['IV'] = (puts_selected_columns_df['IV'] * 100).round(4) if not TypeError else None
            calls_selected_columns_df = calls_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price', 'Vol', 'OI']]
            puts_selected_columns_df = puts_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price', 'Vol', 'OI']]

            calls_dfs = [calls_selected_columns_df[i:i+10] for i in range(0,len(calls_selected_columns_df),10)]
            puts_dfs = [puts_selected_columns_df[i:i+10] for i in range(0,len(puts_selected_columns_df),10)]
            print(calls_selected_columns_df)
            print(puts_selected_columns_df)
            call_table = tabulate(calls_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
            put_table = tabulate(puts_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
            embeds = []
            for call_df, put_df in zip(calls_dfs, puts_dfs):
                call_table = tabulate(call_df, headers='keys', tablefmt='fancy', showindex=False)
                put_table = tabulate(put_df, headers='keys', tablefmt='fancy', showindex=False)
                embed = disnake.Embed(title=f"Skews - {ticker} - Next 30 Days", color=disnake.Colour.random())
                embed.description = f"**CALLS:**```{call_table}```\n**PUTS:**```{put_table}```"
                embed.set_footer(text=f"Viewing Skews for {ticker}")
                embeds.append(embed)
            


            await inter.edit_original_message(view=AlertMenus(embeds), embed=embeds[0])

from sdks.polygon_sdk.list_sets import sublist2





@bot.slash_command()
async def skew_pc(inter: disnake.AppCmdInter, ticker: str = commands.Param(autocomplete=ticker_autocomp)):
    """View skews for the next 60 days. PC Format with more columns."""
    MAX_CONCURRENCY = 60
    await inter.response.defer()
    ticker = ticker.upper()

    async def fetch_data(session, tickers):
        async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&apiKey={YOUR_API_KEY}") as response:
            try:
                near_money = await response.json(content_type=None)
                near_money_results = near_money['results']
                atm_data = UniversalSnapshot(near_money_results)
                return atm_data.df.sort_values('IV', ascending=True)
            except Exception as e:
                print(f"Error processing tickers: {tickers}. Error: {e}")
                return pd.DataFrame()

    async def process_option_data(grouped_df, session, sem):
        tasks = []
        for _, group in grouped_df:
            group_tickers = group['ticker'].tolist()
            if not group_tickers:
                continue
            tickers_string = ','.join(group_tickers)
            task = asyncio.create_task(fetch_data(session, tickers_string))
            tasks.append(task)

        results = []
        async with sem:
            for future in asyncio.as_completed(tasks):
                result = await future
                results.append(result)

        return results

    async with aiohttp.ClientSession() as session:
        sem = asyncio.Semaphore(MAX_CONCURRENCY)
        counter = 0
        while True:
            counter = counter + 1
            if ticker.startswith("SPX"):
                price = await polygon.get_index_price(ticker)
                lower_strike = round(price) * 0.97
                upper_strike = round(price) * 1.03
            else:
                price = await polygon.get_stock_price(ticker)
                if price is not None:
                    lower_strike = round(price) * 0.85
                    upper_strike = round(price) * 1.15
                else:
                    price = 0
            print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

            initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2027-12-31&limit=250&apiKey={YOUR_API_KEY}"
            results = await polygon._request_all_pages(initial_url)

            if results is not None:
                option_data = UniversalOptionSnapshot(results)
                calls = option_data.df[option_data.df['type'] == 'call']
                puts = option_data.df[option_data.df['type'] == 'put']
                calls_grouped = calls.groupby('exp')
                puts_grouped = puts.groupby('exp')

                calls_results = await process_option_data(calls_grouped, session, sem)
                calls_results_df = pd.concat(calls_results)
                calls_grouped = calls_results_df.groupby('Exp', as_index=False)

                puts_results = await process_option_data(puts_grouped, session, sem)
                puts_results_df = pd.concat(puts_results)
                puts_grouped = puts_results_df.groupby('Exp', as_index=False)

                calls_first_rows = calls_grouped.first()
                puts_first_rows = puts_grouped.first()

                calls_selected_columns_df = calls_first_rows[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]
                puts_selected_columns_df = puts_first_rows[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]
                calls_selected_columns_df['Exp'] = calls_selected_columns_df['Exp'].apply(lambda x: x[5:])
                puts_selected_columns_df['Exp'] = puts_selected_columns_df['Exp'].apply(lambda x: x[5:])
                calls_selected_columns_df['IV'] = (calls_selected_columns_df['IV'] * 100).round(4)
                puts_selected_columns_df['IV'] = (puts_selected_columns_df['IV'] * 100).round(4)
                calls_selected_columns_df = calls_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]
                puts_selected_columns_df = puts_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]

                print(calls_selected_columns_df)
                print(puts_selected_columns_df)
                call_table = tabulate(calls_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                put_table = tabulate(puts_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                embed = disnake.Embed(title=f"Skews - {ticker} - Next 30 Days", description=f"**CALLS:**```{call_table}```\n**PUTS:**```{put_table}```", color=disnake.Colour.random())
                embed.set_footer(text=f"Viewing Skews for {ticker}")
            
                dEmbed = DiscordEmbed(title=f"Skews - {ticker} - Long Outlook", color=hex_colors['yellow'])
                dEmbed.description = f"**CALLS:**```{call_table}```\n**PUTS:**```{put_table}```"
                dEmbed.set_timestamp()
                dEmbed.set_footer(text=f"{ticker} | Implemented by FUDSTOP")
     
                print(f"Sent to konviction.")
                await inter.edit_original_message(embed=embed)
                if counter == 50:
                    await inter.send("stream ended")
                    break
def get_date_string(number_of_days) -> str:
    date = datetime.now() - timedelta(days=number_of_days)
    return date.strftime('%Y-%m-%d')
from datetime import datetime, timedelta
@bot.slash_command()
async def calls_and_puts(inter: disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
    """Returns the total amount of calls and put OI and Volume for the next 30 days for a ticker"""
    await inter.response.defer()

    data = await polygon.all_options(ticker=ticker, expiration_date=thirty_days_from_now_str)

    symbols = data.option_symbol
    put_symbols = []
    call_symbols = []

    for symbol in symbols:
        if 'C0' in symbol:
            call_symbols.append(symbol)
        elif 'P0' in symbol:
            put_symbols.append(symbol)

    total_put_volume = 0
    total_call_volume = 0
    total_put_oi = 0
    total_call_oi = 0

    # Getting volumes for call symbols in chunks
    call_chunks = chunked(call_symbols, 250)
    for call_chunk in call_chunks:
        volume_tasks = [poly_options.get_option_volume(symbol) for symbol in call_chunk]
        oi_tasks = [poly_options.get_option_oi(symbol) for symbol in call_chunk]
        call_volumes_chunk = await asyncio.gather(*volume_tasks)
        call_ois_chunk = await asyncio.gather(*oi_tasks)
        total_call_volume += sum(filter(None, call_volumes_chunk))  # sum up volumes, ignoring None values
        total_call_oi += sum(filter(None, call_ois_chunk))  # sum up ois, ignoring None values

    # Getting volumes for put symbols in chunks
    put_chunks = chunked(put_symbols, 250)
    for put_chunk in put_chunks:
        volume_tasks = [poly_options.get_option_volume(symbol) for symbol in put_chunk]
        oi_tasks = [poly_options.get_option_oi(symbol) for symbol in put_chunk]
        put_volumes_chunk = await asyncio.gather(*volume_tasks)
        put_ois_chunk = await asyncio.gather(*oi_tasks)
        total_put_volume += sum(filter(None, put_volumes_chunk))  # sum up volumes, ignoring None values
        total_put_oi += sum(filter(None, put_ois_chunk))  # sum up ois, ignoring None values

    if total_call_oi > total_put_oi:
        color = disnake.Colour.dark_green()
    else:
        color = disnake.Colour.dark_red()


    embed = disnake.Embed(title=f"Calls and Puts - {ticker} - 30 Days Out", description=f"```py\nDisplaying total calls and puts for the next 30 days {ticker}.```", color=color)
    embed.add_field(name=f"Volume:", value=f"> Calls: **{float(total_call_volume):,}**\n> Puts: **{float(total_put_volume):,}**")
    embed.add_field(name=f"Open Interest:", value=f"> Calls: **{float(total_call_oi):,}**\n> Puts: **{float(total_put_oi):,}**")
    embed.set_thumbnail(await polygon.get_polygon_logo(ticker))
    dEmbed = DiscordEmbed(title=f"Calls and Puts - {ticker} - 30 Days Out", description=f"```py\nDisplaying total calls and puts for the next 30 days {ticker}.```", color=hex_colors['yellow'])
    dEmbed.add_embed_field(name=f"Volume:", value=f"> Calls: **{float(total_call_volume):,}**\n> Puts: **{float(total_put_volume):,}**")
    dEmbed.add_embed_field(name=f"Open Interest:", value=f"> Calls: **{float(total_call_oi):,}**\n> Puts: **{float(total_put_oi):,}**")
    dEmbed.set_thumbnail(await polygon.get_polygon_logo(ticker))
    dEmbed.set_timestamp()
    dEmbed.set_footer(text=f"{ticker} | Implemented by FUDSTOP")

    print(f"Sent to konviction.")
    await inter.edit_original_message(embed=embed)

    print(f"{ticker} CALL VOLUME: {total_call_volume}")
    print(f"{ticker} PUT VOLUME: {total_put_volume}")
    print(f"{ticker} CALL OI: {total_call_volume}")
    print(f"{ticker} PUT OI: {total_put_volume}")


class ResponseSelect(disnake.ui.Select):
    def __init__(self, bot, ticker, options):
        self.bot = bot
        self.ticker = ticker
        super().__init__(
            placeholder="Select a function",
            min_values=1,
            max_values=5,  # allow multiple selections
            options=options
        )

    async def callback(self, interaction: disnake.Interaction):
        selected_options = self.values
        results = []
        conversation_id = str(interaction.user.id)
        history = self.bot.conversation_history.get(conversation_id, [])

        for option in selected_options:
            function = self.bot.function_map.get(option)
            
            if function:
                # Perform the function call
                function_call = await function(self.ticker)
                
                # Process the function response
                if isinstance(function_call, pd.DataFrame):
                    function_response = function_call.to_string()
                elif isinstance(function_call, dict) and "function_response" in function_call:
                    function_response = function_call["function_response"]
                else:
                    function_response = str(function_call)
                
                results.append(function_response)

        response = "\n".join(results)
        
        # Add the DataFrame string to the prompt for the function call
        prompt = f"{self.ticker} {response}"
        
        # Call the function
        view = FuncCall(prompt, self.bot)

        # Send the prompt to GPT-3.5-turbo
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=history + [{"role": "user", "content": prompt}],
            function_call="auto",
        )

        # Process the response from GPT-3.5-turbo and update the conversation history
        message = completion.choices[0].message
        history.append(message)
        self.bot.conversation_history[conversation_id] = history

        if "function_response" in message:
            # Function response received, send it to the user
            embed = disnake.Embed(title="Function Response", description=message["function_response"])
            await interaction.response.send_message(embed=embed)
        else:
            # No function response, continue the conversation as usual
            embed = disnake.Embed(title="GPT4", description=message["content"])
            await interaction.response.edit_message(embed=embed)




@bot.command()
async def gpt4(ctx: commands.Context, prompt: str):
    """Talk with GPT4 using CHATGPT. Call the command once and then reply as normal."""
    messages = [
        {"role": "user", "content": f"Use all of the data and come up with a solution. Pay close attention to the option IV versus the current price. You have the nearest option symbols to the money along with all corresponding data to make these determinations."}
    ]
    conversation_id = str(ctx.author.id)

    # Store the initial prompt in the conversation history
    conversation_history = {
        conversation_id: [{"role": "user", "content": prompt}]
    }

    # Create a list of options for the response dropdown
    response_options = [
        disnake.SelectOption(label=f"Response {i+1}", value=str(i+1), description=f"#snippet of response {i+1}", emoji=f"<a:_:1043272438378672248>")
        for i in range(3)  # Modify this number to add more response options if needed
    ]

    # Create the dropdown for response selection
    view = disnake.ui.View()
    view.add_item(ResponseSelect(prompt, bot, options=response_options))

    # Send the initial response and the response selection dropdown to the user
    initial_response = await bot.get_gpt3_response(messages)
    embed = disnake.Embed(title="Chat with GPT4", description=f"> {initial_response}")
    await ctx.send(embed=embed, view=view)



@bot.command()
async def all(ctx: commands.Context, ticker):
    datamaster = DataMaster(ticker=ticker)
    logo = await polygon.get_polygon_logo(ticker)
    data = await datamaster.create(ticker)

    data_chunks = [data.df.transpose()[i:i+20] for i in range(0, len(data.df.transpose()), 20)]
    
    for chunk in data_chunks:

        embed = disnake.Embed(title=f"All", description=f"```{chunk}```")
        embed.set_thumbnail(logo)
        await ctx.send(embed=embed)

    
# @bot.command()
# async def gpt4(ctx: commands.Context, prompt: str):
#     """Talk with CHATGPT. Call the command once and then reply as normal."""
#     messages = [
#         {"role": "user", "content": f"Use all of the data and come up with a solution. Pay close attention to the option IV versus the current price. You have the nearest option symbols to the money along with all corresponding data to make these determinations."}
#     ]
#     conversation_history = {}
#     conversation_id = str(ctx.author.id)
#     prompt = prompt
#     # Retrieve the conversation history from the dictionary
#     history = conversation_history.get(conversation_id, [])

#     while True:
#         # Add the new prompt to the conversation history
#         history.append({"role": "user", "content": prompt})

#         # Create the messages list including system message and conversation history
#         messages = [
#             {"role": "system", "content": "Hello! You have two main purposes: Purpose 1: You are an all helpful bot! Purpose 2: Whenever the phrase 'start project!' is said by the user - you must kick in to project mode and follow the subsequent instructions. You will be given one line of code at a time. You will listen to the user, and help them with their project. DO NOT OVER-EXPLAIN THINGS. They do not need you to explain anything. In fact - only explain something if specifically asked. You are a master python coder. You're working exclusively with stock market data - and have access to every data metric and the user who you are helping has a deep understanding of the financial market data. Provide the most efficient code possible for the purpose of a real-time discord-integrated market system."},
#             {"role": "assistant", "content": "Absolutely! I'll be glad to help, and will listen for the phrase 'start project!' at which point I will follow all instructions given."},
#         ]
#         messages.extend(history)

#         # Generate a response based on the full conversation history
#         completion = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo-16k",
#             messages=messages
#         )

#         message_content = completion.choices[0].message.content

#         # Store the updated conversation history in the dictionary
#         conversation_history[conversation_id] = history

#         embed = disnake.Embed(title="Chat with GPT4", description=f"> {message_content}")


#         # Send the response to the user
#         await ctx.send(embed=embed)
#         print(message_content)
#         # Check if the user wants to stop the conversation
#         if prompt.lower() == "stop":
#             await ctx.send("Conversation ended.")
#             break

#         # Wait for the user's next message
#         def check(m):
#             return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

#         try:
#             user_message = await bot.wait_for("message", check=check, timeout=60)
#         except asyncio.TimeoutError:
#             await ctx.send("Conversation timed out. Please start a new conversation.")
#             break

#         prompt = user_message.content


async def balance_sheet_dataframe(ticker):
    
    balance_sheet= await webull.get_balancesheet(ticker)
    balance_sheet_df = balance_sheet.df
    print(balance_sheet_df)

    return balance_sheet_df


async def financial_statement_dataframe(ticker):

    financial_statement = await webull.get_financial_statement(ticker)

    financial_statement_df = financial_statement.df
    return financial_statement_df


conversation_history = {}  # Create an empty dictionary to store conversation history
from cfg import YOUR_OPENAI_KEY


@bot.command()
async def data(ctx: commands.Context):
    _data = await poly.get_aggregates(ticker="SPY",multiplier=1,timespan="hour", from_date="2023-01-01", to_date="2023-07-25",limit=1000)
    df=_data.df.transpose().head(10)
    table = tabulate(df, headers='keys', tablefmt='fancy', showindex=False)
    await ctx.send(f"```{df}```")



@bot.slash_command()
async def function_call(inter: disnake.MessageCommandInteraction, ticker: str = None):
    await inter.response.defer()
    openai.api_key = YOUR_OPENAI_KEY  # replace with your OpenAI key
    conversation_history = {}
    conversation_id = str(inter.author.id)

    # Retrieve the conversation history from the dictionary
    history = conversation_history.get(conversation_id, [])

    # Initialize GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=history + [{"role": "user", "content": ticker}],
        functions=fc_stock_functions,
        function_call="auto",
    )
    message = response["choices"][0]["message"]

    # Update the conversation history
    history.append(message)
    conversation_history[conversation_id] = history

    if ticker and message.get("function_call"):
        # Call the function
        view = FuncCall(ticker, bot)


        # Send model the info on the function call and function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k", 
            max_tokens=12000,
            messages=[
                {"role": "system", "content": f"Waiting for functions to be called."},

            
                    
                
            ],
        )
        second_message = second_response.choices[0].message['content']
        message_chunks = [second_message[i:i + 3000] for i in range(0, len(second_message), 3000)]

        for chunk in message_chunks:
            embed = disnake.Embed(title=f"GPT-4 FUNCTION CALL", description=f"```py\n{chunk}```")
            await inter.edit_original_message(embed=embed, view=view)
    

        def check2(m):
            return m.author.id == inter.author.id and m.channel.id == inter.channel.id

        try:
            user_message = await bot.wait_for("message", check=check2, timeout=60)
        except asyncio.TimeoutError:
            await inter.channel.send("Conversation timed out. Please start a new conversation.")
            return
        prompt = user_message.content
    else:
        message_content = response.choices[0].message.content
        embed = disnake.Embed(title=f"GPT4", description=f"```py\n{message_content}```")
        await inter.edit_original_message(embed=embed, view=view)


import requests



@bot.command()
async def show_chain(ctx: commands.Context, ticker):
    x = await master.get_near_the_money_single(ticker, 3)
    print(x)
    data = await master.show_the_chain(atm_options= x)
    selected_columns = data[["Open","High", "Close", "Strike", "IV", "Vol", "OI", "Exp"]]
    print(selected_columns)
    embed = disnake.Embed(title=f"ATM Option Snapshot:", description=f"```{selected_columns}```")
    await ctx.send(embed=embed)


@bot.slash_command()
async def at_the_money_trades(inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
    """Get the atm TRADES for a ticker"""
    await inter.response.defer()

  
    x = await master.get_near_the_money_single(ticker, 5)
    print(x)
    df= await master.atm_trades(atm_options= x)

    x = x.split(',')
    dfs = []  # to store all the dataframes
    for option in x:
        agg_objs = await master.get_aggregates(option)
        agg_data = [obj.to_dict() for obj in agg_objs]  # convert each OptionAggs object to a dict
        df = pd.DataFrame(agg_data).head(2)  # get the first two rows
        df['option_symbol'] = human_readable(option)  # add option symbol to the dataframe
        dfs.append(df)

    # Concatenate all the dataframes and convert the result into a tabulate table
    final_df = pd.concat(dfs, ignore_index=True)

    # Keep only 'timestamp', 'high', 'low', 'close', 'volume', 'option_symbol' columns
    final_df = final_df[['high', 'low', 'close', 'volume', 'option_symbol']].sort_values('volume', ascending=False)



    table = tabulate(final_df, headers='keys', tablefmt='fancy', showindex=False)

    embed = disnake.Embed(title=f"ATM Trades", description=f"```{table}```")

    await inter.edit_original_message(embed=embed)


@bot.slash_command()
async def test(inter: disnake.AppCommandInter, command:str=commands.Param(autocomplete=command_autocomp)):

    if command == "all_options":
        await inter.send(f"> **Click to Run:**\n> </all_options:1122312195154387024>")
    elif command == "learn discord":
        await learn_cmds.discord(inter)
    elif command == "learn_order_types":
        await learn_cmds.order_types(inter)
    elif command == "learn_core_logic":
        await learn_cmds.core_logic(inter)
    elif command == "learn_filings":
        await learn_cmds.filings(inter)
    elif command == "learn_cmds.calls":
        await learn_cmds.calls(inter)
    elif command == "learn_etfs":
        await learn_cmds.etfs(inter)
    elif command == "learn_greeks":
        await learn_cmds.greeks(inter)
    elif command == "learn_china":
        await learn_cmds.china(inter)
    elif command == "learn_options_101":
        await learn_cmds.options_101(inter)
    elif command == "learn_option_strategies":
        await learn_cmds.option_strategies(inter)
    elif command == "learn_core_logic":
        await learn_cmds.core_logic(inter)
    elif command == "learn_covered_calls":
        await learn_cmds.covered_calls(inter)
    elif command == "learn_nsfr_ratio":
        await learn_cmds.nsfr_ratio(inter)
    elif command == "learn_candle_patterns":
        await learn_cmds.candle_patterns(inter)
    elif command == "learn_occ":
        await learn_cmds.occ(inter)
    elif command == "learn_criteria":
        await learn_cmds.criteria(inter)
    elif command == "learn_ta":
        await learn_cmds.ta(inter)
    elif command == "learn_finra":
         await learn_cmds.finra(inter)      

    elif command == "analysis_gaps_up":
        await inter.send(f"**Click to Run:**\n> </analysis gaps_up:1122243463723876533>")
    
    elif command == "analysis_gaps_down":
        await inter.send(f"**Click to Run:**\n> </analysis gaps_down:1122243463723876533>")
    


    elif command == "analysis_overbought_gap":
        
        await inter.send(f"**Click to Run:**\n> </analysis overbought_gap:1122243463723876533>")

    elif command == "analysis_topshorts":
        await analysis_cmds.topshorts(inter)


    elif command == "rsi":
        await inter.send(f"> **Click to Run:**\n> </ta rsi_snapshot:1122650723021238362>")


      

    elif command == "company_information":
        await inter.send(f"> **Click to Run:**\n> </poly company_info:1122243463862300754")



    elif command == "earnings_calendar":
        await ss_cmds.earnings(inter)

    elif command == "insider_trading_market_wide":
        await ss_cmds.insider_summary(inter)


    elif command == "daily_treasury_balance":
        await ss_cmds.treasury(inter)

    elif command == "inflation":
        await ss_cmds.inflation(inter)

    elif command == "jobless_claims":
        await ss_cmds.jobless_claims(inter)

    elif command == "market_news":
        await ss_cmds.market_news(inter)

    elif command == "short_volume":
        await inter.send(f"> **Click to run:**\n> </ss short_volume:1122243463862300759>")


    elif command == "reverse_repo":
        await ss_cmds.reverse_repo(inter)




    elif command =="low_floats":
        await ss_cmds.low_floats(inter)


    elif command == "short_interest":

        await ss_cmds.short_interest(inter)



    elif command == "news_sentiment":
        await inter.send(f"> **Click to Run:**\n> </ss news_sentiment:1122243463862300759>")



    elif command == "sec_filings":
        await inter.send(f"> **Click to Run:**\n> </ss sec_filings:1122243463723876533>")

        

    elif command == "short_interest":
        await ss_cmds.short_interest(inter)


    elif command == "price_target":
        await inter.send(f"> **Click to Run:**\n> </fmp price_target:1122711896773103698>")
    elif command == "subreddits":
        await inter.send(f"> **Click to Run:**\n> </ss subreddits:1122243463862300759>")
async def get_option_calls(ticker):
    url = f"https://api.polygon.io/v3/reference/options/contracts?underlying_ticker={ticker}&limit=1000&apiKey={YOUR_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url):
            results = await polygon._request_all_pages(url)
            if results is not None:
                data = CallsOrPuts(results, ticker)
                print(data.df)
                return data.df

# Global dictionary to store user's tickers


@bot.slash_command()
async def get_gap_chart(inter: disnake.AppCmdInter, ticker:str,multiplier:str,timespan:str=commands.Param(choices=['minute','hour','day','week','month','quarter','year']),):
    await inter.response.defer()
    aggs = await mastery.get_aggs(ticker, multiplier, timespan, thirty_days_ago_str, today_str)
    if aggs:  
        gaps = await mastery.find_gaps(aggs)
        # Assuming `gaps` is your list of gaps
        table_str = await mastery.gaps_to_table(gaps)

        # Now you can print the table or use it however you want
        print(table_str)
        await mastery.chart_gaps(aggs, gaps)
        file = File('chart.png', filename='chart.png')
        embed = Embed(title=f"Test Chart - Gaps", description=f"This chart is showing you the gaps from {ticker} on the {timespan} timeframe.\n\n```{table_str}```", color=0xFFD700)
        embed.set_image(url="attachment://chart.png")
        await inter.send(embed=embed, file=file)

    else:
        await inter.edit_original_message("No data returned from get_aggs().")



@bot.slash_command()
async def allskew(inter:disnake.AppCmdInter):
    """Scans and returns all skews with a depth of 5 or more, or -5 or less."""
    await inter.response.defer()
    async def process_ticker(ticker, skews_outside_range):
        x = await master.get_near_the_money_single(ticker, exp_greater_than=today_str, exp_less_than=seven_days_from_now_str)
        try:
            skew = await master.find_skew(x)
    
            if 'Close' not in skew.columns or 'Skew' not in skew.columns:
                print('Close or Skew not found in columns')
                return

            skew['depth'] = skew['Strike'] - skew['Price']
            
            mask = (skew['depth'] < -5.0) | (skew['depth'] > 5.0)
            selected_columns = skew[mask][['Sym', 'Price', 'Skew', 'Exp', 'depth', 'IV', 'OI']]
            selected_columns['Exp'] = selected_columns['Exp'].str[5:]
            selected_columns['IV'] = (selected_columns['IV'] * 100).round(5)
            selected_columns['Direction'] = np.where(selected_columns['Price'] > selected_columns['Skew'], '🔥', '🟢')
            skews_outside_range.extend(selected_columns.to_dict('records'))
            
        except AttributeError:
            return
    counter = 0

    
    while True:
        counter = counter  + 1


        tickers = list(set(sublist1))

        tasks = []
        skews_outside_range = []

        for ticker in tickers:
            
            tasks.append(process_ticker(ticker, skews_outside_range))

        await asyncio.gather(*tasks)

        sorted_skews = sorted(skews_outside_range, key=lambda x: x['depth'])
    
  
        table = tabulate(sorted_skews, headers='keys', tablefmt='fancy', showindex=False)
        df = pd.DataFrame(sorted_skews)
        df.to_csv('sorted_skews.csv')

        embed = disnake.Embed(title=f"{emojis.leftarrow} SKEW-DE-BOP-BOX {emojis.rightarrow}", description=f"```{table}```", color=disnake.Colour.random())
        view = disnake.ui.View()
        await inter.edit_original_message(embed=embed, view=view)
        if counter == 150:
            await inter.send(f"> </skew allskew:1124756467724066824>")
            break          


@bot.command()
async def company(ctx: commands.Context, ticker:str):
    """Provides comapny information"""
    await ctx.send(f"> One Moment while I look-up the data...", delete_after=3)
    get = await DataAnalyzer.company_data(ticker)
    # Here's the correction. We instantiate a DataAnalyzer instance first
    analyzer = DataAnalyzer(get)
    response = analyzer.analyze(f"Analyze this company information: {get}")
    embed = disnake.Embed(title=f"Company Information - {ticker}", description=f"```py\n{response}```", color=disnake.Colour.dark_blue())
    embed.set_thumbnail(await polygon.get_polygon_logo(ticker))
    embed.set_footer(icon_url=await polygon.get_polygon_logo(ticker),text=f"{ticker} - | Data Provided by Polygon.io")
    await ctx.send(embed=embed)


@bot.command()
async def anal(ctx: commands.Context, ticker:str):
    """Provides comapny information"""
    get = await DataAnalyzer.volume_analysis(ticker)
    # Here's the correction. We instantiate a DataAnalyzer instance first
    analyzer = DataAnalyzer(get)
    response = analyzer.analyze(f"Analyze today's volume analysis for {ticker}: {get}")
    embed = disnake.Embed(title=f"Volume Analysis - {ticker}", description=f"```py\n{response}```", color=disnake.Colour.dark_gold())
    embed.set_thumbnail(await polygon.get_polygon_logo(ticker))
    embed.set_footer(icon_url=await polygon.get_polygon_logo(ticker),text=f"{ticker} - | Data Provided by Polygon.io")
    await ctx.send(embed=embed)


@bot.command()
async def rsi(ctx: commands.Context, ticker:str):
    """Provides an RSI snapshot across all timeframes."""

    get = await DataAnalyzer.rsi_snapshot(ticker)
    # Here's the correction. We instantiate a DataAnalyzer instance first
    analyzer = DataAnalyzer(get)
    response = analyzer.analyze(f"Analyze the RSI over all timespans for {ticker}. Provide cool emojis and insights for what the data portrays. An rsi of 30  or below = bullish. 70+ = bearish. The closer to 30 = more bullish .. the closer to 70 = more bearish.. 40-60 is neutral: {get}")
    embed = disnake.Embed(title=f"RSI Snapshot - {ticker}", description=f"```py\n{response}```", color=disnake.Colour.dark_gold())
    embed.set_thumbnail(await polygon.get_polygon_logo(ticker))
    embed.set_footer(icon_url=await polygon.get_polygon_logo(ticker),text=f"{ticker} - | Data Provided by Polygon.io")
    await ctx.send(embed=embed)





@bot.command()
async def summary(ctx: commands.Context, ticker:str):
    """Provides comapny information"""
    get = await DataAnalyzer.rsi_snapshot(ticker)
    GET = await DataAnalyzer.macd_snapshot(ticker)
    vol = await DataAnalyzer.volume_analysis(ticker)

    cost_dist = await webull.cost_distribution(ticker)

    

    # Here's the correction. We instantiate a DataAnalyzer instance first
    analyzer = DataAnalyzer(get)
    response = analyzer.analyze(f"Analyze the RSI over all timespans for {ticker}. Provide cool emojis and insights for what the data portrays. An rsi of 30  or below = bullish. 70+ = bearish. The closer to 30 = more bullish .. the closer to 70 = more bearish.. 40-60 is neutral: {get}. Also - check the results of the MACD data for each timespan - provide emojis as well: {GET}\nAlso - give a brief summary of the volume analysis data: {vol}. Also - check the cost distribution and give some insight.Make summaries VERY BRIEF not to exceed a total of 4096 characters.")
    response2 = analyzer.analyze(f'Heres the cost distribution data: This is a list of the percent of players profiting: {cost_dist.closeProfitRatio[:10]}. Scan it over and be very brief with the output.' )

    embed = disnake.Embed(title=f"RSI Snapshot - {ticker}", description=f"```py\n{response}```", color=disnake.Colour.dark_gold())
    embed.add_field(name=f"Cost Distribution:", value=f"```{response2}```")
    embed.set_thumbnail(await polygon.get_polygon_logo(ticker))
    embed.set_footer(icon_url=await polygon.get_polygon_logo(ticker),text=f"{ticker} - | Data Provided by Polygon.io")
    await ctx.send(embed=embed)

class ServerMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel",placeholder="Select A Channel!",min_values=1,max_values=1,channel_types=[disnake.ChannelType.forum])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            embed = disnake.Embed(title=f"{emojis.ls}{emojis.le}{emojis.lr}{emojis.lv}{emojis.le}{emojis.lr}🌟{emojis.lm}{emojis.le}{emojis.ln}{emojis.lu}")
            
            await interaction.send(f"The selected channel is: {selected_channel.mention}", ephemeral=False)
        else:
            await interaction.send("No channel was selected!", ephemeral=False)


class ServerMenuView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ServerMenu())
        self.add_item(TextMenu())
        self.add_item(ThreadMenu())

class ServerMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel2", placeholder="Select or Search for a Forum Channel!", min_values=1, max_values=1, channel_types=[disnake.ChannelType.forum])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            await interaction.send(f"The selected channel is: {selected_channel.mention}", delete_after=10)
        else:
            await interaction.send("No channel was selected!", delete_after=10)


class TextMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel3", placeholder="Select or Search for a Text Channel!", min_values=1, max_values=1, channel_types=[disnake.ChannelType.text])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            await interaction.send(f"The selected channel is: {selected_channel.mention}", delete_after=10)
        else:
            await interaction.send("No channel was selected!", ephemeral=False)


class ThreadMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel4", placeholder="Select or Search for a Thread!", min_values=1, max_values=1, channel_types=[disnake.ChannelType.public_thread])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            await interaction.send(f"The selected channel is: {selected_channel.mention}", delete_after=10)
        else:
            await interaction.send("No channel was selected!", ephemeral=False)



@bot.slash_command()
async def iv(inter:disnake.AppCmdInter):
    await inter.response.defer()
    while True:
        url=f"https://api.polygon.io/v3/snapshot?ticker.any_of=O:SPY250321C00380000&apiKey={YOUR_API_KEY}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                r = await resp.json()
                results = r['results']
                iv = results[0]['implied_volatility']
                print(iv)
                await inter.edit_original_message(f"> IV: **{iv}**")
@bot.slash_command()
async def data(inter:disnake.AppCmdInter, ticker: str):
    """Launch the terminal."""
    ticker = ticker.upper()
    logo = await polygon.get_polygon_logo(ticker)
    view = MainView(bot, ticker)
    totals = await fudstop_.option_market_totals()

    f2high=float(totals.fiftytwohigh)
    f2low=float(totals.fiftytwolow)
    futures=float(totals.futures_vol)
    mdaily=float(totals.monthlydailyavg)
    optvol=float(totals.optionsVol)
    ydaily=float(totals.yearlydailyavg)

    embed = disnake.Embed(title=f"{emojis.redline} Data Ready {emojis.redline}", description=f"```py\nWelcome. Before you look at {ticker}'s data - here are the total option stats on the day:```", color=disnake.Colour.old_blurple())
    embed.add_field(name=f"Today's Volume Summary:", value=f"> {emojis.alert} Futures: **{futures:,}**\n> {emojis.redline} 52w High: **{f2high:,}**\n\n> {emojis.webullcmd} Today: **{optvol:,}**\n\n> {emojis.redline} 52w Low: **{f2low:,}**")
    embed.add_field(name=f"Averages:", value=f"> Monthly-Daily: **{mdaily:,}**\n> Yearly-Dayly: **{ydaily:,}**", inline=False)
    embed.set_thumbnail(logo)
    embed.set_footer(text=f"Viewing data for {ticker} | Data Provided by Polygon.io -")


    await inter.send(view=view, embed=embed)


@bot.command()
async def top_oi(ctx: commands.Context, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
    """Fetches the top open interest and volume across all expirations."""
    data = await poly_options.get_option_chain_all(ticker)
    dataframe = data.df
    list_of_dfs = await poly_options.organize_by_expiration(dataframe)
    all_rows = []
    for df in list_of_dfs:
        call_df, put_df = await poly_options.separate_calls_puts(df)
        top_call = await poly_options.get_top_open_interest(call_df)
        top_put = await poly_options.get_top_open_interest(put_df)
        top_call['exp'] = datetime.strptime(top_call['exp'], '%Y-%m-%d').strftime('%m-%d-%y')
        top_put['exp'] = datetime.strptime(top_put['exp'], '%Y-%m-%d').strftime('%m-%d-%y')
        top_call['C/P'] = top_call['C/P'].replace('call', 'C')
        top_put['C/P'] = top_put['C/P'].replace('put', 'P')
        all_rows.append(top_call[['C/P', 'strike', 'vol', 'OI', 'exp']].to_frame().T.reset_index(drop=True))
        all_rows.append(top_put[['C/P', 'strike', 'vol', 'OI', 'exp']].to_frame().T.reset_index(drop=True))
        divider = pd.DataFrame([['➖'] * 5], columns=['C/P', 'strike', 'vol', 'OI', 'exp'])
        all_rows.append(divider)
    
    price = await master.get_price(ticker)
    final_df = pd.concat(all_rows, axis=0, ignore_index=True)
    final_table = tabulate(final_df, headers='keys', tablefmt='fancy', showindex=False)
    embed = disnake.Embed(title=f"Top OI - All Exp. {ticker}", description=f"```{final_table}```", color=disnake.Colour.dark_orange())
    embed.add_field(name=f"{ticker}'s Price:", value=f"> **${price}**")
    embed.add_field(name=f"{ticker}", value=f"```py\nViewing top OI/VOL for calls and puts across all expirations for {ticker}.```", inline=False)
    embed.set_footer(text=f"{ticker}", icon_url=await poly.get_polygon_logo(ticker))
    print(len(embed.description))
    await ctx.send(embed=embed)




@bot.slash_command()
async def cmds(ctx: disnake.AppCommandInter):
    """Views the server commands from all bots."""
    # Create a list of embeds
    embeds = [
        disnake.Embed(title=f"FUDSTOP Commands - Webull", description=f"```py\nYou are viewing fudstop commands regarding webull. Learn how to use the Webull App, customize it, and view several graphics such as TA, Trend Analysis, Candlestick analysis, and general market knowledge.```\n> The webull commands can be accessed by using:\n\n> **/webull**"),
        disnake.Embed(title=f"FUDSTOP Commands - Stocksera", description=f"```py\nYou are viewing the fudstop implemented commands from the Stocksera API. View economic data, FTDs, low floats, short interest, short volume, social media chatter and more.```\n> The Stocksera commands can be access by using:\n\n> **/ss**"),
        disnake.Embed(title=f"FUDSTOP Commands - Analysis", description=f"```py\nYou are viewing FUDSTOP Implemented commands from finviz. Analyze technicals and patterns with the analysis commands.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Learn", description=f"```py\nYou are viewing FUDSTOP Learn commands which has a multitude of information from webull guides to SEC Filings, and videos from my channel.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Agencies", description=f"```py\nYou are viewing FUDSTOP implemented commands from the Federal Reserve of New York's API, the Options Clearing Corporation API, and the Office of Financial Research API. View economic data, repo data, and others straight from the source.```"),
        disnake.Embed(title=f"FUDSTOP Commands - School", description=f"```py\nYou are viewing FUDSTOP school commands which aim to help educate the viewer by providing an interactive application where you can select the content via buttons.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Options", description=f"```py\nYou are viewing the FUDSTOP Implemented options commands from polygon.io. This is being actively revamped. Stay tuned!```"),
        disnake.Embed(title=f"FUDSTOP Commands - FMP", description=f"```py\n Viewing commands from the Financial Modeling Prep API. Will be actively building this section which will contain many areas of data analytics.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Other", description=f"```py\n Skews, bananas, GPT4, and other FUDSTOP-originated commands can be found here.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Stream", description=f"```py\n Viewing commands that stream live data - from stock and crypto prices to live options volume. (coming soon).```"),
        disnake.Embed(title=f"FUDSTOP Commands - Stock", description=f"```py\n Viewing commands that stream live data - from stock and crypto prices to live options volume. (coming soon).```"),
        disnake.Embed(title=f"FUDSTOP Commands - Navigation", description=f"```py\n Easily navigate throughout the server by utilizing the navigation commands. You can search threads, forums, or channels.```"),
        disnake.Embed(title=f"Open BB - Charting", description=f"```py\nView these commands from OpenBB that allow you to chart right from discord.```"),
        disnake.Embed(title=f"Open BB - Economy", description=f"```py\nView these commands for getting economic data from Open BB.```"),
        disnake.Embed(title=f"Open BB - Due Diligence", description=f"```py\nView these commands for getting earnings info, split, company financials, company bio, and more.```"),
        disnake.Embed(title=f"Open BB - Dark Pools", description=f"```py\nView these commands to call data related to dark pools.```"),
        disnake.Embed(title=f"Open BB - Flow", description=f"```py\nView commands relating to money flow, premium, options summaries - and more.```"),
        disnake.Embed(title=f"Open BB - Options", description=f"```py\nView these commands to chart open interest, volume, view option stats, option history, volatiltiy, and more.```")
    ]

    # Add fields to a specific embed (e.g., the second embed at index 1)
    fudstop_webull = 0
    fudstop_stocksera = 1
    fudstop_analysis = 2
    fudstop_learn = 3
    fudstop_agencies = 4
    fudstop_school = 5
    fudstop_opts = 6
    
    fudstop_fmp = 7
    fudstop_other = 8
    fudstop_stream = 9
    fudstop_stock = 10
    fudstop_nav = 11
    openbb_charting = 12
    openbb_economy = 13
    openbb_dd = 14
    openbb_dp = 15
    openbb_flow = 16
    openbb_op = 17

    webull_commands = embeds[fudstop_webull]
    webull_commands.add_field(name="Analysis Tools", value="> View webull tools pertaining to how to utilize data analysis tools.\n> Click to use:\n\n</webull analysis_tools:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Bid/Ask Spread", value="> Learn about the bid ask spread.\n> Click to use:\n\n</webull bid_ask_spread:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Graphics", value="> View several webull graphics such as TA, Chart Patterns, and more.\n> Click to use:\n\n</webull graphics:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Options Chain", value="> Learn about the Webull Option Chain and how to use it.\n> Click to use:\n\n</webull options_chain:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Options Setup", value="> Learn how to cutsomize your webull options chart.\n> Click to use:\n\n> </webull options_setup:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Orders", value="> Learn about the different market order types.\n> Click to use:\n\n</webull orders:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Paper Trading", value="> Learn about paper trading and options paper trading via Webull.\n> Click to use:\n\n</webull paper_trading:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Volume Analysis", value="> Returns a live stream of the input ticker's volume analysis on the day.\n> Click to use:\n\n</webull volume_analysis:1122243464042659942>", inline=True)
    webull_commands.add_field(name=f"News Announcement", value=f"> Get the latest market news for a ticker.\n\n</webull news_announcement:1122243464042659942>")


    stocksera_commands = embeds[fudstop_stocksera]
    stocksera_commands.add_field(name=f"Earnings", value=f"> Returns earnings tickers for the given date range.\n> Click to use:\n\n</ss earnings_calendar:1122243463862300759>")
    stocksera_commands.add_field(name=f"FTDs", value=f"> Search market-wide FTDs ranked by highest to lowest with T+35 dates.\n> Click to use:\n\n</ss fails_to_deliver_market_wide:1122243463862300759>")
    stocksera_commands.add_field(name=f"Inflation", value=f"> Returns historic inflation up to the current day dated back to 1977.\n> Click to use:\n\n</ss inflation:1122243463862300759>")
    stocksera_commands.add_field(name=f"Insider Summary", value=f"> View the latest insider trades across the market.\n> Click to use:\n\n</ss insider_trading_market_wide:1122243463862300759>")
    stocksera_commands.add_field(name=f"Jobless Claims", value=f"> View the latest and historic jobless claims numbers.\n> Click to use:\n\n</ss jobless_claims:1122243463862300759>")
    stocksera_commands.add_field(name=f"Low Floats", value=f"> Returns tickers with extremely low free floats.\n> Click to use:\n\n</ss low_floats:1122243463862300759>")
    stocksera_commands.add_field(name=f"Market News", value=f"> Return market-wide news to track narratives.\n> Click to use:\n\n</ss market_news:1122243463862300759>")
    stocksera_commands.add_field(name=f"News Sentiment", value=f"> View headlines for a ticker and the underlying sentiment.\n> Click to use:\n\n</ss news_sentiment:1122243463862300759>")
    stocksera_commands.add_field(name=f"Reverse Repo", value=f"> View the latest and historic repo numbers from the FED.\n\n</ss reverse_repo:1122243463862300759>")
    stocksera_commands.add_field(name=f"SEC Filings", value=f"> View the latest SEC Filings for a ticker.\n> Click to use:\n\n</ss sec_filings:1122243463862300759>")
    stocksera_commands.add_field(name=f"Short Interest", value=f"> View tickers with high % of their float shorted.\n> Click to use:\n\n</ss short_interest:1122243463862300759>")
    stocksera_commands.add_field(name=f"Short Volume", value=f"> View a stock's latest and historic short volume.\n> Click to use:\n\n</ss short_volume:1122243463862300759>")
    stocksera_commands.add_field(name=f"Stocktwits", value=f"> Return a ticker's rank on StockTwits.\n> Click to use:\n\n</ss stocktwits:1122243463862300759>")
    stocksera_commands.add_field(name=f"Subreddits", value=f"> View a ticker's popular subreddit / active users and rank.\n> Click to use:\n\n</ss subreddits:1122243463862300759>")

    chart_commands = embeds[openbb_charting]
    chart_commands.add_field(name=f"Chart 3 Minute", value=f"> Charts a ticker on the 3 minute timeframe.\n\n</c3m:1004263746090324062>")
    chart_commands.add_field(name=f"Chart 5 Minute", value=f"> Charts a ticker on the 5 minute timeframe.\n\n</c5m:1004263746090324063>")
    chart_commands.add_field(name=f"Chart 15 Minute", value=f"> Charts a ticker on the 15 minute timeframe.\n\n</c15m:1004263746090324064>")
    chart_commands.add_field(name=f"Chart Daily", value=f"> Charts a ticker on the daily timeframe.\n\n</cd:1004263746090324061>")
    chart_commands.add_field(name=f"Chart Week", value=f"> Charts a ticker on the weekly timeframe.\n\n</cw:1004263746090324060>")
    chart_commands.add_field(name=f"Chart Custom", value=f"> Charts a ticker with custom timeframe.\n\n</chart:1004263746090324065>")
    chart_commands.add_field(name=f"Chart FIB", value=f"> Charts the fibbonaci for a ticker.\n\n</chartfib:1007163283276562512>")
    chart_commands.add_field(name=f"Chart Support & Resistance", value=f"> Charts support/resistance for a given ticker.\n\n</chartsr:1009175257590026281>")
  
    econ_commands = embeds[openbb_economy]
    econ_commands.add_field(name=f"Reverse Repo", value=f"> Get the latest reverse repo data.\n\n</econ revrepo:1004263746111275130>")
    econ_commands.add_field(name=f"Economic Calendar", value=f"> Displays a calendar of economic events.\n\n</econ calendar:1004263746111275130>")
    econ_commands.add_field(name=f"Commodities", value=f"> Futures and comoddities overview.\n\n</econ commodities:1004263746111275130>")
    econ_commands.add_field(name=f"Currencies", value=f"> Currencies overview.\n\n</econ currencies:1004263746111275130>")
    econ_commands.add_field(name=f"Fed Rates", value=f"> Upcoming Federal Rates decision with percent chance.\n\n</econ fedrates:1004263746111275130>")
    econ_commands.add_field(name=f"Global Bonds", value=f"> Global Bonds Overview.\n\n</econ glbonds:1004263746111275130>")
    econ_commands.add_field(name=f"Indicies", value=f"> Indices overview.\n\n</econ indices:1004263746111275130>")
    econ_commands.add_field(name=f"US Bonds", value=f"> Us bonds overview.\n\n</econ usbonds:1004263746111275130>")
    econ_commands.add_field(name=f"Yield Curve", value=f"> Displays US Bonds and Yield Curve.\n\n</econ yieldcurve:1004263746111275130>")


    dd_commands = embeds[openbb_dd]
    dd_commands.add_field(name=f"Earnings", value=f"> Earnings to occur in the coming business days.\n\n</dd earnings:1004263746090324066>")
    dd_commands.add_field(name=f"Pre-Market", value=f"> Displays pre-market data for a ticker.\n\n</dd pm:1004263746090324066>")
    dd_commands.add_field(name=f"After-Hours", value=f"> Displays after hours data for a ticker.\n\n</dd ah:1004263746090324066>")
    dd_commands.add_field(name=f"Analyst", value=f"> Displays analyst recommendations.\n\n</dd analyst:1004263746090324066>")
    dd_commands.add_field(name=f"Bio", value=f"> Displays a stock companie's bio.\n\n</dd bio:1004263746090324066>")
    dd_commands.add_field(name=f"Customers", value=f"> Displays customers of the company.\n\n</dd customers:1004263746090324066>")
    dd_commands.add_field(name=f"Dividend Info", value=f"> Displays dividend information for a ticker.\n\n</dd divinfo:1004263746090324066>")
    dd_commands.add_field(name=f"Earnings Move", value=f"> Displays implied earnings move based on option prices.\n\n</dd ermove:1004263746090324066>")
    dd_commands.add_field(name=f"Earnings Estimate", value=f"> Display earnings estimates for a ticker.\n\n</dd est:1004263746090324066>")
    dd_commands.add_field(name=f"Insider Trades", value=f"> Displays latest 15 transactions from insiders for a ticker.\n\n</dd financials:1004263746090324066>")
    dd_commands.add_field(name=f"Institution Holdings", value=f"> View institutional holdings for a ticker.\n\n</dd institutions:1004263746090324066>")
    dd_commands.add_field(name=f"Next Earnings", value=f"> Displays next earnings for a ticker.\n\n</dd nexter:1004263746090324066>")
    dd_commands.add_field(name=f"Price Target", value=f"> Displays recent price targets with chart for a ticker.\n\n</dd pt:1004263746090324066>")
    dd_commands.add_field(name=f"SEC Filings", value=f"> Displays recent SEC filings for a ticker.\n\n</dd sec:1004263746090324066>")
    dd_commands.add_field(name=f"Splits", value=f"> Displays split and historic split info for a ticker.\n\n</dd splits:1004263746090324066>")
    dd_commands.add_field(name=f"Suppliers", value=f"> Displays suppliers of a company.\n\n</dd supplier:1004263746090324066>")
    dd_commands.add_field(name=f"Year to Date", value=f"> Displays year to date performance for a ticker.\n\n</dd ytd:1004263746090324066>")

    dp_commands = embeds[openbb_dp]
    dp_commands.add_field(name=f"All Blocks", value=f"> Displays the last 15 block trades.\n\n</dp allblocks:1004263746170011748>")
    dp_commands.add_field(name=f"All Dark Pools", value=f"> Displays the last 15 dark pool trades.\n\n</dp alldp:1004263746170011748>")
    dp_commands.add_field(name=f"All Prints", value=f"> Displays the last 15 combination of dark pool and block trades.\n\n</dp allprints:1004263746170011748>")
    dp_commands.add_field(name=f"Big Prints", value=f"> Biggest levels of all prints over x number of days.\n\n</dp bigprints:1004263746170011748>")
    dp_commands.add_field(name=f"Dark Pool Levels", value=f"> Displays the last 15 block trades.\n\n</dp levels:1004263746170011748>")
    dp_commands.add_field(name=f"Dark Pool Sectors", value=f"> Summary of all prints by market cap and sector.\n\n</dp sectors:1004263746170011748>")
    dp_commands.add_field(name=f"Dark Pool Summary", value=f"> Summary of all prints by % market cap.\n\n</dp summary:1004263746170011748>")
    dp_commands.add_field(name=f"Top Summary", value=f"> Displays total block and dark pool data.\n\n</dp topsum:1004263746170011748>")


    flow_commands = embeds[openbb_flow]

    flow_commands.add_field(name=f"Big Flow", value=f"> Returns the top 20 largest option trades by premium. \n\n</flow bigflow:1004263746170011749>")
    flow_commands.add_field(name=f"Day Flow", value=f"> Returns the most recent flow for a stock.\n\n</flow day:1004263746170011749>")
    flow_commands.add_field(name=f"Opening Flow", value=f"> Top 20 opening flow where volume is greater than open interest.\n\n</flow opening:1004263746170011749>")
    flow_commands.add_field(name=f"Flow Premium", value=f"> Returns a chart with the summary of premium per day by calls and puts.\n\n</flow prem:1004263746170011749>")
    flow_commands.add_field(name=f"Sector Flow", value=f"> Summary of all flow by market cap per sector.\n\n</flow sectors:1004263746170011749>")
    flow_commands.add_field(name=f"Day Summary", value=f"> Graphs today's total premium for a stock.\n\n</flow sumday:1004263746170011749>")
    flow_commands.add_field(name=f"Expiration Summary", value=f"> Flow summary by expiration date for a ticker.\n\n</flow bigflow:1004263746170011749>")
    flow_commands.add_field(name=f"Flow Summary", value=f"> Summary of all flow by % market cap.\n\n</flow summary:1004263746170011749>")
    flow_commands.add_field(name=f"Flow Sumtop", value=f"> Top flow for the day - calls vs puts by stock.\n\n</flow sumtop:1004263746170011749>")
    flow_commands.add_field(name=f"Weekly Summary", value=f"> Graph the weekly premium for a stock.\n\n</flow sumweek:1004263746170011749>")
    flow_commands.add_field(name=f"Unusual Flow", value=f"> Unusual option trades with over $100,000 in premium.\n\n</flow unu:1004263746170011749>")
    flow_commands.add_field(name=f"Weekly Flow", value=f"> Top 20 flow premium for a stock with weekly expirations.\n\n</flow bigflow:1004263746170011749>")
    

    options_commands = embeds[openbb_op]
    options_commands.add_field(name=f"Options Chains", value=f"> Displays the option chain by expiry for a stock.\n\n</op chains:1004263746111275138>")
    options_commands.add_field(name=f"Equity Put/Call Ratio", value=f"> Displays the equity put/call volume ratio.\n\n</op equitypc:1004263746111275138>")
    options_commands.add_field(name=f"Gamma", value=f"> Displays gamma levels for a stock.\n\n</op gamma:1004263746111275138>")
    options_commands.add_field(name=f"High IV", value=f"> Displays the top 15 IV30 tickers.\n\n</op highiv:1004263746111275138>")
    options_commands.add_field(name=f"Price History", value=f"> Displays option price history on a chart.\n\n</op hist:1004263746111275138>")
    options_commands.add_field(name=f"Index Put/Call Ratio", value=f"> Displays the index put/call ratio for the market.\n\n</op indexpc:1004263746111275138>")
    options_commands.add_field(name=f"In the Money", value=f"> Displays in the money options by expiry for a stock.\n\n</op itm:1004263746111275138>")
    options_commands.add_field(name=f"Max Pain", value=f"> Displays max pain by expiry for a stock.\n\n</op maxpain:1004263746111275138>")
    options_commands.add_field(name=f"Open Interest", value=f"> Displays the open interest and put/call ratio for a stock in a table.\n\n</op oi:1004263746111275138>")
    options_commands.add_field(name=f"Open Interst Chart", value=f"> Charts total open interest by strike price.\n\n</op oichart:1004263746111275138>")
    options_commands.add_field(name=f"Option Smile", value=f"> Charts the option volatility smile for a stock.\n\n</op smile:1004263746111275138>")
    options_commands.add_field(name=f"Option Stats", value=f"> Displays options statistics for a stock.\n\n</op stats:1004263746111275138>")
    options_commands.add_field(name=f"Top Open Interest", value=f"> Displays top open interest for a ticker.\n\n</op topoi:1004263746111275138>")
    options_commands.add_field(name=f"Top Open Interest Change", value=f"> Displays top open interest changes for a ticker.\n\n</op topoichange:1004263746111275138>")
    options_commands.add_field(name=f"Top Strike Volume", value=f"> Displays top strikes recieving volume for a ticker. Can also query by expiration.\n\n</op topstrikevol:1004263746111275138>")
    options_commands.add_field(name=f"Unusual Options", value=f"> Shows unusual options.\n\n</op unu:1004263746111275138>")
    options_commands.add_field(name=f"Unusual Options Stock", value=f"> Displays top 20 average volume tickers.\n\n</op uoastock:1004263746111275138>")
    options_commands.add_field(name=f"ETF Options", value=f"> Displays top 15 etfs for option volume.\n\n</op topvoletf:1004263746111275138>")
    options_commands.add_field(name=f"Volatility Surface", value=f"> Displays a ticker's option volatility surface.\n\n</op vsurf:1004263746111275138>")

    analysis_commands = embeds[fudstop_analysis]
    analysis_commands.add_field(name=f"Finscreener", value=f"> Screen for different patterns, technical conditions, and more using the fin-screener command.\n\n</analysis finscreen:1122243463723876533>")
    analysis_commands.add_field(name=f"Gaps Up", value=f"> Screen for gaps down - customizable by percent.\n\n</analysis gaps_up:1122243463723876533>")
    analysis_commands.add_field(name=f"Gaps Down", value=f"> Screen for gaps up - customizable by percent.\n\n</analysis gaps_down:1122243463723876533>")
    analysis_commands.add_field(name=f"Overbought Gaps", value=f"> Search for gaps paired with an overbought RSI for a downside opportunity.\n\n</analysis overbought_gaps:1122243463723876533>")
    analysis_commands.add_field(name=f"Top Shorts", value=f"> Screen for different patterns, technical conditions, and more using the fin-screener command.\n\n</analysis top_shorts:1122243463723876533>")
    
    learn_commands = embeds[fudstop_learn]
    learn_commands.add_field(name=f"Learn Covered Calls", value=f"> Learn about Level 1 Options - Covered Calls\n\n</learn covered_calls:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Calls", value=f"> Learn about Level 2 Options - Long Call options.\n\n</learn calls:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Candle Patterns", value=f"> Learn about various candlestick patterns and view animated gifs.\n\n</learn candle_patterns:1122243463723876538>")
    learn_commands.add_field(name=f"Learn China", value=f"> Learn about the China opportunity and how it's tied into US Monetary Policy.\n\n</learn china:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Core Criteria", value=f"> Learn the Core Logic criteria for trading options.\n\n</learn core_criteria:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Core Logic", value=f"> Learn about the Core Logic trading strategy used in the FUDSTOP Discord.\n\n</learn core_logic:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Discord", value=f"> Learn about Discord, the FUDSTOP Server, and helpful tips and tricks.\n\n</learn discord:1122243463723876538>")
    learn_commands.add_field(name=f"Learn ETFs", value=f"> Learn about exchange traded funds.\n\n</learn etfs:1122243463723876538>")
    learn_commands.add_field(name=f"Learn SEC Filings", value=f"> Learn about SEC Filings out of the NSCC, DTCC, OCC, FINRA, PCAOB, NYSE, MIAX, NASDAQ, CFR, the Fed, and many more market agencies.\n\n</learn filings:1122243463723876538>")
    learn_commands.add_field(name=f"Learn FINRA", value=f"> Learn about FINRA and their history.\n\n</learn finra:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Greeks", value=f"> Learn about the option greeks.\n\n</learn greeks:1122243463723876538>")
    learn_commands.add_field(name=f"Learn NSFR Ratio", value=f"> Learn about the Net Stable Funding Ratio\n\n</learn nsfr_ratio:1122243463723876538>")
    learn_commands.add_field(name=f"Learn OCC", value=f"> Learn about the Options Clearing Corporation and important developments since Covid out of this industry.\n\n</learn occ:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Option Strategies", value=f"> Learn about different option trading strategies.\n\n</learn option_strategies:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Options 101", value=f"> Take the Options 101 Course provided by CBOE Global Markets.\n\n</learn options_101:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Order Types", value=f"> Learn about the different market order types.\n\n</learn order_types:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Technical Analysis", value=f"> Learn about technical analysis patterns and how they can be utilized.\n\n</learn ta:1122243463723876538>")



    navigation_commands = embeds[fudstop_nav]
    navigation_commands.add_field(name=f"Navigate Channels", value=f"> Navigate through the discord by searching through the channels with a convenient auto-complete search menu.\n\n> </navigate channels:1122243463723876539>")
    navigation_commands.add_field(name=f"Navigate Forums", value=f"> Navigate through the discord by searching through the forums with a convenient auto-complete search menu.\n\n> </navigate forums:1122243463723876539>")
    navigation_commands.add_field(name=f"Navigate Threads", value=f"> Navigate through the discord by searching through the member threads and forum threats with a convenient auto-complete search menu.\n\n> </navigate threads:1122243463723876539>")

    agency_commands = embeds[fudstop_agencies]
    agency_commands.add_field(name=f"Soma Holdings", value=f"> View the latest FED SOMA holdings, The Federal Reserve System Open Market Account (SOMA) contains dollar-denominated assets acquired through open market operations.\n\n> These securities serve several purposes:\n\n> They are:collateral for U.S. currency in circulation and other liabilities on the Federal Reserve System’s balance sheet;\n> a tool for the Federal Reserve’s management of reserve balances;\n> and a tool for achieving the Federal Reserve’s macroeconomic objectives.\n\n**Click to Run:**\n</fed soma:1122243463723876535>", inline=False)
    agency_commands.add_field(name=f"Rates", value=f"> Returns global rates for all central banks - secured rates.\n\n</fed rates:1122243463723876535>")
    agency_commands.add_field(name=f"Swaps Non-Us", value=f"> Returns the latest Non-US denominated currency swaps from the FED.\n\n</fed swaps_non_us:1122243463723876535>")
    agency_commands.add_field(name=f"OCC Volume", value=f"> Returns the day's volume stats from the Options Clearing Corporation.\n\n</occ total_volume:1122243463723876541>")
    agency_commands.add_field(name=f"OCC Totals", value=f"> Returns total futures, options, and trade volume averages.\n\n</occ totals:1122243463723876541> ")
    agency_commands.add_field(name=f"OFR Advanced Repo", value=f"> View and download all participant repo data.\n\n</ofr advanced_repo:1122243463723876542>")






    school_commands = embeds[fudstop_school]
    school_commands.add_field(name=f"Technical Signals", value=f"> Learn about technical analysis signals\n\n</school tech_analysis:1122243463862300756>")
    school_commands.add_field(name=f"ETFs", value=f"> Learn about ETFs, how they're made - and how they work.\n\n</school etfs:1122243463862300756>")
    school_commands.add_field(name=f"Time-Related Vocabulary", value=f"> Learn about the different time-related vocabulary frequently encountered in markets.\n\n</school time:1122243463862300756>")
    school_commands.add_field(name=f"Candlestick Patterns", value=f"> Learn about different technical candlestick patterns.\n\n</school patterns:1122243463862300756>")
    




    stream_commands = embeds[fudstop_stream]
    stream_commands.add_field(name=f"Double Crypto", value=f"> Stream two crypto coins simultaneously.\n\n</stream double_crypto:1122243463862300762>")
    stream_commands.add_field(name=f"Crypto", value=f"> Stream a single crypto coin with live prices.\n\n</stream crypto:1122243463862300762>")
    stream_commands.add_field(name=f"Double-Quote", value=f"> Stream two stock tickers simultaneously and also track live volume.\n\n</stream double_quote:1122243463862300762>")
    stream_commands.add_field(name=f"Top Volume", value=f"> Constantly monitors the top-most traded option contract in real time.\n\n</stream topvolume:1122243463862300762>")
    stream_commands.add_field(name=f"Tits", value=f"> Stream some titties.\n\n</stream tits:1122243463862300762>")

    stock_commands = embeds[fudstop_stock]
    stock_commands.add_field(name=f"Capital-flow",value=f"> View the capital flow broken down by player size for a ticker.\n\n</stock capitalflow:1122243463862300760>")
    stock_commands.add_field(name=f"Company Brief",value=f"> View company information.\n\n</poly company_information:1122243463862300754>")
    stock_commands.add_field(name=f"IPO Calendar",value=f"> Pull up the IPO Calendar, or tickers that are listing on the markets for the first time.\n\n</stock ipos:1122243463862300760>")
    stock_commands.add_field(name=f"Institutions",value=f"> View Institutional Holdings for a ticker.\n\n</stock institutions:1122243463862300760>")
    stock_commands.add_field(name=f"Short Interest",value=f"> View the latest short interest report out of FINRA for a ticker.\n\n</stock shortinterest:1122243463862300760>")
    stock_commands.add_field(name=f"Insider Summary",value=f"> View the latest insider transactions for a stock.\n\n</stock insider_summary:1122243463862300760>")
    stock_commands.add_field(name=f"Order Flow",value=f"> View live order-flow for a ticker.\n\n</stock orderflow:1122243463862300760>")
    stock_commands.add_field(name=f"Leverage",value=f"> View stock leverage information such as interest rate, overnight rates, margin, and shortability.\n\n</stock leverage:1122243463862300760>")

    


    other_commands = embeds[fudstop_other]
    other_commands.add_field(name=f"GPT4", value=f"> Call upon and interact with GPT4 right in discord. After calling the command initially - carry on as if you were having a normal conversation. A helpful tool for productivity but not an all-seeing magician.\n\n</gpt4:1122365837739819029>")
    other_commands.add_field(name=f"AllSkew", value=f"> Track all option skews across the top most 800 traded tickers in real time.\n\n</allskew:1121980575276879983>")
    other_commands.add_field(name=f"Skew Finder", value=f"> Find and track the skew of any ticker in real time.\n\n</skew finder:1122736124524249088>")
    other_commands.add_field(name=f"Social Sentiment", value=f"> View current social sentiment surrounding a ticker.\n\n</social sentiment:1122243463862300758>")
    other_commands.add_field(name=f"TradingView Spying", value=f"> Spy on tradingview conversations. (BUGGY)\n\n</social tradingview_spying:1122243463862300758>")


    fmp_commands = embeds[fudstop_fmp]
    fmp_commands.add_field(name=f"Country Risk Premium", value=f"> View global risk in order from riskiest country to least risky country.\n\n</fmp country_risk_premium:1122711896773103698>")
    fmp_commands.add_field(name=f"Price Target", value=f"> View price target data for a ticker.\n\n</fmp price_target:1122711896773103698>")

    fudopt_commands = embeds[fudstop_opts]
    fudopt_commands.add_field(name=f"Fetch Entire Chain", value=f"> Fetches a ticker's entire options chain across all expirations with all accompanying data - such as last trade, last quote, greeks, day stats, underlying ticker stats, and contract stats.\n\n</options fetch_entire_chain:1122243463862300753>")
    fudopt_commands.add_field(name=f"All Market Options", value=f"> Fetche's the entire options market organized by the data metric of your choosing.\n\n</options all_market_options:1122243463862300753>")
    page_select = PageSelect(embeds)
    view = AlertMenus(embeds).add_item(page_select)

    

    
    

    await ctx.send(embed=webull_commands, view=view)





@bot.command()
async def skews(ctx):
    data, table = await master.tabulate_options(sublist1)
    data = data.drop(['Call IV%', 'Put IV%', 'Call Change', 'Put Change'], axis=1)  # Remove Call IV% and Put IV% columns
    data = data.rename(columns={'Low IV Call Strike': 'Res.', 'Low IV Put Strike': 'Supt.', 'Put OI': 'pOI', 'Call OI': 'cOI'})  # Rename columns


    # Remove "2023-" from the date results
    data['Exp'] = data['Exp'].str.replace(r'^2023-', '', regex=True)
    # Reorder columns
    columns = ['Sym', 'Exp', 'pOI', 'cOI','Supt.', 'Price', 'Res.']
    data = data[columns]
    # Create a new metric "depth"
    data['depth'] = data['Supt.'] - data['Res.']
    data['Res.'] = data['Res.'].astype(float)
    data['Supt.'] = data['Supt.'].astype(float)
    # Sort by the new metric
    data = data.sort_values(by='depth')
# Perform comparisons using float values
    # data['Play'] = data.apply(lambda row: '🔴🔥' if float(row['Price']) > row['Res.'] and float(row['Price']) > row['Supt.'] else
    #                                     '🟢🔥' if float(row['Price']) < row['Res.'] and float(row['Price']) < row['Supt.'] else
    #                                     '🔴' if float(row['Price']) > row['Res.'] else
    #                                     '🟢' if float(row['Price']) < row['Supt.'] else
    #                                     '◽', axis=1)
    data = data.drop(columns=['depth'])

    paginated_data = paginate_dataframe(data)  # Paginate the data into a list of dataframes



    embeds = []  # List to store the embeds
    for i, df in enumerate(paginated_data):
        table = tabulate(df, headers='keys', tablefmt='fancy', showindex=False)
        embed = disnake.Embed(title=f"Page {i + 1} of {len(paginated_data)}")
        embed.description = f"```{table}```"
        embeds.append(embed)


    view = AlertMenus(embeds)

    await ctx.send(embed=embeds[0], view=view)

def paginate_dataframe(data, items_per_page=10):
    return [data[i:i+items_per_page] for i in range(0, len(data), items_per_page)]
import openai
from cfg import YOUR_OPENAI_KEY as openaikey
openai.api_key = openaikey



def load_extensions(bot):
    extensions = []
    cogs_directory = os.path.join(os.path.dirname(__file__), 'cogs')

    for filename in os.listdir(cogs_directory):
        if filename.endswith('.py'):
            extension_name = filename[:-3]  # Remove the .py extension
            extensions.append(f'cogs.{extension_name}')

    for extension in extensions:
        try:
            bot.load_extension(f'bot.{extension}')
        except Exception as e:
            print(f"Failed to load extension {extension} due to {e}")
if __name__ == '__main__':
    load_extensions(bot)
    bot.run(YOUR_DISCORD_BOT_TOKEN)



