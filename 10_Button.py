# Input Widgets in Streamlit(9)
#     1) Buttons######################
#     2) Download Button
#     3) Check Box
#     4) Radio Button
#     5) Select Box
#     6) Slider
#     7) Text Input
#     8) Number Input
#     9) Date Input

import streamlit as st

if st.button('Say Hello'):
    st.write('Hey Hello There ! ')
else:
    st.write('Goodbye')
