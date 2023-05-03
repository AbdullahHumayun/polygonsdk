import requests


from typing import List


class Ticker:
    disSymbol: str
    symbol: str


class Position:
    id: int
    accountId: int
    paperId: int
    ticker: Ticker
    status: str
    position: float
    cost: float
    costPrice: float
    lastPrice: float
    marketValue: float
    unrealizedProfitLoss: float
    unrealizedProfitLossRate: float
    tickerType: str
    optionType: str
    optionExpireDate: str
    optionContractMultiplier: float
    optionExercisePrice: float
    belongTickerId: int

# Replace the following line with your actual Webull headers
webull_headers = {'Authorization': 'YOUR_AUTHORIZATION_TOKEN'}

# Fetch account data and extract positions
r2 = requests.get("https://act.webullfintech.com/webull-paper-center/api/paper/1/acc/11086026", headers=webull_headers).json()
positions_data = r2['positions']

# Convert the positions data into a list of Position objects
positions = [Position(**position_data) for position_data in positions_data]

# Print the cost and market value for each position
for position in positions:
    print(position.cost, position.marketValue)