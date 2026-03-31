import snowflake.connector

def load(df):
    conn = snowflake.connector.connect(
        user='YOUR_USER',
        password='YOUR_PASSWORD',
        account='YOUR_ACCOUNT'
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(f"""
        INSERT INTO sales (product, quantity, price, total_price)
        VALUES ('{row['product']}', {row['quantity']}, {row['price']}, {row['total_price']})
        """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded to Snowflake")
