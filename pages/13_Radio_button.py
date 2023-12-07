# Input Widgets in Streamlit(9)
#     1) Buttons
#     2) Download Button
#     3) Check Box
#     4) Radio Button   ######################
#     5) Select Box
#     6) Slider
#     7) Text Input
#     8) Number Input
#     9) Date Input

import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
elif genre == 'Drama':
    st.write('You selected drama')
elif genre == 'Documentary':
    st.write('You selected Documentary')

