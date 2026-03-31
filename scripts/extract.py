import pandas as pd

def extract():
    df = pd.read_csv('data/sales_data.csv')
    print("Data extracted successfully")
    return df
