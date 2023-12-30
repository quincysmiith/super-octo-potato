import streamlit as st
from streamlit.components.v1 import html
from ydata_profiling import ProfileReport
import pandas as pd
import sweetviz as sv




st.set_page_config(layout="wide",
                   page_title="Data Summaries", 
                   page_icon="🧊")




uploaded_file = st.file_uploader("Choose a file")


if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    profile = ProfileReport(data, explorative=True)

    st.markdown("<h1 style='text-align: center;'>Pandas Profiling Report</h1>", unsafe_allow_html=True)
    html_report = profile.to_html()
    with st.expander("Expand for Ydata profiling report"):
        html(html_report, width=700, height=1000, scrolling=True)
    profile.to_file("report.html")
    st.download_button("Download Ydata report", "report.html", file_name="ydata_report.html")


    st.markdown("<h1 style='text-align: center;'>Sweetviz data report</h1>", unsafe_allow_html=True)
    my_report = sv.analyze(data)
    my_report.show_html(filepath='SWEETVIZ_REPORT.html', 
            open_browser=False, 
            layout='widescreen', 
            scale=None)
    with open('SWEETVIZ_REPORT.html', 'r') as f:
        sweetviz_html = f.read()
    with st.expander("Expand for Sweetviz report"):
        html(sweetviz_html, height=1000, scrolling=True)
    st.download_button("Download Sweetviz report", "SWEETVIZ_REPORT.html", file_name="sweetviz_report.html")

