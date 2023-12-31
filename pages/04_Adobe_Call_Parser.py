import streamlit as st
from streamlit.components.v1 import html
from utils import matomo_tracking, make_logo

st.set_page_config(
    page_title="Adobe Call Parser",
    page_icon="🧊",
    layout="wide",
)

make_logo()

st.title("Adobe Call Parser")

embed_code = """
<p class="codepen" data-height="600" data-default-tab="result" data-slug-hash="qjQJNr" data-user="quincysmiith" style="height: 161.33297729492188px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/quincysmiith/pen/qjQJNr">
  Parsing Adobe Calls</a> by marquin (<a href="https://codepen.io/quincysmiith">@quincysmiith</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
"""


html(embed_code, width=700, height=600)

st.markdown(
    """
            For a guide on how to use this tool see this [post](https://marquinsmith.com/2017/09/12/using-the-adobe-call-parser/)
            """
)


matomo_tracking()
