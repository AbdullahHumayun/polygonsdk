import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Reload the original data
data = pd.read_csv('aggregates_data_U.csv')
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Define the function to plot a single candle
def plot_candle(ax, timestamp, open_price, high_price, low_price, close_price):
    timestamp_num = mdates.date2num(timestamp)
    color = 'g' if open_price < close_price else 'r'
    ax.plot([timestamp_num, timestamp_num], [low_price, high_price], color=color)
    ax.add_patch(plt.Rectangle((timestamp_num - 0.4 / 24, min(open_price, close_price)),
                                0.8 / 24, abs(open_price - close_price), color=color))

# Create figure and axis
fig, ax = plt.subplots(figsize=(15, 7))

# Plot each candle
for i, row in data.iterrows():
    plot_candle(ax, row['Timestamp'], row['Open'], row['High'], row['Low'], row['Close'])

# Format the x-axis
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.xticks(rotation=45)

# Set labels and title
plt.title('Candlestick Chart')
plt.xlabel('Timestamp')
plt.ylabel('Price')
plt.grid(True)
plt.show()