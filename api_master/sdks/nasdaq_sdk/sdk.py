import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from cfg import YOUR_NASDAQ_KEY
from .lists import country_acronyms, repo_codes, sp500_codes, income_expenditure_codes, economic_indicator_codes, unemployment_codes, interest_rate_codes, gdp_codes
import pandas as pd
import requests
import io
session = requests.session()
class Nasdaq:
    def __init__(self):
        self.api_key = YOUR_NASDAQ_KEY
        self.base_url = "https://data.nasdaq.com/api/v3/datasets/"



    def bigmac(self):
        """Returns valuation per country."""
        for country in country_acronyms:
            r = session.get(f"{self.base_url}ECONOMIST/BIGMAC_{country}.csv?&api_key={self.api_key}")

            # Check if the request was successful
            if r.status_code == 200:
                # Create a file-like object from the response content
                file_like_object = io.BytesIO(r.content)

                df = pd.read_csv(file_like_object)

                # Save the DataFrame to a separate CSV file for each country
                filename = f"files/nasdaq/bigmac/{country}_bigmac.csv"
                df.to_csv(filename, index=False)
                print(f"Saved data for {country} to {filename}")

            else:
                print(f"Error downloading CSV for {country}: {r.status_code}")


    def inflation(self):
        """Returns inflation number across the globe."""
        for country in country_acronyms:
            r = session.get(f"{self.base_url}RATEINF/CPI_{country}.csv?&api_key={self.api_key}")

            # Check if the request was successful
            if r.status_code == 200:
                # Create a file-like object from the response content
                file_like_object = io.BytesIO(r.content)

                df = pd.read_csv(file_like_object)

                # Save the DataFrame to a separate CSV file for each country
                filename = f"files/nasdaq/inflation/{country}_inflation.csv"
                df.to_csv(filename, index=False)
                print(f"Saved data for {country} to {filename}")

            else:
                print(f"Error downloading CSV for {country}: {r.status_code}")


    def repo(self):
        """Get repo data from the Federal Reserve."""
        for repo_code in repo_codes:
            r = session.get(f"{self.base_url}FRED/{repo_code}.csv?&api_key={self.api_key}")



            # Check if the request was successful
            if r.status_code == 200:
                # Create a file-like object from the response content
                file_like_object = io.BytesIO(r.content)

                df = pd.read_csv(file_like_object)

                # Save the DataFrame to a separate CSV file for each country
                filename = f"files/nasdaq/repo/{repo_code}_repo.csv"
                df.to_csv(filename, index=False)
                print(f"Saved data for {repo_code} to {filename}")

            else:
                print(f"Error downloading CSV for {repo_code}: {r.status_code}")


    def sp500(self):
        """Get SP500 Macro data from the Federal Reserve."""
        for sp500_code in sp500_codes:
            r = session.get(f"{self.base_url}MULTPL/{sp500_code}.csv?&api_key={self.api_key}")



            # Check if the request was successful
            if r.status_code == 200:
                # Create a file-like object from the response content
                file_like_object = io.BytesIO(r.content)

                df = pd.read_csv(file_like_object)

                # Save the DataFrame to a separate CSV file for each country
                filename = f"files/nasdaq/sp_500/{sp500_code}.csv"
                df.to_csv(filename, index=False)
                print(f"Saved data for {sp500_code} to {filename}")

            else:
                print(f"Error downloading CSV for {sp500_code}: {r.status_code}")


    def income_expenditures(self):
        """Get income expenditure data from the Federal Reserve."""
        for income_expenditure_code in income_expenditure_codes:
            r = session.get(f"{self.base_url}FRED/{income_expenditure_code}.csv?&api_key={self.api_key}")



            # Check if the request was successful
            if r.status_code == 200:
                # Create a file-like object from the response content
                file_like_object = io.BytesIO(r.content)

                df = pd.read_csv(file_like_object)

                # Save the DataFrame to a separate CSV file for each country
                filename = f"files/nasdaq/income_expenditures/{income_expenditure_code}.csv"
                df.to_csv(filename, index=False)
                print(f"Saved data for {income_expenditure_code} to {filename}")

            else:
                print(f"Error downloading CSV for {income_expenditure_code}: {r.status_code}")

    def economic_indicators(self):
        for economic_indicator_code in economic_indicator_codes:
            r = session.get(f"{self.base_url}FRED/{economic_indicator_code}.csv?&api_key={self.api_key}")



            # Check if the request was successful
            if r.status_code == 200:
                # Create a file-like object from the response content
                file_like_object = io.BytesIO(r.content)

                df = pd.read_csv(file_like_object)

                # Save the DataFrame to a separate CSV file for each country
                filename = f"files/nasdaq/economic_indicators/{economic_indicator_code}.csv"
                df.to_csv(filename, index=False)
                print(f"Saved data for {economic_indicator_code} to {filename}")

            else:
                print(f"Error downloading CSV for {economic_indicator_code}: {r.status_code}")


    def unemployment(self):
        """Return unemeployment data from the FED"""
        for unemployment_code in unemployment_codes:
            r = session.get(f"{self.base_url}FRED/{unemployment_code}.csv?&api_key={self.api_key}")



            # Check if the request was successful
            if r.status_code == 200:
                # Create a file-like object from the response content
                file_like_object = io.BytesIO(r.content)

                df = pd.read_csv(file_like_object)

                # Save the DataFrame to a separate CSV file for each country
                filename = f"files/nasdaq/unemployment/{unemployment_code}.csv"
                df.to_csv(filename, index=False)
                print(f"Saved data for {unemployment_code} to {filename}")

            else:
                print(f"Error downloading CSV for {unemployment_code}: {r.status_code}")



    def interest_rates(self):

        for interest_rate_code in interest_rate_codes:
            r = session.get(f"{self.base_url}FRED/{interest_rate_code}.csv?&api_key={self.api_key}")



            # Check if the request was successful
            if r.status_code == 200:
                # Create a file-like object from the response content
                file_like_object = io.BytesIO(r.content)

                df = pd.read_csv(file_like_object)

                # Save the DataFrame to a separate CSV file for each country
                filename = f"files/nasdaq/interest_rates/{interest_rate_code}.csv"
                df.to_csv(filename, index=False)
                print(f"Saved data for {interest_rate_code} to {filename}")

            else:
                print(f"Error downloading CSV for {interest_rate_code}: {r.status_code}")


    def gdp(self):
        """Returns gross domestic product spreadsheets."""

        for gdp_code in gdp_codes:
            r = session.get(f"{self.base_url}FRED/{gdp_code}.csv?&api_key={self.api_key}")



            # Check if the request was successful
            if r.status_code == 200:
                # Create a file-like object from the response content
                file_like_object = io.BytesIO(r.content)

                df = pd.read_csv(file_like_object)

                # Save the DataFrame to a separate CSV file for each country
                filename = f"files/nasdaq/gdp/{gdp_code}.csv"
                df.to_csv(filename, index=False)
                print(f"Saved data for {gdp_code} to {filename}")

            else:
                print(f"Error downloading CSV for {gdp_code}: {r.status_code}")

