import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
 
# Add Title
st.title("Use Pygwalker In Streamlit")
 
# Import your data
df = pd.read_csv("job_postings.csv")
 
# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, return_html=True)

# Generate the HTML using Pygwalker
pyg_table = pyg.walk(df, hideDataSourceConfig=True, vegaTheme='vega')
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)

 
# Embed the HTML into the Streamlit app
components.html(pyg_table, height=1000, scrolling=True)
