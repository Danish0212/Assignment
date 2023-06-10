import streamlit as st
import os
from src.UI import foo
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    body {
        zoom: 90%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
import math
from PIL import Image
import os

with open('style/final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

# st.markdown("<div style='display: flex; margin-top: -45px ; justify-content: center;'><hr style='height: 2px; background-color: gray; width: 440px; border: none;'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: blue;margin-top: -10px ;font-size:20px;'><span style='font-weight: bold'></span>ChatGPT  Application</p>", unsafe_allow_html=True)
st.markdown("<hr style=height:2.5px;margin-top:0px;background-color:gray;>",unsafe_allow_html=True)
#---------Side bar-------#

with st.sidebar:
    selected = st.selectbox("",['GPT integrated'],key='text')
    Library = st.selectbox("",
                     ["Library Used","Streamlit","langchain","openAI","Pandas",],key='text1')
    st.markdown("## ")
    href = """<form action="#">
            <input type="submit" value="Clear/Reset" />
            </form>"""
    st.sidebar.markdown(href, unsafe_allow_html=True)
#--------------function calling-----------#
if __name__ == "__main__":
    try:
        if selected == 'GPT integrated':
            foo()
    except BaseException as error:
        st.error(error)