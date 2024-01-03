import streamlit as st
from streamlit.components.v1 import html


def make_logo():
    """
    set the marquinsmith logo on the page, aligned to the right hand side
    """
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col6:
        st.image("https://marquin-space-object-storage-01.sgp1.cdn.digitaloceanspaces.com/web-resources/FINAL%20LOGO%20LARGE%20OPTION%20DARK%20GREY%20FOR%20WEBSITE.png",
                width = 50 )

def matomo_tracking():
    """load matomo tracking code into the streamlit app
    """

    # -----------------------------------------
    # Matomo tracking
    # -----------------------------------------

    with open("matomo_tracking.html") as f:
        html_string = f.read()
        html(html_string)