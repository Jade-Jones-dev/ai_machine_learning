import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Stream Lit Charts")
chart_data = pd.DataFrame(
    np.random.randn(30, 3),
    columns=["A", "B", "C"]
)

st.subheader("Area chart")
st.area_chart(chart_data)

st.subheader("Bar chart")
st.bar_chart(chart_data)

st.subheader("Line chart")
st.line_chart(chart_data)

st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
    'x' : np.random.randn(100),
    'y' : np.random.randn(100)
})

st.scatter_chart(scatter_data)

st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50/50] + [37.76, 122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

st.subheader("PyPlot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label="A")
ax.plot(chart_data['B'], label="B")
ax.plot(chart_data['C'], label="C")
ax.set_title("Py Plot line chart")
ax.legend()
st.pyplot(fig)
