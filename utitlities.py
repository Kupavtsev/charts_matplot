from datetime import datetime, timedelta
import functools
from dateutil.tz import tzutc

arred = lambda x,n : x*(10**n)//1/(10**n)

def digits_after_comma_func(symbol, price) -> int:
    # if symbol == 'BTCUSDT': return 0
    return len(str(price).split('.')[1])

def catch_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Capture the local variables at the time of the exception
            local_vars = {**kwargs}  # Start with keyword arguments
            local_vars.update({f'arg{i}': arg for i, arg in enumerate(args)})  # Add positional arguments
            
            # Log the error with variable information
            print(f"An error occurred in function '{func.__name__}': {e}")
            print(f"Local variables: {local_vars}")
            with open('errors/catch_errors.txt', 'a') as f:
                print(f'\n{datetime.now().strftime("%Y-%m-%d %H:%M")}  MarketProfile\n', '='*64, file=f)
                print(f"An error occurred in function '{func.__name__}': {e}", file=f)
                print(f"Local variables: {local_vars}", file=f)
            raise  # Re-raise the exception if needed
    return wrapper

# def catch_errors(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             # Capture the local variables at the time of the exception
#             local_vars = {**kwargs}  # Start with keyword arguments
#             local_vars.update({f'arg{i}': arg for i, arg in enumerate(args)})  # Add positional arguments
            
#             # Log the error with variable information
#             print(f"An error occurred in function '{func.__name__}': {e}")
#             for var_name, value in local_vars.items():
#                 print(f"Variable '{var_name}': {value}")
#             raise  # Re-raise the exception if needed
#     return wrapper

def time_this(original_function):
    '''
    save result to file
    get and save name of every mesured function
    '''
    def new_function(*args,**kwargs):
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args,**kwargs)
        after = datetime.datetime.now()
        print('Elapsed Time = {0}'.format(after-before))
        return x
    return new_function

def utcnow():
    now = datetime.utcnow()
    now = now.replace(tzinfo=tzutc())
    now = now.strftime("%Y-%m-%d")
    return now

def price_formated(key):
        if len(str(key).split('.')[0]) == 5:
            key = int(float(key))
        elif len(str(key).split('.')[1]) == 7:
             key = arred(float(key), 6)
        else: key = float(key)
        return key

def dates_cycle(startdate, prev_sessions):
        # Define the start and end dates
        start_date = startdate  # Replace with your start date
        end_date = prev_sessions   # Replace with your end date

        # Create a list to hold the dates
        date_range = []

        # Iterate through the range of dates
        current_date = start_date
        while current_date >= end_date:
            date_range.append(current_date)  # Add the current date to the list
            current_date -= timedelta(days=1)  # Move to the next date
        
        return date_range
            
class formats():

    assets_view :dict = {'ACHUSDT': lambda price: price*1000, 'WLDUSDT': lambda price: price*10,\
                         'LEVERUSDT': lambda price: price*10000}

    @staticmethod
    def human_price_view(symbol :str, price :float):
        
        if symbol in formats.assets_view:
            price = formats.assets_view[symbol](price)
            return round(price, 2)
        else: price = price_formated(price)

        return price
    

class Last_mid_ticks_tr100():
    def last_body_ticks_mid_tr100(mp2h_sessions :isinstance):
        for obj in mp2h_sessions:
            if type(obj.body_ticks_mid_tr100) == float and obj.body_ticks_mid_tr100 > 0:
                return obj.body_ticks_mid_tr100

    def last_top_tail_mid_tr100(mp2h_sessions :isinstance):
        for obj in mp2h_sessions:
            if type(obj.top_tail_mid_tr100) == float and obj.top_tail_mid_tr100 > 0:
                return obj.top_tail_mid_tr100

    def last_bottom_tail_mid_tr100(mp2h_sessions :isinstance):
        for obj in mp2h_sessions:
            if type(obj.bottom_tail_mid_tr100) == float and obj.bottom_tail_mid_tr100 > 0:
                return obj.bottom_tail_mid_tr100