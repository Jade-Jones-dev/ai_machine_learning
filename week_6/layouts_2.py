import streamlit as st

# using keys 
# st.button("Ok")
# st.button("Ok", key="btn2")

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("Set min value", 0, 50, 25)
st.session_state.slider = st.slider("Slider", min_value, 100, min_value)

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show input field", value=st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
    user_input = st.text_input("Enter something:", value=st.session_state.user_input)
    st.session_state.user.input = user_input
else:
    user_input = st.session_state.get("user_input", '')

st.write(f"User input: {user_input}")