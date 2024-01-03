import streamlit as st
from sqlfluff.api import fix, lint
import pandas as pd

# from datetime import datetime
from pathlib import Path
from utils import matomo_tracking, make_logo

# -----------------------------------------
# Global settings
# -----------------------------------------


# set page title and width
st.set_page_config(layout="wide", page_title="SQL code Formatter")

# remove footer and menu option
hide_menu_style = """
<style>
#MainMenu {visibility: hidden; }
footer {visibility: hidden; }
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

make_logo()

# -----------------------------------------
# Functionality
# -----------------------------------------

st.markdown("# SQL Code Formatter")

st.markdown("A utility tool to help create beautifully formatted SQL code")


with st.form("SQL form"):
    original_sql = st.text_area("Original SQL code", value="Paste SQL code here")
    my_dialect = st.radio(
        label="Select Dialect of SQL",
        options=["ansi", "bigquery", "mysql", "postgresql", "sqlite"],
        index=1,
    )

    submitted = st.form_submit_button("Format SQL")

    if submitted:
        st.markdown(
            """
        ---

        ## Results
        
        """
        )
        new_sql = fix(original_sql, dialect=my_dialect)
        linted = lint(original_sql, dialect=my_dialect)

        df = pd.DataFrame(linted)
        df.columns = ["Line Num", "Line Position", "Code", "Description", "Rule"]
        df["Line | Position"] = (
            df["Line Num"].astype(str) + " | " + df["Line Position"].astype(str)
        )
        df = df[["Code", "Line | Position", "Description"]]
        num_issues = len(df)

        if num_issues == 0:
            st.markdown(f"Great stuff, {num_issues} issues found!")

        elif num_issues <= 5:
            st.markdown(
                f":white_check_mark: Strong code, only {num_issues} issues found :white_check_mark:"
            )

        else:
            st.markdown(f":warning: {num_issues} issues found.")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### Original SQL Code")
            st.code(original_sql, language="sql")

        with col2:
            st.markdown("### Formatted SQL Code")
            st.code(new_sql, language="sql")

        with col3:
            st.markdown("### Issues identified")
            st.dataframe(data=df)

matomo_tracking()
