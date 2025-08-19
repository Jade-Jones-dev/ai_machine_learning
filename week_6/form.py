import streamlit as st
import pandas as pd

st.title("Form demo")

with st.form(key="sample_form"):
    st.subheader("Text Inputs")
    name = st.text_input("Enter Your Name")
    feedback = st.text_area("Provide your feedback")

    st.subheader("Date and time inputs")
    dob = st.date_input("Select your date of birth")
    time= st.time_input("Choose a preferred time")

    st.subheader("Selectors")
    choice = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
    gender = st.selectbox("Select Your gender", ["Male", "Female", "Other", "Decline to answer"])
    slider_value = st.select_slider("Select a range", [1, 2, 3, 4, 5])

    st.subheader("Toggles and checkboxes")
    notifications = st.checkbox("Receive notifications?")
    toggle_value = st.checkbox("Enable dark mode?", value=False)

    submit_button = st.form_submit_button(label="Submit")

st.subheader("Buttons")
if st.button("Click me"):
    st.write(f"Hello {name}")
