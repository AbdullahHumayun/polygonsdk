import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from cfg import today_str
from sdks.fed_newyork_sdk.sdk import FedNewyork
import pandas as pd


sdk = FedNewyork()




repo = sdk.repo_operations_search(start_date="2023-01-01", end_date=today_str)


repo_df = repo.df
detail_df = repo.detail_df

# Define the directory path
directory = 'files/fed_reserve/repo/'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file paths
filename = f'{directory}repo_data.csv'
detail_filename = f'{directory}repo_data_detail.csv'

repo.df.to_csv(filename) #you will now have this file
repo.detail_df.to_csv(detail_filename) #you will now have this file



###get latest repo numbers###

sdk = FedNewyork()


repo = sdk.repo_latest()



print("Total Amount Submitted:", repo.totalAmtSubmitted[0])
print("Total Amount Accepted:", repo.totalAmtAccepted[0])
print("Maturity Date:", repo.maturityDate[0])