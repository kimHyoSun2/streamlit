# Layouts and Containers in Streamlit(3)
#     1) Sidebar 
#     2) Columns
#     3) Expander #################

import streamlit as st

st.bar_chart({"data":[1,5,2,6,2,1]})

with st.expander("Expand me"):
    st.write("Some text written inside expander")
    st.write("Hello Hello Hello")
