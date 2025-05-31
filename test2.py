import pandas as pd
import mplfinance as mpf
from io import StringIO

# Raw data as provided, including volume
data = """
2024-10-14;4.0628;4.4696;3.9886;4.3544;14435426.0
2024-10-15;4.3549;4.455;4.0502;4.2343;14644822.0
2024-10-16;4.2346;4.4046;4.16;4.2302;12703961.0
2024-10-17;4.2289;4.3391;4.0577;4.1949;10420358.0
2024-10-18;4.1947;4.5595;4.1288;4.5567;10308825.0
2024-10-19;4.5575;4.9405;4.4657;4.8556;21764855.0
2024-10-20;4.8556;5.0577;4.6673;5.0315;15019306.0
2024-10-21;5.0315;5.1375;4.7061;4.796;14279205.0
2024-10-22;4.7945;4.902;4.7;4.8758;10314090.0
2024-10-23;4.8763;4.98;4.4883;4.6839;13503568.0
2024-10-24;4.6841;5.1295;4.6181;4.9282;18960590.0
2024-10-25;4.9287;4.9321;4.0773;4.3713;19091625.0
2024-10-26;4.3722;4.5898;4.2795;4.5043;10374993.0
2024-10-27;4.5044;4.5903;4.4562;4.5069;5569659.0
2024-10-28;4.507;4.6539;4.3116;4.6052;10374452.0
"""

# Load the data into dataframe
df = pd.read_csv(StringIO(data), sep=';', header=None, names=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

# Define the price level to plot
level = 4.5

# Create a horizontal line across the full index range at price level using addplot
ap0 = mpf.make_addplot([level]*len(df), color='purple', linestyle='--', width=1.5)

# Plot candlestick with volume and the horizontal line
mpf.plot(
    df,
    type='candle',
    style='charles',
    title='Candlestick Chart with Volume and Price Level',
    ylabel='Price',
    volume=True,
    addplot=ap0
)
