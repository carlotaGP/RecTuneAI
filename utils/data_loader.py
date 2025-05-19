import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path="data/spotify_clean.csv"):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df
