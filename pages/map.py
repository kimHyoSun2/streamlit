# 지도 그리기
# 를 사용하면 st.map()지도에 데이터 포인트를 표시할 수 있습니다. Numpy를 사용하여 샘플 데이터를 생성하고 샌프란시스코 지도에 그려보겠습니다.

import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)