
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

import numpy as np

# from side.assets_cons_lev_pos import fig, init2, update2
from side.assets_cons_lev_neg import fig, init2, update2

'''
Choise to show posi or neg ysd levels only.
'''


# button_ax = plt.axes([0.7, 0.002, 0.05, 0.04])
# button = Button(button_ax, 'Test')

# Create the animation
anim = FuncAnimation(fig, update2, init_func=init2, frames=np.arange(0, 100), interval=300000)  # 300000 ms = 5 minutes

# def test(event):
    # print('Test!')

# button.on_clicked(test)

# Show the plot
plt.tight_layout()
# plt.savefig('fig.png',bbox_inches='tight')
plt.show()