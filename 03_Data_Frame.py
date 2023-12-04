# Data Display Elements in Streamlit 
#     1) Working with DataFrames

import streamlit as st
import pandas as pd
import numpy as np

st.write('DataFrame Test')
# data = np.random.randn(50,20)
data1 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
df = pd.DataFrame(data1, columns = ('col %d' % i for i in range(5)))
st.dataframe(df)
