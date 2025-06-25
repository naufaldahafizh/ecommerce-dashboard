def sales_by_month(df):
    monthly = (
        df.groupby('order_month')['total_price']
        .sum()
        .reset_index()
    )
    return monthly
