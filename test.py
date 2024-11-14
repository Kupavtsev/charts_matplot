import yfinance as yf
import pandas as pd

# Define ticker symbol and time range
ticker = "AAPL"
data = yf.download(ticker, period="1y")

import matplotlib.pyplot as plt

# Plotting the closing prices
plt.plot(data.index, data['Close'], label='Close Price')

# Adding custom levels
plt.axhline(y=150, color='r', linestyle='--', label='Level 1')
plt.axhline(y=200, color='g', linestyle='--', label='Level 2')

plt.title('Price Chart with Custom Levels')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()




















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













import yfinance as yf
import matplotlib.pyplot as plt
import time
from db_connect import get_data

# Fetch historical data for two different stocks
ticker1 = "AAPL"  # Apple
ticker2 = "MSFT"  # Microsoft

# Function to update the plot
def update_plot():
    # Fetch data
    data1 = get_data()  # Assuming this fetches the latest BTC data
    data2 = yf.download(ticker2, start="2023-01-01", end="2024-01-01")

    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))

    # Plot for the first stock (BTC)
    axs[0].clear()  # Clear previous plot
    axs[0].plot(data1.index, data1[6], label='BTC Close Price', color='blue')
    axs[0].axhline(y=95100, color='red', linestyle='--', label='Level 1')
    axs[0].axhline(y=94300, color='green', linestyle='--', label='Level 2')
    axs[0].axhline(y=86600, color='red', linestyle='--', label='Level 3')
    axs[0].axhline(y=85000, color='green', linestyle='--', label='Level 4')
    axs[0].set_title('BTC Stock Price')
    axs[0].legend()

    # Plot for the second stock (Microsoft)
    axs[1].clear()  # Clear previous plot
    axs[1].plot(data2.index, data2['Close'], label='MSFT Close Price', color='orange')
    axs[1].axhline(y=250, color='red', linestyle='--', label='Level 1')
    axs[1].axhline(y=300, color='green', linestyle='--', label='Level 2')
    axs[1].set_title('Microsoft Stock Price')
    axs[1].legend()

    # Adjust layout and redraw
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)  # Pause to allow the plot to update

# Main loop to update the plot every 5 minutes
try:
    plt.ion()  # Turn on interactive mode
    while True:
        update_plot()
        time.sleep(300)  # Sleep for 5 minutes (300 seconds)
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Show the final plot












import yfinance as yf
import matplotlib.pyplot as plt
from apscheduler.schedulers.background import BackgroundScheduler
from db_connect import get_data

# Fetch historical data for two different stocks
ticker1 = "AAPL"  # Apple
ticker2 = "MSFT"  # Microsoft

# Function to update the plot
def update_plot():
    # Fetch data
    data1 = get_data()  # Assuming this fetches the latest BTC data
    data2 = yf.download(ticker2, start="2023-01-01", end="2024-01-01")

    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))

    # Plot for the first stock (BTC)
    axs[0].clear()  # Clear previous plot
    axs[0].plot(data1.index, data1[6], label='BTC Close Price', color='blue')
    axs[0].axhline(y=95100, color='red', linestyle='--', label='Level 1')
    axs[0].axhline(y=94300, color='green', linestyle='--', label='Level 2')
    axs[0].axhline(y=86600, color='red', linestyle='--', label='Level 3')
    axs[0].axhline(y=85000, color='green', linestyle='--', label='Level 4')
    axs[0].set_title('BTC Stock Price')
    axs[0].legend()

    # Plot for the second stock (Microsoft)
    axs[1].clear()  # Clear previous plot
    axs[1].plot(data2.index, data2['Close'], label='MSFT Close Price', color='orange')
    axs[1].axhline(y=250, color='red', linestyle='--', label='Level 1')
    axs[1].axhline(y=300, color='green', linestyle='--', label='Level 2')
    axs[1].set_title('Microsoft Stock Price')
    axs[1].legend()

    # Adjust layout and redraw
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)  # Pause to allow the plot to update

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(update_plot, 'interval', minutes=5)  # Schedule the update every 5 minutes

# Start the scheduler
scheduler.start()

# Initial plot
plt.ion()  # Turn on interactive mode
update_plot()  # Initial call to plot

try:
    plt.show()  # Show the plot
    while True:
        pass  # Keep the script running
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()  # Shut down the scheduler on exit
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Show the final plot





















import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
 
fig, ax = plt.subplots()
scatter = ax.scatter(np.random.rand(10), np.random.rand(10))
 
button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])
button = Button(button_ax, 'Add')
 
def add_point(event):
    new_point = np.random.rand(2)
    scatter.set_offsets(np.concatenate([scatter.get_offsets(), [new_point]]))
    plt.draw()
 
button.on_clicked(add_point)
 
plt.show()