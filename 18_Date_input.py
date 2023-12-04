# Input Widgets in Streamlit(9)
#     1) Buttons
#     2) Download Button
#     3) Check Box
#     4) Radio Button
#     5) Select Box
#     6) Slider
#     7) Text Input
#     8) Number Input
#     9) Date Input  ######################
import streamlit as st
import datetime

d = st.date_input(
    'When is your birthday ?',
    datetime.date(2019,7,6))

st.write("Your birthday is:",d)
