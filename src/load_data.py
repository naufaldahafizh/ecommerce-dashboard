import pandas as pd

def load_clean_data(path='../ecommerce-dashboard/data/clean_orders.csv'):
    df = pd.read_csv(path, parse_dates=['order_purchase_timestamp'])
    df['order_month'] = pd.to_datetime(df['order_month'])
    return df
