import pandas as pd 
import os
from datetime import datetime


# decorator for showing time of function work
def counttime(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        result = func(*args, **kwargs)
        later = datetime.now()
        difference = (later - now).total_seconds()
        print(f'...time took: {difference:,.0f} seconds\n\n')
        return result
    return wrapper

@counttime
def read_data(file_name):
    return pd.read_csv(file_name, sep=', ', engine='python')

@counttime
def agg_data(df):
    return df.groupby('city').id.agg(['count'])

@counttime
def save_csv(df, file_name):
    cols = ["count"]
    df[cols].to_csv(file_name, sep=',')


if __name__ == '__main__':
    file_name = 'data23mb.txt'

    mb = os.path.getsize(file_name) / 1024 / 1024
    print (f'processing file {mb:.1f}mb')

    df = read_data(file_name)

    print ('agg and count data: ')
    df_cities = agg_data(df)
    print(df_cities.head())

    print (f'saving to {file_name}_agg.txt: ')
    file_name = file_name+'_agg.txt'
    save_csv(df_cities, file_name)