import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.set_page_config(page_title="Excel Dashboard", layout="wide")
st.title("📊 Live Excel Dashboard")

# Read the Excel file
df = pd.read_excel("Working_Excel.xlsx")

# Show the raw data
st.subheader("🔍 Raw Excel Data")
st.dataframe(df, use_container_width=True)

# Pivot summary (if possible)
if 'Category' in df.columns and 'Amount' in df.columns:
    st.subheader("📌 Pivot Summary")
    pivot = df.groupby("Category")["Amount"].sum().reset_index()
    st.dataframe(pivot)

    # Bar Chart
    st.subheader("📊 Bar Chart")
    bar_fig = px.bar(pivot, x="Category", y="Amount", title="Amount by Category")
    st.plotly_chart(bar_fig, use_container_width=True)

    # Pie Chart
    st.subheader("🧁 Pie Chart")
    pie_fig = px.pie(pivot, names="Category", values="Amount", title="Category Distribution")
    st.plotly_chart(pie_fig, use_container_width=True)
else:
    st.warning("The file must contain 'Category' and 'Amount' columns for summary and charts.")
