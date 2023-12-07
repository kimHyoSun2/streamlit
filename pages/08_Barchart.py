# Chart Elements in Streamlit (4)
#     1) Line Chart(03:25)
#     2) Area Chart(03:16)
#     3) Bar Chart(03:05)
import streamlit as st
import pandas as pd
import numpy as np

data = np.random.randn(20,3,)
chart_data = pd.DataFrame(data,columns = ['a','b','c'])
st.bar_chart(chart_data)
st.dataframe(data,800)



# 그래프 그리기 
#view = [ i**2 for i in range(1,5)]
# st.write('## TOI300 Streamlit Web Edu-Test')
# st.bar_chart(view)

# sview = pd.Series(view)
# sview
# st.write(sview)
