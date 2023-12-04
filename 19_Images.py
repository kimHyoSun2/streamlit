# Media Items in Streamlit(2)
#     1) Working with Images   #######
#     2) Working with Videos

from PIL import Image
import streamlit as st

image = Image.open('data/flower.jpg')

st.image(image,caption="Nice Picture")
