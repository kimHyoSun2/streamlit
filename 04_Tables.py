# Data Display Elements in Streamlit 
#     2) Tables
'''
이번 장에서는 데이터 디스플레이 요소인 표에 대해 알아봅시다
앞장에서 배운 데이터프레임에 비해 표는 보다 정적인 것을 표시하는데 사용됩니다. 

DataFrame에서는 데이터 정렬과 같은 옵션이 있고, 매개변수와 같은 것들을 통해서 변형이 가능합니다. 
그러나 테이블은 데이터를 정렬하거나 보기를 오름차순, 내림차순으로 변경하는 옵션을 얻을 수 없습니다
'''
import streamlit as st
import pandas as pd


data1 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
df = pd.DataFrame(data1, columns = ('col %d' % i for i in range(5)))
st.table(df)