# Chart Elements in Streamlit (4)
#     1) Line Chart
'''
이번장에서는 다양한 차트 요소를 제공하는 라인 차트 및 스트림에 대해 알아봅시다.
다양한 데이터 유형을 계획하고 시각화방법중에서 차트를 사용합니다.

첫번째 라인 차트표출 방법에 대해서 알아봅시다.

- 데이터 소스
- x축의 값 
- Y축의 값
- 폭
- 높이
'''

import streamlit as st
import pandas as pd
import numpy as np

data = np.random.randn(20,2)
# data = [[1,2,3,4,5],[10,20,30,40,50]]
chart_data = pd.DataFrame(data,columns = ['A','B'])
st.line_chart(chart_data)
st.dataframe(data,800)  # 800 width 
