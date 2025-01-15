import streamlit as st
import Pipeline as pl
st.title("Event Extractor")

result=[]
Url = st.text_input("Enter the Url", value="", max_chars=100)

size = st.slider("Select Range of Sentence", 0, 100, 2)

if st.button("Extract Event"):
    result= pl.event_extract(Url, size)
    for x in result:
        st.write(x)
     

