from pathlib import Path
import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = Path(__file__).parent / "books.db"


@st.cache_resource
def get_connection():
    con = sqlite3.connect(DB_PATH, check_same_thread=False)
    con.execute("PRAGMA foreign_keys = ON; ")
    return con


@st.cache_data(show_spinner=False)
def sql(query: str, params: tuple | None = None) -> pd.DataFrame:
    con = get_connection()
    return pd.read_sql_query(query, con, params=params)


st.title("Books / Ratings Dashboard")

with st.sidebar:
    st.header("Filters")
    min_ratings = st.slider("Min ratings per book", 0, 500, 5, 5)

    cohort_min, cohort_max = st.select_slider(
        "Age cohort (Users with known age)", options=list(range(5, 101)), value=(20, 30)
    )

    explicit_only = st.checkbox("Only show ratings 1-10", value=True)
    st.divider()
    st.caption(f"Database: `{DB_PATH.name}`")

overview, books, authors, users = st.tabs(["Overview", "Books", "Authors", "Users"])

with overview:
    st.subheader("Overview")
    counts = sql(
        """
        SELECT 'books' AS table_name, COUNT(*) AS rows FROM books
        UNION ALL
        SELECT 'ratings', COUNT(*) FROM ratings
        UNION ALL
        SELECT 'users', COUNT(*) FROM users
        ORDER BY rows DESC;
        """
    )
    c1, c2 = st.columns([1, 2])
    with c1:
        st.subheader("Table sizes")
        st.dataframe(counts, use_container_width=True)
    with c2:
        explicit = 'WHERE "Book-Rating" > 0' if explicit_only else ""
        rating_dist = sql(
            f"""
            SELECT "Book-Rating" as rating, COUNT(*) as n
            FROM ratings
            {explicit}
            GROUP BY rating
            ORDER BY rating;
            """
        )
        st.subheader("Ratings distribution")
        tab1, tab2, tab3 = st.tabs(["Bar Chart", "Line Chart", "Area Chart"])
        with tab1:
            st.write("Bar chart for ratings distribution")
            st.bar_chart(rating_dist, x="rating", y="n")
        with tab2:
            st.write("Line chart for ratings distribution")
            st.line_chart(rating_dist, x="rating", y="n")
        with tab3:
            st.write("Area chart for ratings distribution")
            st.area_chart(rating_dist, x="rating", y="n")


with books:
    st.subheader("Most rated books")
    books_explicit = 'WHERE r."Book-Rating" > 0' if explicit_only else ""

    n_books = sql(
        f"""
         SELECT COUNT(*) AS n_books
         FROM (
             SELECT b.ISBN
             FROM ratings r
             JOIN books b ON b.ISBN = r.ISBN
             {books_explicit}
             GROUP BY b.ISBN
             HAVING COUNT(*) >= ?
             ) t;
        """,
        params=(min_ratings,),
    )
    st.write("Books meeting threshold:", int(n_books.loc[0, "n_books"]))

    books_df = sql(
        f"""
        SELECT b.ISBN,
           b."Book-Title" AS title,
           COUNT(*) AS n_ratings,
           AVG(r."Book-Rating") AS avg_rating
        FROM ratings r
        JOIN books b ON b.ISBN = r.ISBN
        {books_explicit}
        GROUP BY b.ISBN, title
        HAVING COUNT(*) >= ?
        ORDER BY n_ratings DESC
        LIMIT 50;
        """,
        params=(min_ratings,),
    )

if books_df.empty:
    st.info(
        "No books meet the current filters. Try lowering 'Min ratings' or unchecking 'Only show ratings 1–10'."
    )
else:
    st.dataframe(books_df, use_container_width=True, height=500)

with authors:
    st.subheader("Top authors by average rating")
    authors_df = sql(
        f"""
        SELECT b."Book-Author" AS author,
               COUNT(*) AS n_ratings,
               AVG(r."Book-Rating") AS avg_rating
        FROM ratings r
        JOIN books b ON b.ISBN = r.ISBN
        {books_explicit}
        GROUP BY author
        HAVING COUNT(*) >= 100
        ORDER BY avg_rating DESC, n_ratings DESC
        LIMIT 50;
    """
    )
    st.dataframe(authors_df, use_container_width=True, height=500)

with users:
    st.subheader("Cohort favourites")
    users_explicit = 'WHERE r."Book-Rating" > 0'if explicit_only else "WHERE 1=1"
    cohort_df = sql(f"""
        SELECT b."Book-Title" AS title,
               COUNT(*) AS n_ratings,
               AVG(r."Book-Rating") AS avg_rating
        FROM ratings r
        JOIN users u ON u."User-ID" = r."User-ID"
        JOIN books b ON b.ISBN = r.ISBN
        {users_explicit}
          AND u."Age" BETWEEN ? AND ?
        GROUP BY title
        HAVING COUNT(*) >= 20
        ORDER BY avg_rating DESC, n_ratings DESC
        LIMIT 50;
    """, params=(cohort_min, cohort_max))
    st.dataframe(cohort_df, use_container_width=True, height=500)

st.caption("Tip: use the sidebar to toggle explicit-only ratings and adjust thresholds.")