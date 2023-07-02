import requests
import disnake
from disnake.ext import commands
from _discord import emojis
from time import sleep
import os
from requests.auth import HTTPBasicAuth
import time
from typing import List
import matplotlib.pyplot as plt
from io import BytesIO

from disnake import ui
import pandas as pd
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from menus.embedmenus import AlertMenus
from sdks.polygon_sdk.mapping_dicts import OPTIONS_EXCHANGES, option_condition_dict
from sdks.helpers.helpers import human_readable
import asyncio
from cfg import YOUR_API_KEY
import numpy as np
polygon_options = PolygonOptionsSDK(YOUR_API_KEY)
polygon = AsyncPolygonSDK(YOUR_API_KEY)

headers = ["implied_volatility","open_interest","day_change_percent","day_volume","day_vwap","contract_type","expiration_date","strike_price","delta","gamma","theta","vega","ask","ask_size","bid","bid_size","midpoint","conditions","exchange","price","sip_timestamp","size","change_to_break_even","underlying_price","underlying_ticker"]



class ChartSelect(disnake.ui.Select):
    def __init__(self, df: pd.DataFrame, tickers: List[str]):
        self.df = df
        self.tickers = tickers  # Store tickers
        options = [
            disnake.SelectOption(label='Volatility Skew vs. Expiration Dates', value='volatility_skew'),
        ]
        super().__init__(
            placeholder="Chart data -->",
            min_values=1,
            max_values=1,
            custom_id="chart-selector",
            options=options
        )

class ChartSelect(disnake.ui.Select):
    def __init__(self, df: pd.DataFrame, tickers: List[str]):
        self.df = df
        self.tickers = tickers  # Store tickers
        options = [
            disnake.SelectOption(label='Volatility Skew vs. Expiration Dates', value='volatility_skew'),
        ]
        super().__init__(
            placeholder="Chart data -->",
            min_values=1,
            max_values=1,
            custom_id="chart-selector",
            options=options
        )

    async def callback(self, inter: disnake.MessageCommandInteraction):
        selected_option = inter.data['values'][0]

        if selected_option == 'volatility_skew':
            # Filter rows with the lowest IV for each expiration date
            filtered_df = self.df.groupby('expiration_date').apply(lambda x: x.loc[x['implied_volatility'].idxmin()])

            # Generate chart
            fig = plt.figure(figsize=(10, 6), dpi=100, facecolor='#F5F5DC')
            ax = fig.add_subplot(111, projection='3d')

            # Get unique expiration dates and strikes
            expiration_dates = filtered_df['expiration_date'].unique()
            strikes = filtered_df['strike_price'].unique()

            # Create meshgrid
            X, Y = np.meshgrid(expiration_dates, strikes)

            # Initialize Z values
            Z = np.zeros_like(X, dtype=float)

            # Iterate through each cell in the meshgrid and assign the corresponding implied volatility value
            for i, exp_date in enumerate(expiration_dates):
                for j, strike in enumerate(strikes):
                    iv = filtered_df[(filtered_df['expiration_date'] == exp_date) & (filtered_df['strike_price'] == strike)]['implied_volatility']
                    if len(iv) > 0:
                        Z[j, i] = iv.iloc[0]

            # Plot the 3D surface
            ax.plot_surface(X, Y, Z, cmap='viridis')

            ax.set_xlabel('Expiration Date', color='w')
            ax.set_ylabel('Strike Price', color='w')
            ax.set_zlabel('Implied Volatility', color='w')

            # Set title with ticker information
            tickers = ', '.join(self.tickers)  # Use stored tickers
            ax.set_title(f"Volatility Skew for Tickers: {tickers}", color='w')

            # Set dark gridlines
            ax.grid(color='w', linestyle='--', linewidth=0.3)
            ax.spines['bottom'].set_color('w')
            ax.spines['top'].set_color('w')
            ax.spines['right'].set_color('w')
            ax.spines['left'].set_color('w')

            # Mark the strikes with the lowest IV
            lowest_iv = filtered_df.groupby('expiration_date')['implied_volatility'].idxmin()
            ax.scatter(
                filtered_df.loc[lowest_iv, 'expiration_date'],
                filtered_df.loc[lowest_iv, 'strike_price'],
                filtered_df.loc[lowest_iv, 'implied_volatility'],
                color='red',
                s=50,
                label='Lowest IV'
            )

            # Customize the chart
            ax.view_init(elev=30, azim=45)  # Adjust the view angle
            ax.dist = 12  # Adjust the camera distance

            # Save chart to a BytesIO object with transparent background
            chart_bytes = BytesIO()
            plt.savefig(chart_bytes, format='png', transparent=True)
            chart_bytes.seek(0)

            # Create an embed with the chart as an attachment
            embed = disnake.Embed()
            embed.set_image(url="attachment://chart.png")

            # Send the chart as an embed attachment
            await inter.response.edit_message(content="Chart:", file=disnake.File(chart_bytes, filename="chart.png"), embed=embed)
class SortView(disnake.ui.View):
    def __init__(self, df:pd.DataFrame, tickers):
        self.df = df
        self.tickers=tickers
        super().__init__(timeout=None)

        self.add_item(ChartSelect(df, tickers))
        self.add_item(SortSelect(df, tickers))
        



class SortSelect(disnake.ui.Select):
    def __init__(self, df: pd.DataFrame, tickers):
        self.tickers=tickers
        self.df = df
        super().__init__(placeholder="Sort Data-->",
                         min_values=1,
                         max_values=1,
                         custom_id="sorter",
                         options= [ 
                             disnake.SelectOption(label='Implied Volatility',value = "implied_volatility", description='Sort IV - lowest to highest.', emoji=f"{emojis.shot}"),
                             disnake.SelectOption(label='Volume',value=f"day_volume", description='Sort Volume - Highest to Lowest.', emoji=f"{emojis.dodo}"),
                             disnake.SelectOption(label='Open Interest',value=f"open_interest", description='Sort OI - highest to lowest.', emoji=f"{emojis.crown}"),
                             disnake.SelectOption(label='Change Percent',value="day_change_percent", description='Sort by change percent- highest to lowest.', emoji=f"{emojis.question}"),
                             disnake.SelectOption(label='Last Trade Size',value="size", description='Sort IV - lowest to highest.', emoji=f"{emojis.moneytower}"),
                             disnake.SelectOption(label='Gamma',value="gamma", description='Sort Gamma - highest to lowest.', emoji=f"{emojis.movingchart}"),
                             disnake.SelectOption(label='Delta',value="delta", description='Sort Delta - highest to lowest.', emoji=f"{emojis.coolchart}"),

                         ])
    
    async def callback(self, inter:disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            if self._selected_values:
                # Remove the previously sorted file
                prev_sorted_filename = f'files/options/ticker_chains/{self._selected_values}_sorted.csv'
                if os.path.exists(prev_sorted_filename):
                    os.remove(prev_sorted_filename)
                df = self.df.sort_values(self._selected_values)
                print(df)
                filename=f'files/options/ticker_chains/{self._selected_values}_sorted.csv'
                df.to_csv(filename)
                await inter.response.edit_message(f"> Data successfully sorted by {self._selected_values} - all chains.",file=disnake.File(filename), view=SortView(df, self.tickers))



class Options(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def options(self, inter):
        pass

    @options.sub_command()
    async def fetch_entire_chain(self, inter: disnake.AppCommandInter, tickers: str):
        """Fetches the latest up-to-date data for every option for any ticker across all expirations."""
        
        tickers = tickers.split(',')
        await inter.response.defer()
        
        async def fetch_options_data(ticker):
            all_options = await polygon_options.get_option_chain_all(ticker)
            return pd.DataFrame(all_options.data_dict)

        tasks = [fetch_options_data(ticker) for ticker in tickers]
        combined_data = await asyncio.gather(*tasks)

        if combined_data:
            combined_df = pd.concat(combined_data, ignore_index=True).sort_values(by="implied_volatility", ascending=True)
            combined_df.to_csv('files/options/ticker_chains/all_tickers_combined.csv', index=False)

            view = SortView(combined_df, tickers)

            await inter.edit_original_message(view=view)




        else:
            await inter.send("No data available for the given tickers.")






def setup(bot:commands.Bot):
    bot.add_cog(Options(bot))
    print(f"> Extension {__name__} is ready\n")