import datetime as dt

import streamlit as st

import visualization.graphs as graphs
from visualization.data import get_data

with open("visualization/dashboard_header.md", "r") as f:
    header = f.read()


def app():
    st.markdown(header, unsafe_allow_html=True)
    user = st.text_input("User Reference")
    if not user:
        st.error("Please enter a user reference")
    today = dt.date.today()
    start, end = st.date_input(
        value=(today - dt.timedelta(days=7), today),
        label="Start Date",
        max_value=today,
    )
    if start > end:
        st.error("Start date must be before end date")

    df = get_data(user, start, end)
    st.altair_chart(graphs.line_chart(df))
