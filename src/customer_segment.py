import pandas as pd

def segment_customers(df):
    customer_orders = (
        df.groupby('customer_unique_id')
        .agg({
            'order_id': 'nunique',
            'total_price': 'sum'
        })
        .rename(columns={
            'order_id': 'order_count',
            'total_price': 'total_spent'
        })
        .reset_index()
    )

    # Segmentasi sederhana
    customer_orders['segment'] = pd.qcut(
        customer_orders['total_spent'], 
        q=4, 
        labels=['Low', 'Medium', 'High', 'Top']
    )

    return customer_orders
