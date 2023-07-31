import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import random

from sdks.models.test_events import TestIndicesEvent
from sdks.polygon_sdk.list_sets import sublist1
from cfg import sector_hooks
from asyncio import Queue
from typing import List
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
import asyncio
from disnake.ext import commands

import disnake
import pandas as pd
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
df = pd.read_csv('files/indices/all_indices_data.csv') #you must download this spreadsheet from the "get_latest_options_data.py" file.

@bot.slash_command()
async def send_indices_messages(inter: disnake.AppCmdInter):  # Only takes options_handler
    await inter.response.defer()
    while True:

        index = random.randint(0, len(df) - 1)
        row = df.iloc[index]
 
        event_indices = TestIndicesEvent.from_row(row)

        # Call the handler with the message
        await indices_handler([event_indices])
        await inter.edit_original_message(row)

async def consume(queue: asyncio.Queue):
    

    while True:
        
        data = await queue.get()
        for msgs in data:
            print(msgs)
async def indices_handler(msgs: List[TestIndicesEvent]):
    print(msgs)



from cfg import YOUR_DISCORD_BOT_TOKEN
async def main():

    data_queue = Queue()
    num_messages_workers =6 


    # Create separate tasks for send_messages function with different handlers
    stock_messages_tasks = [asyncio.create_task(send_indices_messages(indices_handler)) for _ in range(num_messages_workers)]

    await asyncio.gather(*stock_messages_tasks)

bot.run(YOUR_DISCORD_BOT_TOKEN)

