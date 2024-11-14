import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import yfinance as yf
import time

from db_connect import get_data, btc, arkm


# Cons Levels


cons_levels = {
    'BTCUSDT': [btc.cons_lev1, btc.cons_lev2, btc.cons_lev3, btc.cons_lev4],
    'ARKMUSDT': [arkm.cons_lev1, arkm.cons_lev2, arkm.cons_lev3, arkm.cons_lev4],
}

# Create a figure and axis
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Initialize the plot
def init():
    axs[0].set_title('BTC')
    axs[1].set_title('ARKM')
    return axs

# Update function for animation
def update(frame):
    # Fetch data
    data1 = get_data('BTCUSDT')
    data2 = get_data('ARKMUSDT')

    # Clear previous data
    axs[0].cla()
    axs[1].cla()

    # Plot for Apple
    axs[0].plot(data1.index, data1[6], label='BTC', color='blue')
    axs[0].axhline(y=cons_levels['BTCUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[0].axhline(y=cons_levels['BTCUSDT'][1], color='green', linestyle='--', label='Level 2')
    axs[0].axhline(y=cons_levels['BTCUSDT'][2], color='red', linestyle='--', label='Level 3')
    axs[0].axhline(y=cons_levels['BTCUSDT'][3], color='green', linestyle='--', label='Level 4')
    # axs[0].axhline(y=1.91, color='red', linestyle='--', label='Level 1')
    # axs[0].legend()

    # Plot for Microsoft
    axs[1].plot(data2.index, data2[6], label='arkm', color='orange')
    axs[1].axhline(y=cons_levels['ARKMUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[1].axhline(y=cons_levels['ARKMUSDT'][1], color='green', linestyle='--', label='Level 2')
    axs[1].axhline(y=cons_levels['ARKMUSDT'][2], color='red', linestyle='--', label='Level 3')
    axs[1].axhline(y=cons_levels['ARKMUSDT'][3], color='green', linestyle='--', label='Level 4')
    # axs[1].axhline(y=250, color='green', linestyle='--', label='Level 1')
    # axs[1].legend()

    # Set titles
    axs[0].set_title('BTC')
    axs[1].set_title('ARKM')

# Create the animation
anim = FuncAnimation(fig, update, init_func=init, frames=np.arange(0, 100), interval=60000)  # 300000 ms = 5 minutes

# Show the plot
plt.tight_layout()
plt.show()