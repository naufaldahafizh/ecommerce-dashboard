import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# Tambahkan path root project (tempat src berada)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.load_data import load_clean_data
from src.top_products import get_top_n_products
from src.customer_segment import segment_customers
from src.time_analysis import sales_by_month

# Load data
df = load_clean_data()

# Title
st.title("E-Commerce Sales Dashboard (Olist)")

# Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Sales Overview", "Top Products", "Customer Segments"])

# Page: Sales Overview
if menu == "Sales Overview":
    st.header("Monthly Sales Overview")
    monthly = sales_by_month(df)
    fig = px.line(monthly, x="order_month", y="total_price", title="Monthly Revenue")
    st.plotly_chart(fig, use_container_width=True)

# Page: Top Products
elif menu == "Top Products":
    st.header("Top-Selling Product Categories")
    n = st.slider("Top N Products", 5, 20, 10)
    top_products = get_top_n_products(df, n)
    fig = px.bar(top_products, x="product_category_name", y="total_orders", title=f"Top {n} Products")
    st.plotly_chart(fig, use_container_width=True)

# Page: Customer Segments
elif menu == "Customer Segments":
    st.header("Customer Segmentation by Spending")
    seg = segment_customers(df)
    fig = px.histogram(seg, x="segment", title="Distribution of Customer Segments")
    st.plotly_chart(fig, use_container_width=True)
