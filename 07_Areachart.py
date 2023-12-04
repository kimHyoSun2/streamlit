# Chart Elements in Streamlit (4)
#     2) Area Chart
import streamlit as st
import pandas as pd
import numpy as np

data = np.random.randn(20,3)
chart_data = pd.DataFrame(data,columns = ['x','y','z'])
st.area_chart(chart_data)
st.dataframe(chart_data,800)
