import requests
import time
import csv
import aiohttp

from cfg import discord_headers
from .channel_ids import channels  # Dictionary containing channels
from .searching import Message

class DiscordSDK():

    def __init__(self):

        
        self.headers = discord_headers



    def search(self, guild, channel_name, search_content):
        base_url = f'https://discord.com/api/v9/guilds/{guild}/messages/search'

        # Get the channel ID from the dictionary
        channel_id = channels.get(channel_name)
        if not channel_id:
            print(f'Channel "{channel_name}" not found.')
            return

        all_messages = []
        offset = 0
        limit = 25

        while True:
            # Construct the URL for the given channel
            url = f'{base_url}?channel_id={channel_id}&include_nsfw=true&content={search_content}&limit={limit}&offset={offset}'
            print(url)
            # Perform the search request
            response = requests.get(url, headers=discord_headers).json()
            try:
                total_results = response['total_results']
            except KeyError:
                continue
            messages = response['messages']

            if not messages:
                break

            all_messages.extend([Message(i) for i in messages])

            # Update the offset for the next request
            offset += limit

            # Wait to avoid rate limiting (change the sleep duration as needed)
            time.sleep(0.5)

        # Save messages to a CSV file
        with open('discord_messages.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['message_id', 'author', 'content', 'timestamp']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            
            for message in all_messages:
                writer.writerow({'message_id': message.id, 'author': message.author, 'content': message.content, 'timestamp': message.timestamp})

        print(f'Saved {len(all_messages)} messages to discord_messages.csv')

        return all_messages, total_results       
    

    async def search_all(self, guild, max_id, search_content):
        base_url = f'https://discord.com/api/v9/guilds/{guild}/messages/search'

        for channel_name, channel_id in channels.items():

            url = f'{base_url}?channel_id={channel_id}&max_id={max_id}&include_nsfw=true&content={search_content}'


            response = requests.get(url, headers=self.headers)


            print(f'Search results for channel {channel_name}:')
            print(response.content)
            print('\n')

        


    async def get_discord_messages(self, guild, channel_id):
        base_url = f"https://discord.com/api/v9/guilds/{guild}/messages/search?channel_id={channel_id}&include_nsfw=true?limit=50"
        params = {"offset": 0}

        async with aiohttp.ClientSession() as session:
            all_results = []
            more_results = True

            while more_results:
                async with session.get(base_url, params=params, headers=discord_headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        results = data["messages"]

                        # Check if there are any results in the response
                        if results:
                            print(results)
                            all_results.extend(results)
                            params["offset"] += 25
                        else:
                            more_results = False
                    else:
                        print(f"Error fetching data: {response.status}")
                        more_results = False


    async def search_by_user(self, guild_id, author_id, content, include_nsfw):
        url = f"https://discord.com/api/v9/guilds/{guild_id}/messages/search"
        params = {
            "author_id": author_id,
            "content": content,
            "include_nsfw": include_nsfw
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=discord_headers, params=params) as response:
                json_response = await response.json()

                messages = []
                for message in json_response["messages"]:
                    for item in message:
                        messages.append(Message(item))

        return messages