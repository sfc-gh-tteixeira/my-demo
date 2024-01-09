import streamlit as st

"""
# Hello world!
"""

n = st.slider("Number of repetitions", 1, 1000)

"Hi there! " * n
