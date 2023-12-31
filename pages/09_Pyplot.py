# Chart Elements in Streamlit (4)
#     1) Line Chart
#     2) Area Chart
#     3) Bar Chart
#     4) Pyplot

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

arr = np.random.normal(1,1,size=100)
fig,ax = plt.subplots()
ax.hist(arr,bins=20)
st.pyplot(fig)
st.dataframe(arr,800)