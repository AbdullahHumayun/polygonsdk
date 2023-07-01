import disnake
from autocomp import ticker_autocomp
from disnake.ext import commands
import aiohttp
import asyncio
from menus.embedmenus import SkewPageSelect,SkewAlertMenus
from tabulate import tabulate
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from cfg import YOUR_API_KEY
from cfg import today_str,seven_days_from_now_str, today_str
from sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot
from sdks.polygon_sdk.masterSDK import MasterSDK
poly = AsyncPolygonSDK(YOUR_API_KEY)
from _discord import emojis
import pandas as pd
poly_opt = PolygonOptionsSDK(YOUR_API_KEY)
sdk = MasterSDK()
webull = AsyncWebullSDK()
class Skew(commands.Cog):
    def __init__(self,bot):
        self.bot=bot





    @commands.slash_command()
    async def skew(self, inter):
        pass

    
    @skew.sub_command()
    async def allskew(self, inter:disnake.AppCmdInter):
        await inter.response.defer()
        tickers = ["AMD", "GME", "NVDA", "TSLA", "UPST", "BIDU", "U", "W", "MSFT"]
        all_rows = []

        for ticker in tickers:
            options_lists = await sdk.get_near_the_money_single(ticker, 5)
            print(options_lists)
            x = await poly_opt.get_universal_snapshot(options_lists)

            df = x.df
            calls = df[df['C/P'] == 'call'].sort_values('IV', ascending=True)
            puts = df[df['C/P'] == 'put'].sort_values('IV', ascending=True)

            call_skew = calls.iloc[[0]]
            put_skew = puts.iloc[[0]]
            # Rename headers in call_skew DataFrame
            call_skew = call_skew.rename(columns={"Vol": "C Vol", "OI": "C OI", "Skew": "C Skew", "IV": "C IV"})

            # Rename headers in put_skew DataFrame
            put_skew = put_skew.rename(columns={"Vol": "P Vol", "OI": "P OI", "Skew": "P Skew", "IV": "P IV"})

            # Select specific columns from call_skew DataFrame
            call_skew_selected = call_skew[["Sym","C IV", "C OI", "C Skew"]].reset_index(drop=True)

            # Select specific columns from put_skew DataFrame
            put_skew_selected = put_skew[["💲", "P Skew", "P OI", "P IV"]].reset_index(drop=True)

            combined_skew = pd.concat([call_skew_selected, put_skew_selected], axis=1)
            combined_skew = combined_skew.fillna("")  # Replace remaining NaN values with empty string

            # Dropping the duplicated 'Sym' column
            # Modify IV columns
            combined_skew["C IV"] = combined_skew["C IV"].apply(lambda x: round(float(x) * 100, 6) if x != "" else x)
            combined_skew["P IV"] = combined_skew["P IV"].apply(lambda x: round(float(x) * 100, 6) if x != "" else x)

            # Dropping the duplicated 'Sym' column
            combined_skew = combined_skew.loc[:, ~combined_skew.columns.duplicated()]
            all_rows.append(combined_skew)

        # Combine all dataframes in all_rows
        all_data = pd.concat(all_rows)

        # Print DataFrame as a fancy grid
        data_table = tabulate(all_data, headers='keys', tablefmt='fancy', showindex=False)
        embed = disnake.Embed(title=f"All Skew", description=f"```{data_table}```")
        await inter.edit_original_message(embed=embed)

    @skew.sub_command()
    async def multiple(inter: disnake.AppCmdInter, tickers: str):
        """Query multiple tickers for a static skew picture."""
        await inter.response.defer()
        tickers = tickers.split(',')
        embeds = []
        
        async def process_ticker(ticker: str):
            ticker = ticker.upper()
            if ticker.startswith("SPX"):
                price = await poly.get_index_price(ticker)
                lower_strike = round(price) * 0.97
                upper_strike = round(price) * 1.03
            else:
                price = await poly.get_stock_price(ticker)
                lower_strike = round(price) * 0.85
                upper_strike = round(price) * 1.15
            print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

            async with aiohttp.ClientSession() as session:
                initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-12-30&limit=250&apiKey={YOUR_API_KEY}"

                results = await poly._request_all_pages(initial_url)
                if results is not None:
                    option_data = UniversalOptionSnapshot(results)
                    calls = option_data.df[option_data.df['type'] == 'call']
                    puts = option_data.df[option_data.df['type'] == 'put']
                    calls_grouped = calls.groupby('exp')
                    puts_grouped = puts.groupby('exp')

                    async def process_grouped_tickers(grouped_df, session: aiohttp.ClientSession):
                        results = []
                        for _, group in grouped_df:
                            group_tickers = group['ticker'].tolist()
                            if not group_tickers:
                                continue
                            tickers_string = ','.join(group_tickers)
                            async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers_string}&apiKey={YOUR_API_KEY}") as response:
                                try:
                                    near_money = await response.json(content_type=None)
                                    near_money_results = near_money['results']
                                    atm_data = UniversalSnapshot(near_money_results)
                                    results.append(atm_data.df.sort_values('IV', ascending=True))
                                except Exception as e:
                                    print(f"Error processing tickers_string: {tickers_string}. Error: {e}")
                        return results

                    async with sem:  # Acquire semaphore to limit concurrent requests
                        calls_results = await process_grouped_tickers(calls_grouped, aiohttp.ClientSession)
                        calls_results_df = pd.concat(calls_results)
                        calls_grouped = calls_results_df.groupby('🗓️', as_index=False)

                        puts_results = await process_grouped_tickers(puts_grouped, session)
                        puts_results_df = pd.concat(puts_results)
                        puts_grouped = puts_results_df.groupby('🗓️', as_index=False)

                        calls_first_rows = calls_grouped.first()
                        puts_first_rows = puts_grouped.first()

                        calls_selected_columns_df = calls_first_rows[['🗓️', 'IV', 'Skew', '💲']]
                        puts_selected_columns_df = puts_first_rows[['🗓️', 'IV', 'Skew', '💲']]
                        calls_selected_columns_df['🗓️'] = calls_selected_columns_df['🗓️'].apply(lambda x: x[5:])
                        puts_selected_columns_df['🗓️'] = puts_selected_columns_df['🗓️'].apply(lambda x: x[5:])
                        calls_selected_columns_df['IV'] = (calls_selected_columns_df['IV'] * 100).round(4)
                        puts_selected_columns_df['IV'] = (puts_selected_columns_df['IV'] * 100).round(4)
                        calls_selected_columns_df = calls_selected_columns_df.reset_index(drop=True)[['🗓️', 'IV', 'Skew', '💲']]
                        puts_selected_columns_df = puts_selected_columns_df.reset_index(drop=True)[['🗓️', 'IV', 'Skew', '💲']]

                        print(calls_selected_columns_df)
                        print(puts_selected_columns_df)
                        call_table = tabulate(calls_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                        put_table = tabulate(puts_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                        embed = disnake.Embed(
                            title=f"Skews - {ticker} - Next 90 Days",
                            description=f"**CALLS:**```{call_table}```\n**PUTS:**```{put_table}```\n\n> Tickers Queried: {tickers}",
                            color=disnake.Colour.random()
                        )
                        embed.set_footer(text=f"Viewing Skews for {ticker}")
                        return embed

        sem = asyncio.Semaphore(100)  # Adjust the semaphore limit to a higher value

        tasks = [process_ticker(ticker) for ticker in tickers]

        results = await asyncio.gather(*tasks)
        
        view = SkewAlertMenus(results).add_item(SkewPageSelect(results, tickers))

        await inter.edit_original_message(embed=results[0], view=view)
        

    @skew.sub_command()
    async def pc(inter: disnake.AppCmdInter, ticker: str = commands.Param(autocomplete=ticker_autocomp)):
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
                    price = await poly.get_index_price(ticker)
                    lower_strike = round(price) * 0.97
                    upper_strike = round(price) * 1.03
                else:
                    price = await poly.get_stock_price(ticker)
                    lower_strike = round(price) * 0.85
                    upper_strike = round(price) * 1.15
                print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

                initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-09-30&limit=250&apiKey={YOUR_API_KEY}"
                results = await poly._request_all_pages(initial_url)

                if results is not None:
                    option_data = UniversalOptionSnapshot(results)
                    calls = option_data.df[option_data.df['type'] == 'call']
                    puts = option_data.df[option_data.df['type'] == 'put']
                    calls_grouped = calls.groupby('exp')
                    puts_grouped = puts.groupby('exp')

                    calls_results = await process_option_data(calls_grouped, session, sem)
                    calls_results_df = pd.concat(calls_results)
                    calls_grouped = calls_results_df.groupby('🗓️', as_index=False)

                    puts_results = await process_option_data(puts_grouped, session, sem)
                    puts_results_df = pd.concat(puts_results)
                    puts_grouped = puts_results_df.groupby('🗓️', as_index=False)

                    calls_first_rows = calls_grouped.first()
                    puts_first_rows = puts_grouped.first()

                    calls_selected_columns_df = calls_first_rows[['🗓️', 'IV', 'Skew', '💲', 'Size', 'Vol', 'OI']]
                    puts_selected_columns_df = puts_first_rows[['🗓️', 'IV', 'Skew', '💲', 'Size', 'Vol', 'OI']]
                    calls_selected_columns_df['🗓️'] = calls_selected_columns_df['🗓️'].apply(lambda x: x[5:])
                    puts_selected_columns_df['🗓️'] = puts_selected_columns_df['🗓️'].apply(lambda x: x[5:])
                    calls_selected_columns_df['IV'] = (calls_selected_columns_df['IV'] * 100).round(4)
                    puts_selected_columns_df['IV'] = (puts_selected_columns_df['IV'] * 100).round(4)
                    calls_selected_columns_df = calls_selected_columns_df.reset_index(drop=True)[['🗓️', 'IV', 'Skew', '💲', 'Size', 'Vol', 'OI']]
                    puts_selected_columns_df = puts_selected_columns_df.reset_index(drop=True)[['🗓️', 'IV', 'Skew', '💲', 'Size', 'Vol', 'OI']]

                    print(calls_selected_columns_df)
                    print(puts_selected_columns_df)
                    call_table = tabulate(calls_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                    put_table = tabulate(puts_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                    embed = disnake.Embed(title=f"Skews - {ticker} - Next 30 Days", description=f"**CALLS:**```{call_table}```\n**PUTS:**```{put_table}```", color=disnake.Colour.random())
                    embed.set_footer(text=f"Viewing Skews for {ticker}")
                    await inter.edit_original_message(embed=embed)
                    if counter == 50:
                        await inter.send("stream ended")
                        break


    @skew.sub_command()
    async def mobile(inter: disnake.AppCmdInter, ticker: str = commands.Param(autocomplete=ticker_autocomp)):
        "Skew command for mobile user format - less columns than PC."
        MAX_CONCURRENCY = 10
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
                    price = await poly.get_index_price(ticker)
                    lower_strike = round(price) * 0.97
                    upper_strike = round(price) * 1.03
                else:
                    price = await poly.get_stock_price(ticker)
                    lower_strike = round(price) * 0.85
                    upper_strike = round(price) * 1.15
                print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

                initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-09-30&limit=250&apiKey={YOUR_API_KEY}"
                results = await poly._request_all_pages(initial_url)

                if results is not None:
                    option_data = UniversalOptionSnapshot(results)
                    calls = option_data.df[option_data.df['type'] == 'call']
                    puts = option_data.df[option_data.df['type'] == 'put']
                    calls_grouped = calls.groupby('exp')
                    puts_grouped = puts.groupby('exp')

                    calls_results = await process_option_data(calls_grouped, session, sem)
                    calls_results_df = pd.concat(calls_results)
                    calls_grouped = calls_results_df.groupby('🗓️', as_index=False)

                    puts_results = await process_option_data(puts_grouped, session, sem)
                    puts_results_df = pd.concat(puts_results)
                    puts_grouped = puts_results_df.groupby('🗓️', as_index=False)

                    calls_first_rows = calls_grouped.first()
                    puts_first_rows = puts_grouped.first()

                    calls_selected_columns_df = calls_first_rows[['🗓️', 'IV', 'Skew', '💲', 'Size']]
                    puts_selected_columns_df = puts_first_rows[['🗓️', 'IV', 'Skew', '💲', 'Size']]
                    calls_selected_columns_df['🗓️'] = calls_selected_columns_df['🗓️'].apply(lambda x: x[5:])
                    puts_selected_columns_df['🗓️'] = puts_selected_columns_df['🗓️'].apply(lambda x: x[5:])
                    calls_selected_columns_df['IV'] = (calls_selected_columns_df['IV'] * 100).round(4)
                    puts_selected_columns_df['IV'] = (puts_selected_columns_df['IV'] * 100).round(4)
                    calls_selected_columns_df = calls_selected_columns_df.reset_index(drop=True)[['🗓️', 'IV', 'Skew', '💲', 'Size']]
                    puts_selected_columns_df = puts_selected_columns_df.reset_index(drop=True)[['🗓️', 'IV', 'Skew', '💲', 'Size']]

                    print(calls_selected_columns_df)
                    print(puts_selected_columns_df)
                    call_table = tabulate(calls_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                    put_table = tabulate(puts_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                    embed = disnake.Embed(title=f"Skews - {ticker} - Next 30 Days", description=f"**CALLS:**```{call_table}```\n**PUTS:**```{put_table}```", color=disnake.Colour.random())
                    embed.set_footer(text=f"Viewing Skews for {ticker}")
                    await inter.edit_original_message(embed=embed)
                    if counter == 50:
                        await inter.send("stream ended")
                        break

                                        
            
            ## non - spx money query

                else:
                    counter = 0
                    while True:
                        counter = counter + 1
                        price = await poly.get_stock_price(ticker)
                        
                        lower_strike = round(price) * 0.85 #greater thresholds for non-SPX
                        upper_strike = round(price) * 1.15
                        print(f"NON-SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")
                        #query non SPX longer


                        
                        async with aiohttp.ClientSession() as session:
                            initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={seven_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"
                            async with session.get(initial_url) as resp:
                                data = await resp.json()
                                results = data['results']
                                if results is not None:
                                    option_data = UniversalOptionSnapshot(results)
                                    symbols = str(option_data.ticker).replace("'","").replace(']','').replace('[','').replace(' ','')
                                    print(symbols)


                    
                                    async with aiohttp.ClientSession() as session:
                                        async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={symbols}&limit=1&apiKey={YOUR_API_KEY}") as response:
                                            near_money = await response.json()
                                            near_money_results = near_money['results']
                                            if near_money_results is not None:
                                                atm_data = UniversalSnapshot(near_money_results)
                            
                                                df = atm_data.df.sort_values('IV', ascending=True)
                                                call_df = df[df['Type'] == 'call'].sort_values('IV', ascending=True)
                                                put_df = df[df['Type'] == 'put'].sort_values('IV', ascending=True)
                     

                                                

                                                # Add a field for the call options
                                                call_table = call_df[['Sym','💲','Strike', 'IV', 'Exp', 'Type', 'Vol']].iloc[[0]]
                                                put_table = put_df[['Sym','💲','Strike', 'IV', 'Exp', 'Type', 'Vol']].iloc[[0]]
                                                put_rows = put_table.values.tolist()
                                                put_table_str = tabulate(put_rows, headers=put_table.columns, tablefmt="fancy")

                                                call_rows = call_table.values.tolist()
                                                call_table_str = tabulate(call_rows, headers=call_table.columns, tablefmt="fancy")

                                                combined_table = pd.concat([put_table, call_table])

                                                table_rows = combined_table.values.tolist()
                                                table_str = tabulate(table_rows, headers=combined_table.columns, tablefmt="fancy")

                                                embed = disnake.Embed(title=f"Skew Monitor - {ticker}", description=f"```\n{table_str}\n```", color=disnake.Colour.random())
                                                embed.set_footer(text=f"{ticker}",icon_url=await poly.get_polygon_logo(ticker))
                                    await inter.edit_original_message(embed=embed)
                                    if counter == 50:
                                        await inter.send("Stream ended")
                                        break

def setup(bot:commands.Bot):
    bot.add_cog(Skew(bot))
    print(f"> Extension {__name__} is ready\n")