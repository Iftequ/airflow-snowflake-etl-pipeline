def transform(df):
    df['total_price'] = df['quantity'] * df['price']
    df = df.dropna()
    print("Data transformed successfully")
    return df
