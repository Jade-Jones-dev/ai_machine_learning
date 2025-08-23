import streamlit as st
import time

#immutable
@st.cache_data(ttl=60)
def fetch_data():
    time.sleep(3)
    return{"data" : "This is cached data"}

st.write("Fetching data ...")
data = fetch_data()
st.write(data)

#mutable
file_path= "example.txt"
@st.cache_resource
def get_file_handler():
    file = open(file_path, "a+")
    return file

file_handler = get_file_handler()
if st.button("Write to file"):
    file_handler.write("New line of text\n")
    file_handler.flush()
    st.success("Wrote a new line in file")

if st.button("Read File"):
    file_handler.seek(0)
    content = file_handler.read()
    st.text(content)

st.button("Close file", on_click=file_handler.close)