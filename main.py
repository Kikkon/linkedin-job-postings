import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, StreamlitRenderer

st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

st.title("Video Game Sales with Ratings Statistics")

# Initialize pygwalker communication
init_streamlit_comm()

# When using `use_kernel_calc=True`, you should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv("./Video_Games_Sales_as_at_22_Dec_2016.csv")
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    return StreamlitRenderer(df, spec="./config.json", debug=True)


renderer = get_pyg_renderer()

# display explore ui
renderer.render_explore()

tab1, tab2 = st.tabs(
    ["Top 20 Game", "Statistics"]
)

# display chart ui
with tab1:
    st.subheader("Top 20 Game")
    renderer.render_pure_chart(2)

with tab2:
    st.subheader("Sales Info")
    renderer.render_pure_chart(1, width=400)
    st.subheader("User Count")
    renderer.render_pure_chart(0, width=400)
