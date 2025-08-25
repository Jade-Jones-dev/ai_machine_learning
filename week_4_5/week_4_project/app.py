from pathlib import Path
import sqlite3
import pandas as pd
import streamlit as st



APP_DIR = Path(__file__).parent
DB_PATH = APP_DIR / "books.db"

@st.cache_resource
def get_connection():
    return sqlite3.connect(DB_PATH)


st.title("Books / Ratings Dashboard")

with st.sidebar:
    st.header("Filters")
    min_ratings = st.slider("Min ratings per book", 0, 500, 50, 10)
    
    cohort_min, cohort_max = st.select_slider(
        "Age cohort (Users with known age)", options=list(range(5, 101)),
        value=(20,30)
    )
   
    explicit_only = st.checkbox("Only show ratings 1-10", value=True)
    st.divider()
    st.caption(f"Database: `{DB_PATH.name}`")
  

