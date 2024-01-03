import streamlit as st
from streamlit.components.v1 import html
from ydata_profiling import ProfileReport
import pandas as pd
import sweetviz as sv
from utils import matomo_tracking, make_logo

st.set_page_config(layout="wide", page_title="Data Summaries", page_icon="🧊")

make_logo()

st.markdown("# Data Summaries")

st.markdown(
    """
            Understand your data with a quick data summary.
            This app summarizes your data using Pandas Profiling and Sweetviz. 
            
            You can also download the reports as html files.
            """
)

st.markdown("---")

st.markdown("## Upload your data")

uploaded_file = st.file_uploader(
    "Choose a csv file to see a summary of the data within", type=["csv"]
)

st.markdown("---")

st.markdown("## Data Summaries")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    profile = ProfileReport(data, explorative=True)

    st.markdown("### Ydata Profile report")
    html_report = profile.to_html()
    with st.expander("Expand for Ydata profiling report"):
        html(html_report, width=700, height=1000, scrolling=True)
    profile.to_file("report.html")
    st.download_button(
        "Download Ydata report", html_report, file_name="ydata_report.html"
    )

    st.markdown("### Sweetviz Profile report")
    my_report = sv.analyze(data)
    my_report.show_html(
        filepath="SWEETVIZ_REPORT.html",
        open_browser=False,
        layout="widescreen",
        scale=None,
    )
    with open("SWEETVIZ_REPORT.html", "r") as f:
        sweetviz_html = f.read()
    with st.expander("Expand for Sweetviz report"):
        html(sweetviz_html, height=1000, scrolling=True)
    st.download_button(
        "Download Sweetviz report", sweetviz_html, file_name="sweetviz_report.html"
    )


# -----------------------------------------
# Matomo tracking
# -----------------------------------------

with open("matomo_tracking.html") as f:
    html_string = f.read()
    html(html_string)
