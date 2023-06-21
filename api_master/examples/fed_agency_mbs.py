import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from cfg import today_str
from sdks.fed_newyork_sdk.sdk import FedNewyork
import pandas as pd



sdk = FedNewyork()

ambs_auctions = sdk.agency_mbs_count(100) #returns last 100 operations


df = pd.DataFrame(vars(ambs_auctions))

# Define the directory path
directory = 'files/fed_reserve/ambs/'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file path
filename = f'{directory}auctions.csv'

df.to_csv(filename)


#choose a start / end date - default = today
ambs_search = sdk.agency_mbs_search(start_date="2023-01-01", end_date=today_str) 


search_df = pd.DataFrame(vars(ambs_search))

# Define the directory path
directory = 'files/fed_reserve/ambs/'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file path
filename = f'{directory}auction_search.csv'

search_df.to_csv(filename)
