# Layouts and Containers in Streamlit(3)
#     1) Sidebar 
#     2) Columns  #################
#     3) Expander

import streamlit as st

st.write('# Column 나누기1')
col1, col2, col3 = st.columns(3)
with col1:
    st.header("This is column 1")
    st.title("Col 1")
    st.write("Some text inside column 1")


with col2:
    st.header("This is column 2")
    st.title("Col 2")
    st.write("Some text inside column 2")

with col3:
    st.header("This is column 3")
    st.title("Col 3")
    st.write("Some text inside column 3")


# 사이드바 외에도 Streamlit은 앱 레이아웃을 제어할 수 있는 여러 가지 다른 방법을 제공함
# st.columns위젯을 나란히 배치할 수 있고 
# st.expander 큰 콘텐츠를 숨겨 공간을 절약할 수 있습니다.

st.write('# Column 나누기2')

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
with left_column:
    st.button('Press me1!')
    if st.button('Press me2!'): st.write('Pressed me2!')


# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")