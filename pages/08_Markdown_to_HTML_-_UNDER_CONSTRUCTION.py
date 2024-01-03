import streamlit as st
from utils import matomo_tracking, make_logo


make_logo()
st.markdown("# Markdown to HTML")

st.markdown("## Page under construction")

st.image(
    "https://marquin-space-object-storage-01.sgp1.cdn.digitaloceanspaces.com/web-resources/lil%20fel%20fel%20404.png"
)


# -----------------------------------------
# Matomo tracking
# -----------------------------------------

with open("matomo_tracking.html") as f:
    html_string = f.read()
    html(html_string)
