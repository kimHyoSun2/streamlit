import streamlit as st
import pandas as pd

view = [100,150,80]
view
st.write('## test view')
st.bar_chart(view)

sview = pd.Series(view)
sview
# 실행하는 방법streamlit run test.py
# 결과값 
# [
# 0:100
# 1:100
# 2:100
# ]
#aaaaa