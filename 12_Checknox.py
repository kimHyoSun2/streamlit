# Input Widgets in Streamlit(9)
#     1) Buttons
#     2) Download Button
#     3) Check Box  ######################
#     4) Radio Button 
#     5) Select Box
#     6) Slider
#     7) Text Input
#     8) Number Input
#     9) Date Input


'''
https://docs.streamlit.io/library/api-reference/widgets/st.checkbox
st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
'''
import streamlit as st

ch1 = st.checkbox("옵션1", 'opt1')
ch2 = st.checkbox("옵션2", 'opt2')
ch3 = st.checkbox("옵션3", 'opt3')
ch4 = st.checkbox("옵션4", 'opt4')
ch5 = st.checkbox("옵션5", 'opt5')

if ch1: st.write('checked 옵션1')
if ch2: st.write('checked 옵션2')
if ch3: st.write('checked 옵션3')
if ch4: st.write('checked 옵션4')
if ch5: st.write('checked 옵션5')
