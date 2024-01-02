import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pandas as pd

st.set_page_config(layout="wide")

init_streamlit_comm()

st.title("Data Explorer")

st.markdown("Interactive data exploration tool using Pygwalker")

st.markdown("---")

st.markdown("## Upload a csv file")

uploaded_file = st.file_uploader("Choose a csv file to see a summary of the data within", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)


    @st.cache_resource
    def get_renderer():
        return StreamlitRenderer(data)
    

    st.markdown("## Explore the data")

    renderer = get_renderer()

    renderer.render_explore()
