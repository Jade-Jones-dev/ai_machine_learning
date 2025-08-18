import streamlit as st
import os

#st.write("Hello world we are live and working")
#st.write({"key": "value"})
#3 + 4
#"Bye"


#pressed = st.button("Press me")
#print("First", pressed)

#pressed2 = st.button("Press me too")
#print("Second", pressed2)
st.title("Title")
st.header("This is a header")
st.subheader("Sub Header")
st.markdown(" This is a **Markdown** _italics_")
st.caption("Small text")

code_example = """
def greet(name):
    print("hello", name)
"""

st.code(code_example, language="python")
st.divider()
st.image(os.path.join(os.getcwd(), "static", "alexa.png"))



