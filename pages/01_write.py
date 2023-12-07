# st.write()

import streamlit as st
import pandas as pd

# 글자를 써봅시다 
st.write("## ■ write string")
st.write('hello')           # normal
st.write('*hello*')         # italic
st.write('**hello**')       # bold
st.write('***hello***')     # bold & italic
st.write(':red[hello]')     # color text 
st.write(':orange[hello]')  # color text 


# print문처럼 쉼표 구분자로 쓰기 가능
st.write("# ■ write string & int")
st.write(3,"*",5,'=',3*5)   # 문자와 숫자의 표출형태 비교 

# 리스트 데이터 표출가능
st.write("# list ")
view = [ i**2 for i in range(1,5)]
st.write(view) # 이렇게도 가능 

# 명시적인 명령어를 입력할 필요 없이 
# 거의 모든 것(마크다운, 데이터, 차트)을 작성 가능
# 보여주고 싶은 것을 자신의 코드 라인에 넣기만 하면 앱에 표시
view           # 이렇게도 가능 (매직명령어)


# 큰 글자(#1개)  ~ 작은 글자 (#6개)
st.write("# write text ")
st.write("## write text ")
st.write("### write text ")
st.write("#### write text ")
st.write("##### write text ")
st.write("###### write text ")

# 결과값 
# [
# 0:100
# 1:100
# 2:100
# ]