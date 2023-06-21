import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from cfg import today_str
from sdks.fed_newyork_sdk.sdk import FedNewyork
import pandas as pd



sdk = FedNewyork()

ambs_auctions = sdk.liquidity_swaps_count(50) #returns last 100 operations
df_count = pd.DataFrame(vars(ambs_auctions))


# Define the directory path
directory = 'files/fed_reserve/fxswaps/'
# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)



# Define the file path
filename = f'{directory}fx_operations.csv'
df_count.to_csv(filename)





#choose a start / end date - default = today
ambs_search = sdk.liquidity_swaps_search(start_date="2023-01-01", end_date=today_str)
search_df = pd.DataFrame(vars(ambs_search))
filename2 = f'{directory}fx_operations_count.csv'


search_df.to_csv(filename2)