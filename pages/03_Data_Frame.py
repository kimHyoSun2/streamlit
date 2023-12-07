# Data Display Elements in Streamlit 
#     1) Working with DataFrames

import streamlit as st
import pandas as pd
import numpy as np


st.write('## DataFrame 데이터 보이기 I')
# data = np.random.randn(50,20)
data1 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
df = pd.DataFrame(data1, columns = ('col %d' % i for i in range(5)))
st.dataframe(df)



st.write('## DataFrame 데이터 보이기 II')
df = np.random.randn(10, 20)
st.dataframe(df)





# import streamlit as st
# import pandas as pd
# df = pd.DataFrame({
# 'first column': [1, 2, 3, 4],
# 'second column': [10, 20, 30, 40]
# })

# df   

# import streamlit as st
# import pandas as pd

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))
