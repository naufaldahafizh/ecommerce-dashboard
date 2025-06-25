def get_top_n_products(df, n=10):
    top_products = (
        df.groupby('product_category_name')['product_id']
        .count()
        .sort_values(ascending=False)
        .head(n)
        .reset_index(name='total_orders')
    )
    return top_products
