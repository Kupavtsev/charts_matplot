from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np
import asyncio

from db_connect import get_data,\
                       btc, arkm, ach, lpt, storj, wld, amb, knc, lever, mkr, pendle, spell
from utitlities import days_until_date

fig, axs = plt.subplots(3, 4, figsize=(14, 5))


asset :str = 'PENDLEUSDT'
asset_id :int = 14

# Cons Levels
'''
also shoud get data from date_price dict
'''
cons_levels = {
    'BTCUSDT': [btc.cons_lev1, btc.cons_lev2, btc.cons_lev3, btc.cons_lev4],
    'ACHUSDT': [ach.cons_lev1, ach.cons_lev2, ach.cons_lev3, ach.cons_lev4],
    'ARKMUSDT': [arkm.cons_lev1, arkm.cons_lev2, arkm.cons_lev3, arkm.cons_lev4],
    'LPTUSDT': [lpt.cons_lev1, lpt.cons_lev2, lpt.cons_lev3, lpt.cons_lev4],
    'STORJUSDT': [storj.cons_lev1, storj.cons_lev2, storj.cons_lev3, storj.cons_lev4],
    'WLDUSDT': [wld.cons_lev1, wld.cons_lev2, wld.cons_lev3, wld.cons_lev4],
    'AMBUSDT': [amb.cons_lev1, amb.cons_lev2, amb.cons_lev3, amb.cons_lev4],
    'KNCUSDT': [knc.cons_lev1, knc.cons_lev2, knc.cons_lev3, knc.cons_lev4],
    'LEVERUSDT': [lever.cons_lev1, lever.cons_lev2, lever.cons_lev3, lever.cons_lev4],
    'MKRUSDT': [mkr.cons_lev1, mkr.cons_lev2, mkr.cons_lev3, mkr.cons_lev4],
    # asset: [pendle.cons_lev1, pendle.cons_lev2, pendle.cons_lev3, pendle.cons_lev4],
    asset: pendle,
    'SPELLUSDT': [spell.cons_lev1, spell.cons_lev2, spell.cons_lev3, spell.cons_lev4],
}


'''
get this dates from txt or py file
which will be ganerated in statistics charts_django
'''
# '%Y-%m-%d'
date_price = {
    '2024-12-06' : days_until_date('2024-12-06')
}

print(date_price['2024-12-06'])

days = 0
price_action_date = date.today() - timedelta(days=days)
levels_date = date.today() - timedelta(days=0)
price_action_date_str = 'BTC p/l' + price_action_date.strftime('%Y-%m-%d') + ' / ' + levels_date.strftime('%Y-%m-%d')
print(price_action_date_str)


# Fetch price data
data1 = asyncio.run(get_data('BTCUSDT', days))
data2 = asyncio.run(get_data('ARKMUSDT', days))
data3 = asyncio.run(get_data('ACHUSDT', days))
data4 = asyncio.run(get_data('LPTUSDT', days))

data5 = asyncio.run(get_data('STORJUSDT', days))
data6 = asyncio.run(get_data('WLDUSDT', days))
data7 = asyncio.run(get_data('AMBUSDT', days))
data8 = asyncio.run(get_data('KNCUSDT', days))

data9 = asyncio.run(get_data('LEVERUSDT', days))
data10 = asyncio.run(get_data('MKRUSDT', days))
data11 = asyncio.run(get_data(asset, date_price['2024-12-06']))
data12 = asyncio.run(get_data(asset, days))



# Plot for BTC
axs[0][0].plot(data1.index, data1[6], label=price_action_date_str, color='blue')
axs[0][0].axhline(y=cons_levels['BTCUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[0][0].axhline(y=cons_levels['BTCUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[0][0].axhline(y=cons_levels['BTCUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[0][0].axhline(y=cons_levels['BTCUSDT'][3], color='green', linestyle='--', label='Level 4')
# axs[0].legend()

# Plot for ARKM
axs[0][1].plot(data2.index, data2[6], label='arkm', color='orange')
axs[0][1].axhline(y=cons_levels['ARKMUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[0][1].axhline(y=cons_levels['ARKMUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[0][1].axhline(y=cons_levels['ARKMUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[0][1].axhline(y=cons_levels['ARKMUSDT'][3], color='green', linestyle='--', label='Level 4')
# axs[1].legend()

axs[0][2].plot(data3.index, data3[6], label='ach', color='orange')
axs[0][2].axhline(y=cons_levels['ACHUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[0][2].axhline(y=cons_levels['ACHUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[0][2].axhline(y=cons_levels['ACHUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[0][2].axhline(y=cons_levels['ACHUSDT'][3], color='green', linestyle='--', label='Level 4')

axs[0][3].plot(data4.index, data4[6], label='lpt', color='orange')
axs[0][3].axhline(y=cons_levels['LPTUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[0][3].axhline(y=cons_levels['LPTUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[0][3].axhline(y=cons_levels['LPTUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[0][3].axhline(y=cons_levels['LPTUSDT'][3], color='green', linestyle='--', label='Level 4')



axs[1][0].plot(data5.index, data5[6], label='lpt', color='orange')
axs[1][0].axhline(y=cons_levels['STORJUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[1][0].axhline(y=cons_levels['STORJUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[1][0].axhline(y=cons_levels['STORJUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[1][0].axhline(y=cons_levels['STORJUSDT'][3], color='green', linestyle='--', label='Level 4')

axs[1][1].plot(data6.index, data6[6], label='lpt', color='orange')
axs[1][1].axhline(y=cons_levels['WLDUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[1][1].axhline(y=cons_levels['WLDUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[1][1].axhline(y=cons_levels['WLDUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[1][1].axhline(y=cons_levels['WLDUSDT'][3], color='green', linestyle='--', label='Level 4')

axs[1][2].plot(data7.index, data7[6], label='lpt', color='green')
axs[1][2].axhline(y=cons_levels['AMBUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[1][2].axhline(y=cons_levels['AMBUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[1][2].axhline(y=cons_levels['AMBUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[1][2].axhline(y=cons_levels['AMBUSDT'][3], color='green', linestyle='--', label='Level 4')

axs[1][3].plot(data8.index, data8[6], label='lpt', color='green')
axs[1][3].axhline(y=cons_levels['KNCUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[1][3].axhline(y=cons_levels['KNCUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[1][3].axhline(y=cons_levels['KNCUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[1][3].axhline(y=cons_levels['KNCUSDT'][3], color='green', linestyle='--', label='Level 4')


axs[2][0].plot(data9.index, data9[6], label='lpt', color='green')
axs[2][0].axhline(y=cons_levels['LEVERUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[2][0].axhline(y=cons_levels['LEVERUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[2][0].axhline(y=cons_levels['LEVERUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[2][0].axhline(y=cons_levels['LEVERUSDT'][3], color='green', linestyle='--', label='Level 4')

axs[2][1].plot(data10.index, data10[6], label='lpt', color='green')
axs[2][1].axhline(y=cons_levels['MKRUSDT'][0], color='red', linestyle='--', label='Level 1')
axs[2][1].axhline(y=cons_levels['MKRUSDT'][1], color='green', linestyle='--', label='Level 2')
axs[2][1].axhline(y=cons_levels['MKRUSDT'][2], color='red', linestyle='--', label='Level 3')
axs[2][1].axhline(y=cons_levels['MKRUSDT'][3], color='green', linestyle='--', label='Level 4')

axs[2][2].plot(data11.index, data11[6], label='lpt', color='green')
axs[2][2].axhline(y=cons_levels[asset].cons_lev1, color='red', linestyle='--', label='Level 1')
axs[2][2].axhline(y=cons_levels[asset].cons_lev2, color='green', linestyle='--', label='Level 2')
# # axs[2][2].axhline(y=cons_levels[asset][pendle.cons_lev3], color='red', linestyle='--', label='Level 3')
# # axs[2][2].axhline(y=cons_levels[asset][pendle.cons_lev4], color='green', linestyle='--', label='Level 4')

axs[2][3].plot(data12.index, data12[6], label='lpt', color='green')
axs[2][3].axhline(y=cons_levels[asset].cons_lev1, color='red', linestyle='--', label='Level 1')
axs[2][3].axhline(y=cons_levels[asset].cons_lev2, color='green', linestyle='--', label='Level 2')
# axs[2][3].axhline(y=cons_levels[asset][2], color='red', linestyle='--', label='Level 3')
# axs[2][3].axhline(y=cons_levels[asset][3], color='green', linestyle='--', label='Level 4')

# Set titles
axs[0][0].set_title(price_action_date_str)
axs[0][1].set_title('ARKM')
axs[0][2].set_title('ACH')
axs[0][3].set_title('LPT')

axs[1][0].set_title('STORJ')
axs[1][1].set_title('WLD')
axs[1][2].set_title('AMB')
axs[1][3].set_title('KNC')

axs[2][0].set_title('LEVER')
axs[2][1].set_title('MKR')
axs[2][2].set_title(asset)
axs[2][3].set_title(asset)





plt.tight_layout()
plt.show()