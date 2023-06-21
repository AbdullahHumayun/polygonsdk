import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from cfg import today_str
from sdks.fed_newyork_sdk.sdk import FedNewyork
import pandas as pd


sdk = FedNewyork()




securities_lending = sdk.securities_lending_search(start_date="2023-01-01", end_date=today_str)



# Define the directory path
directory = 'files/fed_reserve/securities_lending/'
filename = f'{directory}lending_search_results.csv'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

securities_lending.df.to_csv(filename)