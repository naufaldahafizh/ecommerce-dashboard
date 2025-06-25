from src.load_data import load_clean_data
from src.top_products import get_top_n_products
from src.customer_segment import segment_customers
from src.time_analysis import sales_by_month

df = load_clean_data()
print(get_top_n_products(df, 5))
print(segment_customers(df))
print(sales_by_month(df))