import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import yfinance as yf
import time
import asyncio

from db_connect import get_data, btc, arkm, ach


# Cons Levels
cons_levels = {
    'BTCUSDT': [btc.cons_lev1, btc.cons_lev2, btc.cons_lev3, btc.cons_lev4],
    'ARKMUSDT': [arkm.cons_lev1, arkm.cons_lev2, arkm.cons_lev3, arkm.cons_lev4],
    'ACHUSDT': [ach.cons_lev1, ach.cons_lev2, ach.cons_lev3, ach.cons_lev4],
}

# Create a figure and axis
fig, axs = plt.subplots(1, 3, figsize=(14, 5))

# Initialize the plot
def init():
    axs[0].set_title('BTC')
    axs[1].set_title('ARKM')
    axs[2].set_title('ACH')
    return axs

# Update function for animation
def update(frame):
    # Fetch data
    data1 = asyncio.run(get_data('BTCUSDT'))
    data2 = asyncio.run(get_data('ARKMUSDT'))
    data3 = asyncio.run(get_data('ACHUSDT'))
    

    # Clear previous data
    axs[0].cla()
    axs[1].cla()
    axs[2].cla()

    # Plot for BTC
    axs[0].plot(data1.index, data1[6], label='BTC', color='blue')
    axs[0].axhline(y=cons_levels['BTCUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[0].axhline(y=cons_levels['BTCUSDT'][1], color='green', linestyle='--', label='Level 2')
    axs[0].axhline(y=cons_levels['BTCUSDT'][2], color='red', linestyle='--', label='Level 3')
    axs[0].axhline(y=cons_levels['BTCUSDT'][3], color='green', linestyle='--', label='Level 4')
    # axs[0].legend()

    # Plot for ARKM
    axs[1].plot(data2.index, data2[6], label='arkm', color='orange')
    axs[1].axhline(y=cons_levels['ARKMUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[1].axhline(y=cons_levels['ARKMUSDT'][1], color='green', linestyle='--', label='Level 2')
    axs[1].axhline(y=cons_levels['ARKMUSDT'][2], color='red', linestyle='--', label='Level 3')
    axs[1].axhline(y=cons_levels['ARKMUSDT'][3], color='green', linestyle='--', label='Level 4')
    # axs[1].legend()

    axs[2].plot(data3.index, data3[6], label='ach', color='orange')
    axs[2].axhline(y=cons_levels['ACHUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[2].axhline(y=cons_levels['ACHUSDT'][1], color='green', linestyle='--', label='Level 2')
    axs[2].axhline(y=cons_levels['ACHUSDT'][2], color='red', linestyle='--', label='Level 3')
    axs[2].axhline(y=cons_levels['ACHUSDT'][3], color='green', linestyle='--', label='Level 4')

    # Set titles
    axs[0].set_title('BTC')
    axs[1].set_title('ARKM')
    axs[2].set_title('ACH')

# Create the animation
anim = FuncAnimation(fig, update, init_func=init, frames=np.arange(0, 100), interval=10000)  # 300000 ms = 5 minutes

# Show the plot
plt.tight_layout()
plt.show()