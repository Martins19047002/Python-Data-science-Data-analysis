from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from src.analysis import compute_summary, hypothesis_summary
from src.data_loader import load_covid_data
from src.visualization import plot_relationships, plot_trends

st.set_page_config(page_title="Indiana COVID-19 Dashboard", layout="wide")

DATA_PATH = Path("data/indiana_covid19_sample.csv")

st.title("Indiana COVID-19 Trend Dashboard")
st.caption("A simple public-health dashboard for exploring COVID-19 trends in Indiana.")

with st.spinner("Loading dataset..."):
    df = load_covid_data(DATA_PATH)

if df.empty:
    st.error("The data file was not found or could not be loaded. Check the data folder.")
    st.stop()

summary = compute_summary(df)

st.subheader("Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cases", f"{summary['total_cases']:,}")
col2.metric("Total Deaths", f"{summary['total_deaths']:,}")
col3.metric("Peak Daily Cases", f"{summary['peak_cases_per_day']:,}")
col4.metric("Peak Daily Deaths", f"{summary['peak_deaths_per_day']:,}")

st.subheader("Trend Analysis")
fig_trends = plot_trends(df)
st.pyplot(fig_trends)

st.subheader("Additional Relationships")
fig_rel = plot_relationships(df)
st.pyplot(fig_rel)

st.subheader("Hypotheses")
for item in hypothesis_summary(df):
    st.markdown(f"- {item}")

st.caption("This dashboard uses a sample Indiana COVID-19 dataset included in this repository for demonstration purposes.")
