import psycopg2
import pandas as pd
import os
import dotenv
import asyncio
import asyncpg

dotenv.load_dotenv()

assets = {'ACHUSDT':1, 'BTCUSDT':4, 'ARKMUSDT':15, 'LPTUSDT':3,'STORJUSDT':6,'WLDUSDT':7, 'AMBUSDT':12, 'KNCUSDT':9, 'LEVERUSDT':10, 'MKRUSDT':8, 'PENDLEUSDT':14, 'SPELLUSDT':13}

async def get_data(asset, days :int):
    
    conn = await asyncpg.connect(
        database=os.getenv('database'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        host=os.getenv('host'),
        port=os.getenv('port')
    )

    try:
        query = f"SELECT id, session_date, start_of_candle, price_open, price_high, price_low, price_close, volume, symbol_id FROM public.get_data_five_minutes\
                WHERE symbol_id={assets[asset]} AND session_date = CURRENT_DATE - {days};"

        rows = await conn.fetch(query)
        data = pd.DataFrame(rows)
        

        # Step 1: Convert column index 2 to datetime
        data[2] = pd.to_datetime(data[2])

        # Step 2: Sort the DataFrame by the values in column index 2
        sorted_df = data.sort_values(by=2)

        # Step 3: Reset the index to reflect the new order
        sorted_df.reset_index(drop=True, inplace=True)

        if len(sorted_df) >0 : print('15M DF query OK!')

        return sorted_df

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            await conn.close()


class ConsLevels():
    
    cons_lev1 = None
    cons_lev2 = None
    cons_lev3 = None
    cons_lev4 = None

    def get_cons_levels(self, asset :str, days :int = 0):
        try:
            conn = psycopg2.connect(
                database=os.getenv('database'),
                user=os.getenv('user'),
                password=os.getenv('password'),
                host=os.getenv('host'),
                port=os.getenv('port')
            )
            cursor = conn.cursor()
            cursor.execute(
                # "SELECT id, session_date, start_of_candle, price_open, price_high, price_low, price_close, volume, ma7, ma14, ma28, symbol_id FROM public.get_data_five_minutes;"
                f"SELECT id, symbol, session, cons_ysd_body_levels, cons_ysd_body_levels_neg, cons_ysd_body_levels_tr100, cons_ysd_body_levels_tr100_neg, series_neg, series_pos\
                FROM public.ysd_body_levels WHERE symbol='{asset}' AND session = CURRENT_DATE - {days};"
                )
            
            # Fetch all rows
            rows = cursor.fetchall()
            data =  pd.DataFrame(rows)
            if len(data) > 0: print('Levels DF query OK!')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        self.cons_lev1 = data.iloc[0, 3]
        self.cons_lev2 = data.iloc[0, 5]
        self.cons_lev3 = data.iloc[0, 4]
        self.cons_lev4 = data.iloc[0, 6]


btc = ConsLevels()
arkm = ConsLevels()
ach = ConsLevels()
lpt = ConsLevels()


storj = ConsLevels()
wld = ConsLevels()
amb = ConsLevels()
knc = ConsLevels()

lever = ConsLevels()
mkr = ConsLevels()
pendle = ConsLevels()
spell = ConsLevels()


if __name__ == '__main__':
    ex = ConsLevels()
    ex.get_cons_levels('BTCUSDT')
    # print(ex.cons_lev2)
    pass