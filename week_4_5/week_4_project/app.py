from pathlib import Path
import sqlite3
import pandas as pd
import streamlit as st

st.title("Streamlit charts project")

APP_DIR = Path(__file__).parent
DB_PATH = APP_DIR / "books.db"

@st.cache_resource
def get_connection():
    return sqlite3.connect(DB_PATH)

