import yfinance as yf
import matplotlib.pyplot as plt

from db_connect import get_data

# Fetch historical data for two different stocks
ticker1 = "AAPL"  # Apple
ticker2 = "MSFT"  # Microsoft

# data1 = yf.download(ticker1, start="2023-01-01", end="2024-01-01")
data1 = get_data()
data2 = yf.download(ticker2, start="2023-01-01", end="2024-01-01")

print(data1)
print(type(data1))

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Plot for the first stock (Apple)
# axs[0].plot(data1.index, data1['Close'], label='AAPL Close Price', color='blue')
axs[0].plot(data1.index, data1[6], label='BTC Close Price', color='blue')
axs[0].axhline(y=95100, color='red', linestyle='--', label='Level 1')
axs[0].axhline(y=94300, color='green', linestyle='--', label='Level 2')
axs[0].axhline(y=86600, color='red', linestyle='--', label='Level 3')
axs[0].axhline(y=85000, color='green', linestyle='--', label='Level 4')
axs[0].set_title('BTC Stock Price')
# axs[0].set_xlabel('time')
# axs[0].set_ylabel('Price')
# axs[0].legend()

# Plot for the second stock (Microsoft)
axs[1].plot(data2.index, data2['Close'], label='MSFT Close Price', color='orange')
axs[1].axhline(y=250, color='red', linestyle='--', label='Level 1')
axs[1].axhline(y=300, color='green', linestyle='--', label='Level 2')
axs[1].set_title('Microsoft Stock Price')
# axs[1].set_xlabel('Date')
# axs[1].set_ylabel('Price')
# axs[1].legend()

# Adjust layout
plt.tight_layout()
plt.show()