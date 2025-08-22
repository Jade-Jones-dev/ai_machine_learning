import streamlit as st

# using keys 
# st.button("Ok")
# st.button("Ok", key="btn2")

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("Set min value", 0, 50, 25)
slider_value = st.slider("Slider", min_value, 100, min_value)