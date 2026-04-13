import streamlit as st
import pandas as pd

st.title("AI Data Dashboard")

df = pd.read_csv("data/processed/output.csv")

st.dataframe(df)
st.line_chart(df.select_dtypes(include='number'))