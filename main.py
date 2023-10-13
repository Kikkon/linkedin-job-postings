import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, StreamlitRenderer

st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

st.title("Billionaires Statistics")
st.subheader("data source: https://www.kaggle.com/datasets/chuckephron/leagueoflegends/data")

# Initialize pygwalker communication
init_streamlit_comm()

# When using `use_kernel_calc=True`, you should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv("./LeagueofLegends.csv")
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    return StreamlitRenderer(df, spec="./billion_config.json", debug=True)


renderer = get_pyg_renderer()

# display explore ui
renderer.render_explore()

tab1, tab2 = st.tabs(
    ["Area Distribution", "Gender Distribution"]
)

# display chart ui
with tab1:
    st.subheader("Country Distribution")
    renderer.render_pure_chart(0)
    st.subheader("Area Distribution")
    renderer.render_pure_chart(2)

with tab2:
    st.subheader("Gender Distribution")
    renderer.render_pure_chart(1)
    st.subheader("Gender Distribution By Rank")
    renderer.render_pure_chart(3)
    st.subheader("Gender Distribution By Age")
    renderer.render_pure_chart(4, width=400)
