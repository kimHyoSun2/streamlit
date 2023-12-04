# Media Items in Streamlit(2)
#     1) Working with Images  
#     2) Working with Videos #######

# st.video(data, format="video/mp4", start_time=0)
import streamlit as st

video_file = open('data/sample.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)