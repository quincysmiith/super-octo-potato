import streamlit as st
from utils import matomo_tracking, make_logo

make_logo()
st.markdown("# Google Tag Manager Hunter")

st.markdown(
    "This is a simple app to help you find Google Tag Manager tags in your website."
)

st.markdown("## Page under construction")

st.image(
    "https://marquin-space-object-storage-01.sgp1.cdn.digitaloceanspaces.com/web-resources/lil%20fel%20fel%20404.png"
)


matomo_tracking()
