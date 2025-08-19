import streamlit as st

st.sidebar.title("This is the sidebar")
st.sidebar.write("You can place elements here")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("You are in Tab 1")

with tab2:
    st.write("You are in Tab 2")

with tab3:
    st.write("You are in Tab 3")

col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")

with st.container(border=True):
    st.write("This is inside of a container")
    st.write("Containers can group elements")
    st.write("This helps you manage sections on the page")

placeholder = st.empty()
placeholder.write("This is an empty placeholder.Useful for dynamic content")

if st.button("Update placeholder"):
    placeholder.write("This placeholder text has been updated")

with st.expander("Expand for more details"):
    st.write("this is hidden by default")
    st.write("This helps to create cleaner interfaces")

st.write("Hover over this button for a tooltip")
st.button("Button with a tooltip", help="This is a tooltip or popover on hover")

if sidebar_input:
    st.write(f"You enter in the sidebar: {sidebar_input}")