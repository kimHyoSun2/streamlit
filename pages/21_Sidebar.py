# Layouts and Containers in Streamlit(3)
#     1) Sidebar #################
#     2) Columns
#     3) Expander

import streamlit as st

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email","Home Phone","Mobile Phone"))
if add_selectbox == 'Email':
    st.write('selected email')
elif add_selectbox == 'Home Phone':
    st.write('Home Phone')    
elif add_selectbox == 'Mobile Phone':
    st.write('Mobile Phone')    

# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard Shipping","Premium Shipping"))

    
# sidebar에 selectbox 추가 

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# sidebar에 slider 추가 
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
