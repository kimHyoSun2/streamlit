# Input Widgets in Streamlit(9)
#     1) Buttons
#     2) Download Button
#     3) Check Box
#     4) Radio Button
#     5) Select Box
#     6) Slider######################
#     7) Text Input
#     8) Number Input
#     9) Date Input
import streamlit as st
from datetime import time
from datetime import datetime

# 특정값
age = st.slider('■ How old are you?',0,100,15)
st.write("I am",age,"years old.")

# 범위
values = st.slider(
    '■ Select a range of values',
    0.0,100.0,(25.0, 75.0))
st.write("Values:",values)

# 시간
appointment = st.slider(
    "■ Schedule your appointment:",
    value=(time(11,30), time(12,45)))
st.write("You're scheduled for:",appointment)

# 날짜시간
start_time = st.slider(
    '■ When do you start?',
    value=datetime(2020,1,1,9,30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:",start_time)

