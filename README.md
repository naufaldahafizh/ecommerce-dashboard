# E-Commerce Sales Dashboard

This project provides interactive analysis and visualization of e-commerce sales data from [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), a Brazilian e-commerce platform.

---

## Project Goal

Help stakeholders understand:
- Sales trends over time
- Most popular product categories
- Customer segments based on spending

---

## Project Structure

```
ecommerce-dashboard/
├── data/ # Raw and cleaned datasets (CSV)
├── notebooks/ # EDA notebook
│ └── eda.ipynb
├── src/ # Python modules (data loading, aggregation)
│ ├── load_data.py
│ ├── top_products.py
│ ├── customer_segment.py
│ └── time_analysis.py
├── dashboard/ # Streamlit app
│ └── app.py
├── requirements.txt # Python dependencies
├── test_module
└── README.md
```

---

## How to Run the Dashboard

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Features
- Sales Overview: Track revenue trends by month
- Top Products: Explore top-selling product categories
- Customer Segments: Identify customers by spending level (Low to Top)

## Insights
- Sales peaked between late 2017 and early 2018
- Most orders are for tech-related and household products
- Equal distribution of customer segments
