import streamlit as st

st.markdown("# Google Tag Manager Hunter")

st.markdown("This is a simple app to help you find Google Tag Manager tags in your website.")

st.markdown("## Page under construction")

st.image("https://marquin-space-object-storage-01.sgp1.cdn.digitaloceanspaces.com/web-resources/lil%20fel%20fel%20404.png")


# -----------------------------------------
# Matomo tracking
# -----------------------------------------

with open("matomo_tracking.html") as f:
    html_string = f.read()
    html(html_string)