import streamlit as st
import pandas as pd

st.title("Streamlit data demo")

st.subheader("Dataframe")

df = pd.DataFrame({
    "Name":["Pete", "Bob", "George", "Jack", "Jill", "Harry"],
    "Age": [30, 64, 37, 21, 84, 36],
    "Occupation": ["Builder", "Engineer", "Architect", "Priest", "Yoga Teacher", "Journalist"],
    "City": ["London", "Glasgow", "New York", "Cardiff", "Liverpool", "Wolverhampton"]
})
st.dataframe(df)

st.subheader("Data Editor")
editable_df = st.data_editor(df)

st.subheader("Static table")
st.table(df)

st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(), 1))