# 01. streamlit 설치 및 테스트

# 01-1. 설치        pip install streamlit 
#       설치확인    pip list
#       설치제거    pip uninstall streamlit 

# 정상적으로 설치되었는지 확인하기 : streamlit hello

# 01-2 표출 테스트 하기 
#       다음과 같이 코드 입력 후  실행 
#       실행하는 방법 : streamlit run 01_test.py

import streamlit as st
import pandas as pd

view = [ i**2 for i in range(100)]
view
st.write('## TOI300 Streamlit Web Edu-Test')
st.bar_chart(view)

sview = pd.Series(view)
sview

# 결과값 
# [
# 0:100
# 1:100
# 2:100
# ]