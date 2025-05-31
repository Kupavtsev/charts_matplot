from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np
import asyncio

from db_connect import ConsLevels, get_data,\
                       btc, arkm, ach, lpt, storj, wld, knc, lever, mkr, pendle, spell
from utitlities import days_until_date

fig, axs = plt.subplots(3, 4, figsize=(14, 5))


asset :str = 'PENDLEUSDT'
asset_id :int = 14


'''
get this dates from txt or py file
just read a string number with date
each date on a new string
which will be ganerated in statistics charts_django
'''
# '%Y-%m-%d'
date_price = {
    0  : days_until_date('2025-05-01'),
    1 : days_until_date('2025-04-30'),
    2 : days_until_date('2025-04-29'),
    3 : days_until_date('2025-04-28'),
    10 : days_until_date('2025-04-27'),
    11 : days_until_date('2025-04-26'),
    12 : days_until_date('2025-04-25'),
    13 : days_until_date('2025-04-25'),
    20 : days_until_date('2025-04-25'),
    21 : days_until_date('2025-04-25'),
    22 : days_until_date('2025-04-25'),
    23 : days_until_date('2025-04-25'),
}


# days = 6

price_action_date_str0 = (date.today() - timedelta(days=date_price[0])).strftime('%Y-%m-%d')
price_action_date_str01 = (date.today() - timedelta(days=date_price[1])).strftime('%Y-%m-%d')
price_action_date_str02 = (date.today() - timedelta(days=date_price[2])).strftime('%Y-%m-%d')
price_action_date_str03 = (date.today() - timedelta(days=date_price[3])).strftime('%Y-%m-%d')
price_action_date_str10 = (date.today() - timedelta(days=date_price[10])).strftime('%Y-%m-%d')
price_action_date_str11 = (date.today() - timedelta(days=date_price[11])).strftime('%Y-%m-%d')
price_action_date_str12 = (date.today() - timedelta(days=date_price[12])).strftime('%Y-%m-%d')
price_action_date_str13 = (date.today() - timedelta(days=date_price[13])).strftime('%Y-%m-%d')
price_action_date_str20 = (date.today() - timedelta(days=date_price[20])).strftime('%Y-%m-%d')
price_action_date_str21 = (date.today() - timedelta(days=date_price[21])).strftime('%Y-%m-%d')
price_action_date_str22 = (date.today() - timedelta(days=date_price[22])).strftime('%Y-%m-%d')
price_action_date_str23 = (date.today() - timedelta(days=date_price[23])).strftime('%Y-%m-%d')


asset0 = ConsLevels()
asset0.get_cons_levels(asset, days=date_price[0])
asset01 = ConsLevels()
asset01.get_cons_levels(asset, days=date_price[1])
asset02 = ConsLevels()
asset02.get_cons_levels(asset, days=date_price[2])
asset03 = ConsLevels()
asset03.get_cons_levels(asset, days=date_price[3])

asset10 = ConsLevels()
asset10.get_cons_levels(asset, days=date_price[10])
asset11 = ConsLevels()
asset11.get_cons_levels(asset, days=date_price[11])
asset12 = ConsLevels()
asset12.get_cons_levels(asset, days=date_price[12])
asset13 = ConsLevels()
asset13.get_cons_levels(asset, days=date_price[13])

asset20 = ConsLevels()
asset20.get_cons_levels(asset, days=date_price[20])
asset21 = ConsLevels()
asset21.get_cons_levels(asset, days=date_price[21])
asset22 = ConsLevels()
asset22.get_cons_levels(asset, days=date_price[22])
asset23 = ConsLevels()
asset23.get_cons_levels(asset, days=date_price[23])


# Fetch price data
data1 = asyncio.run(get_data(asset, date_price[0]))
data2 = asyncio.run(get_data(asset, date_price[1]))
data3 = asyncio.run(get_data(asset, date_price[2]))
data4 = asyncio.run(get_data(asset, date_price[3]))

data5 = asyncio.run(get_data(asset, date_price[10]))
data6 = asyncio.run(get_data(asset, date_price[11]))
data7 = asyncio.run(get_data(asset, date_price[12]))
data8 = asyncio.run(get_data(asset, date_price[13]))

data9 = asyncio.run(get_data(asset, date_price[20]))
data10 = asyncio.run(get_data(asset, date_price[21]))
data11 = asyncio.run(get_data(asset, date_price[22]))
data12 = asyncio.run(get_data(asset, date_price[23]))



# Plot for BTC
axs[0][0].plot(data1.index, data1[6], label=price_action_date_str0, color='blue')
axs[0][0].axhline(y=asset0.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[0][0].axhline(y=asset0.cons_lev2, color='green', linestyle='--', label='Level 2')
axs[0][0].axhline(y=asset0.cons_lev3, color='red', linestyle='--', label='Level 3')
axs[0][0].axhline(y=asset0.cons_lev4, color='green', linestyle='--', label='Level 4')
# axs[0].legend()

# Plot for ARKM
axs[0][1].plot(data2.index, data2[6], label=price_action_date_str01, color='orange')
axs[0][1].axhline(y=asset01.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[0][1].axhline(y=asset01.cons_lev2, color='green', linestyle='--', label='Level 2')
axs[0][1].axhline(y=asset01.cons_lev3, color='red', linestyle='--', label='Level 3')
axs[0][1].axhline(y=asset01.cons_lev4, color='green', linestyle='--', label='Level 4')
# axs[1].legend()

axs[0][2].plot(data3.index, data3[6], label=price_action_date_str02, color='orange')
axs[0][2].axhline(y=asset02.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[0][2].axhline(y=asset02.cons_lev2, color='green', linestyle='--', label='Level 2')
axs[0][2].axhline(y=asset02.cons_lev3, color='red', linestyle='--', label='Level 3')
axs[0][2].axhline(y=asset02.cons_lev4, color='green', linestyle='--', label='Level 4')

axs[0][3].plot(data4.index, data4[6], label=price_action_date_str03, color='orange')
axs[0][3].axhline(y=asset03.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[0][3].axhline(y=asset03.cons_lev2, color='green', linestyle='--', label='Level 2')
axs[0][3].axhline(y=asset03.cons_lev3, color='red', linestyle='--', label='Level 3')
axs[0][3].axhline(y=asset03.cons_lev4, color='green', linestyle='--', label='Level 4')



axs[1][0].plot(data5.index, data5[6], label=price_action_date_str10, color='orange')
axs[1][0].axhline(y=asset10.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[1][0].axhline(y=asset10.cons_lev2, color='green', linestyle='--', label='Level 2')
axs[1][0].axhline(y=asset10.cons_lev3, color='red', linestyle='--', label='Level 3')
axs[1][0].axhline(y=asset10.cons_lev4, color='green', linestyle='--', label='Level 4')

axs[1][1].plot(data6.index, data6[6], label=price_action_date_str11, color='orange')
axs[1][1].axhline(y=asset11.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[1][1].axhline(y=asset11.cons_lev2, color='green', linestyle='--', label='Level 2')
axs[1][1].axhline(y=asset11.cons_lev3, color='red', linestyle='--', label='Level 3')
axs[1][1].axhline(y=asset11.cons_lev4, color='green', linestyle='--', label='Level 4')

axs[1][2].plot(data7.index, data7[6], label=price_action_date_str12, color='green')
axs[1][2].axhline(y=asset12.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[1][2].axhline(y=asset12.cons_lev2, color='green', linestyle='--', label='Level 2')
axs[1][2].axhline(y=asset12.cons_lev3, color='red', linestyle='--', label='Level 3')
axs[1][2].axhline(y=asset12.cons_lev4, color='green', linestyle='--', label='Level 4')

axs[1][3].plot(data8.index, data8[6], label=price_action_date_str13, color='green')
axs[1][3].axhline(y=asset13.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[1][3].axhline(y=asset13.cons_lev2, color='green', linestyle='--', label='Level 2')
# axs[1][3].axhline(y=asset13.cons_levels3, color='red', linestyle='--', label='Level 3')
# axs[1][3].axhline(y=asset13.cons_levels4, color='green', linestyle='--', label='Level 4')


axs[2][0].plot(data9.index, data9[6], label=price_action_date_str20, color='green')
axs[2][0].axhline(y=asset20.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[2][0].axhline(y=asset20.cons_lev2, color='green', linestyle='--', label='Level 2')
# axs[2][0].axhline(y=asset20.cons_levels3, color='red', linestyle='--', label='Level 3')
# axs[2][0].axhline(y=asset20.cons_levels4, color='green', linestyle='--', label='Level 4')

axs[2][1].plot(data10.index, data10[6], label=price_action_date_str21, color='green')
axs[2][1].axhline(y=asset21.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[2][1].axhline(y=asset21.cons_lev2, color='green', linestyle='--', label='Level 2')
# axs[2][1].axhline(y=asset21.cons_levels3, color='red', linestyle='--', label='Level 3')
# axs[2][1].axhline(y=asset21.cons_levels4, color='green', linestyle='--', label='Level 4')

axs[2][2].plot(data11.index, data11[6], label=price_action_date_str22, color='green')
axs[2][2].axhline(y=asset22.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[2][2].axhline(y=asset22.cons_lev2, color='green', linestyle='--', label='Level 2')
# # axs[2][2].axhline(y=cons_levels[asset][pendle.cons_lev3], color='red', linestyle='--', label='Level 3')
# # axs[2][2].axhline(y=cons_levels[asset][pendle.cons_lev4], color='green', linestyle='--', label='Level 4')

axs[2][3].plot(data12.index, data12[6], label=price_action_date_str23, color='green')
axs[2][3].axhline(y=asset23.cons_lev1, color='red', linestyle='--', label='Level 1')
axs[2][3].axhline(y=asset23.cons_lev2, color='green', linestyle='--', label='Level 2')
# axs[2][3].axhline(y=cons_levels[asset][2], color='red', linestyle='--', label='Level 3')
# axs[2][3].axhline(y=cons_levels[asset][3], color='green', linestyle='--', label='Level 4')

# Set titles
axs[0][0].set_title(price_action_date_str0)
axs[0][1].set_title(price_action_date_str01)
axs[0][2].set_title(price_action_date_str02)
axs[0][3].set_title(price_action_date_str03)

axs[1][0].set_title(price_action_date_str10)
axs[1][1].set_title(price_action_date_str11)
axs[1][2].set_title(price_action_date_str12)
axs[1][3].set_title(price_action_date_str13)

axs[2][0].set_title(price_action_date_str20)
axs[2][1].set_title(price_action_date_str21)
axs[2][2].set_title(price_action_date_str22)
axs[2][3].set_title(price_action_date_str23)





plt.tight_layout()
plt.show()