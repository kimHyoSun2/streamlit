# Layouts and Containers in Streamlit(3)
#     1) Sidebar #################
#     2) Columns
#     3) Expander

import streamlit as st

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email","Home Phone","Mobile Phone"))

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard Shipping","Premium Shipping"))

    
