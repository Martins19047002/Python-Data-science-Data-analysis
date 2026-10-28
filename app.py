import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from src.data_loader import load_covid_data
from src.analysis import compute_summary, rolling_average, hypothesis_summary
from src.visualization import plot_trends, plot_relationships

st.set_page_config(page_title="Indiana COVID-19 Dashboard", layout="wide")

DATA_PATH = Path("data/indiana_covid19_sample.csv")

st.title("Indiana COVID-19 Trend Dashboard")

with st.spinner("Loading Indiana COVID-19 data..."):
    df = load_covid_data(DATA_PATH)

if df.empty:
    st.error("No data available. Please confirm the CSV file exists in the data folder.")
    st.stop()

summary = compute_summary(df)

st.subheader("Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cases", f"{summary['total_cases']:,}")
col2.metric("Total Deaths", f"{summary['total_deaths']:,}")
col3.metric("Peak Cases/Day", f"{summary['peak_cases_per_day']:,}")
col4.metric("Peak Deaths/Day", f"{summary['peak_deaths_per_day']:,}")

st.subheader("Trend Analysis")
fig = plot_trends(df)
st.pyplot(fig)

st.subheader("Hypothesis Summary")
for hypothesis in hypothesis_summary(df):
    st.markdown(f"- {hypothesis}")

st.subheader("Detailed Relationships")
fig2 = plot_relationships(df)
st.pyplot(fig2)

st.caption("This dashboard uses the sample Indiana COVID-19 dataset included in the repository for demonstration and educational use.")
