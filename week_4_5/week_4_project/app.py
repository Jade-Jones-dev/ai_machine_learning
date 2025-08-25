from pathlib import Path
import sqlite3
import pandas as pd
import streamlit as st



APP_DIR = Path(__file__).parent
DB_PATH = APP_DIR / "books.db"

@st.cache_resource
def get_connection():
    return sqlite3.connect(DB_PATH)

@st.cache_data(show_spinner=False)
def sql(query: str, params: tuple | None = None) -> pd.DataFrame:
    con = get_connection()
    return pd.read_sql_query(query, con, params=params)


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

overview, books, authors, users = st.tabs([
    "Overview", "Books", "Authors", "Users"
])

with overview:
    st.subheader("Table sizes")
    counts = sql("""
        SELECT 'books' AS table_name, COUNT(*) AS rows FROM books
        UNION ALL
        SELECT 'ratings', COUNT(*) FROM ratings
        UNION ALL
        SELECT 'users', COUNT(*) FROM users
        ORDER BY rows DESC;
    """)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.dataframe(counts, use_container_width=True)
    with c2:
        explicit = 'WHERE "Book-Rating" > 0' if explicit_only else ''
        rating_dist = sql(f"""
            SELECT "Book-Rating" as rating, COUNT(*) as n
                        FROM ratings
                        {explicit}
                        GROUP BY rating
                        ORDER BY rating;
        """)
        st.subheader("Ratings distribution")
        tab1, tab2, tab3 = st.tabs(["BarChart", "LineChart", "AreaChart"])
        with tab1:
            st.write("BarChart")
            st.bar_chart(rating_dist.set_index("rating")['n'])
        with tab2:
            st.write("LineChart")
            st.line_chart(rating_dist.set_index("rating")['n'])
        with tab3:
            st.write("Area Chart")
            st.area_chart(rating_dist.set_index("rating")['n'])
        
  

