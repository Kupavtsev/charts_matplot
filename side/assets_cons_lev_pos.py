from datetime import date, timedelta
import matplotlib.pyplot as plt
import asyncio

from db_connect import get_data,\
                       btc, arkm, ach, lpt, storj, wld, knc, lever, mkr, pendle, spell

# from assets import fig, axs
days = 0

btc.get_cons_levels('BTCUSDT', days)
arkm.get_cons_levels('ARKMUSDT', days)
ach.get_cons_levels('ACHUSDT', days)
lpt.get_cons_levels('LPTUSDT', days)

storj.get_cons_levels('STORJUSDT', days)
wld.get_cons_levels('WLDUSDT', days)
knc.get_cons_levels('KNCUSDT', days)

lever.get_cons_levels('LEVERUSDT', days)
mkr.get_cons_levels('MKRUSDT', days)
pendle.get_cons_levels('PENDLEUSDT', days)
spell.get_cons_levels('SPELLUSDT', days)

# Cons Levels
cons_levels = {
    'BTCUSDT': [btc.cons_lev1, btc.cons_lev2, btc.cons_lev3, btc.cons_lev4],
    'ACHUSDT': [ach.cons_lev1, ach.cons_lev2, ach.cons_lev3, ach.cons_lev4],
    'ARKMUSDT': [arkm.cons_lev1, arkm.cons_lev2, arkm.cons_lev3, arkm.cons_lev4],
    'LPTUSDT': [lpt.cons_lev1, lpt.cons_lev2, lpt.cons_lev3, lpt.cons_lev4],
    'STORJUSDT': [storj.cons_lev1, storj.cons_lev2, storj.cons_lev3, storj.cons_lev4],
    'WLDUSDT': [wld.cons_lev1, wld.cons_lev2, wld.cons_lev3, wld.cons_lev4],
    'KNCUSDT': [knc.cons_lev1, knc.cons_lev2, knc.cons_lev3, knc.cons_lev4],
    'LEVERUSDT': [lever.cons_lev1, lever.cons_lev2, lever.cons_lev3, lever.cons_lev4],
    'MKRUSDT': [mkr.cons_lev1, mkr.cons_lev2, mkr.cons_lev3, mkr.cons_lev4],
    'PENDLEUSDT': [pendle.cons_lev1, pendle.cons_lev2, pendle.cons_lev3, pendle.cons_lev4],
    'SPELLUSDT': [spell.cons_lev1, spell.cons_lev2, spell.cons_lev3, spell.cons_lev4],
}

# Create a figure and axis
fig, axs = plt.subplots(3, 4, figsize=(14, 5))

# Initialize the plot
def init2():
    axs[0][0].set_title('BTC')
    axs[0][1].set_title('ARKM')
    axs[0][2].set_title('ACH')
    axs[0][3].set_title('LPT')
    
    axs[1][0].set_title('STORJ')
    axs[1][1].set_title('WLD')
    axs[1][3].set_title('KNC')
    
    axs[2][0].set_title('LEVER')
    axs[2][1].set_title('MKR')
    axs[2][2].set_title('PENDLE')
    axs[2][3].set_title('SPELL')
    return axs

# Update function for animation
def update2(frame):
    # check with db_connect DAYS (line = 93)
    
    price_action_date = date.today() - timedelta(days=days)
    print(price_action_date)
    # Fetch data
    data1 = asyncio.run(get_data('BTCUSDT', days))
    data2 = asyncio.run(get_data('ARKMUSDT', days ))
    data3 = asyncio.run(get_data('ACHUSDT', days))
    data4 = asyncio.run(get_data('LPTUSDT', days))

    data5 = asyncio.run(get_data('STORJUSDT', days))
    data6 = asyncio.run(get_data('WLDUSDT', days))
    data8 = asyncio.run(get_data('KNCUSDT', days))

    data9 = asyncio.run(get_data('LEVERUSDT', days))
    data10 = asyncio.run(get_data('MKRUSDT', days))
    data11 = asyncio.run(get_data('PENDLEUSDT', days))
    data12 = asyncio.run(get_data('SPELLUSDT', days))
    

    # Clear previous data
    axs[0][0].cla()
    axs[0][1].cla()
    axs[0][2].cla()
    axs[0][3].cla()

    axs[1][0].cla()
    axs[1][1].cla()
    axs[1][2].cla()
    axs[1][3].cla()

    axs[2][0].cla()
    axs[2][1].cla()
    axs[2][2].cla()
    axs[2][3].cla()

    # Plot for BTC
    axs[0][0].plot(data1.index, data1[6], label='BTC', color='blue')
    axs[0][0].axhline(y=cons_levels['BTCUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[0][0].axhline(y=cons_levels['BTCUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[0][0].axhline(y=cons_levels['BTCUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[0][0].axhline(y=cons_levels['BTCUSDT'][3], color='green', linestyle='--', label='Level 4')
    # axs[0].legend()

    # Plot for ARKM
    axs[0][1].plot(data2.index, data2[6], label='arkm', color='orange')
    axs[0][1].axhline(y=cons_levels['ARKMUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[0][1].axhline(y=cons_levels['ARKMUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[0][1].axhline(y=cons_levels['ARKMUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[0][1].axhline(y=cons_levels['ARKMUSDT'][3], color='green', linestyle='--', label='Level 4')
    # axs[1].legend()

    axs[0][2].plot(data3.index, data3[6], label='ach', color='orange')
    axs[0][2].axhline(y=cons_levels['ACHUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[0][2].axhline(y=cons_levels['ACHUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[0][2].axhline(y=cons_levels['ACHUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[0][2].axhline(y=cons_levels['ACHUSDT'][3], color='green', linestyle='--', label='Level 4')
    
    axs[0][3].plot(data4.index, data4[6], label='lpt', color='orange')
    axs[0][3].axhline(y=cons_levels['LPTUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[0][3].axhline(y=cons_levels['LPTUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[0][3].axhline(y=cons_levels['LPTUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[0][3].axhline(y=cons_levels['LPTUSDT'][3], color='green', linestyle='--', label='Level 4')
    
    
    
    axs[1][0].plot(data5.index, data5[6], label='storj', color='orange')
    axs[1][0].axhline(y=cons_levels['STORJUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[1][0].axhline(y=cons_levels['STORJUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[1][0].axhline(y=cons_levels['STORJUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[1][0].axhline(y=cons_levels['STORJUSDT'][3], color='green', linestyle='--', label='Level 4')
    
    axs[1][1].plot(data6.index, data6[6], label='wld', color='orange')
    axs[1][1].axhline(y=cons_levels['WLDUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[1][1].axhline(y=cons_levels['WLDUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[1][1].axhline(y=cons_levels['WLDUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[1][1].axhline(y=cons_levels['WLDUSDT'][3], color='green', linestyle='--', label='Level 4')
   
    # axs[1][2].plot(data7.index, data7[6], label='lpt', color='green')
    # axs[1][2].axhline(y=cons_levels['AMBUSDT'][0], color='red', linestyle='--', label='Level 1')
    # axs[1][2].axhline(y=cons_levels['AMBUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[1][2].axhline(y=cons_levels['AMBUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[1][2].axhline(y=cons_levels['AMBUSDT'][3], color='green', linestyle='--', label='Level 4')
    
    axs[1][3].plot(data8.index, data8[6], label='knc', color='green')
    axs[1][3].axhline(y=cons_levels['KNCUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[1][3].axhline(y=cons_levels['KNCUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[1][3].axhline(y=cons_levels['KNCUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[1][3].axhline(y=cons_levels['KNCUSDT'][3], color='green', linestyle='--', label='Level 4')


    axs[2][0].plot(data9.index, data9[6], label='lever', color='green')
    axs[2][0].axhline(y=cons_levels['LEVERUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[2][0].axhline(y=cons_levels['LEVERUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[2][0].axhline(y=cons_levels['LEVERUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[2][0].axhline(y=cons_levels['LEVERUSDT'][3], color='green', linestyle='--', label='Level 4')
    
    axs[2][1].plot(data10.index, data10[6], label='mkr', color='green')
    axs[2][1].axhline(y=cons_levels['MKRUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[2][1].axhline(y=cons_levels['MKRUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[2][1].axhline(y=cons_levels['MKRUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[2][1].axhline(y=cons_levels['MKRUSDT'][3], color='green', linestyle='--', label='Level 4')
    
    axs[2][2].plot(data11.index, data11[6], label='pendle', color='green')
    axs[2][2].axhline(y=cons_levels['PENDLEUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[2][2].axhline(y=cons_levels['PENDLEUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[2][2].axhline(y=cons_levels['PENDLEUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[2][2].axhline(y=cons_levels['PENDLEUSDT'][3], color='green', linestyle='--', label='Level 4')
    
    axs[2][3].plot(data12.index, data12[6], label='spell', color='green')
    axs[2][3].axhline(y=cons_levels['SPELLUSDT'][0], color='red', linestyle='--', label='Level 1')
    axs[2][3].axhline(y=cons_levels['SPELLUSDT'][1], color='green', linestyle='--', label='Level 2')
    # axs[2][3].axhline(y=cons_levels['SPELLUSDT'][2], color='red', linestyle='--', label='Level 3')
    # axs[2][3].axhline(y=cons_levels['SPELLUSDT'][3], color='green', linestyle='--', label='Level 4')

    # Set titles
    axs[0][0].set_title('BTC')
    axs[0][1].set_title('ARKM')
    axs[0][2].set_title('ACH')
    axs[0][3].set_title('LPT')
    
    axs[1][0].set_title('STORJ')
    axs[1][1].set_title('WLD')
    axs[1][3].set_title('KNC')
    
    axs[2][0].set_title('LEVER')
    axs[2][1].set_title('MKR')
    axs[2][2].set_title('PENDLE')
    axs[2][3].set_title('SPELL')

