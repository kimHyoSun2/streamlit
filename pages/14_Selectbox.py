# Input Widgets in Streamlit(9)
#     1) Buttons
#     2) Download Button
#     3) Check Box
#     4) Radio Button
#     5) Select Box ##########################
#     6) Slider
#     7) Text Input
#     8) Number Input
#     9) Date Input
import streamlit as st

option = st.selectbox(
    '시도',
    ('서울','대전','대구','부산','울산','광주','세종'))

st.write('선택시도:',option)



import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['second column'])

'You selected: ', option



