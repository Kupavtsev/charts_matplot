import psycopg2
import pandas as pd
import os
import dotenv

dotenv.load_dotenv()

assets = {'BTCUSDT':4, 'ARKMUSDT':15}

def get_data(asset):
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
            f"SELECT id, session_date, start_of_candle, price_open, price_high, price_low, price_close, volume, symbol_id FROM public.get_data_five_minutes\
                WHERE symbol_id={assets[asset]} AND session_date = CURRENT_DATE;"
            )
        
        # Fetch all rows
        rows = cursor.fetchall()
        data =  pd.DataFrame(rows)
        # print(data)
        # for row in rows:
            # print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return data



class ConsLevels():
    
    cons_lev1 = None
    cons_lev2 = None
    cons_lev3 = None
    cons_lev4 = None

    def get_cons_levels(self, asset):
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
                FROM public.ysd_body_levels WHERE symbol='{asset}' AND session = CURRENT_DATE;"
                )
            
            # Fetch all rows
            rows = cursor.fetchall()
            data =  pd.DataFrame(rows)
            print(data)

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
btc.get_cons_levels('BTCUSDT')
arkm = ConsLevels()
arkm.get_cons_levels('ARKMUSDT')

if __name__ == '__main__':
#    get_cons_levels('BTCUSDT')
    ex = ConsLevels()
    ex.get_cons_levels('BTCUSDT')
    # print(ex)
    print(ex.cons_lev2)
    pass