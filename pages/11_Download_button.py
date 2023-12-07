# Input Widgets in Streamlit(9)
#     1) Buttons
#     2) Download Button  ######################
#     3) Check Box
#     4) Radio Button
#     5) Select Box
#     6) Slider
#     7) Text Input
#     8) Number Input
#     9) Date Input
import streamlit as st
import pandas as pd

sample_text = "무궁화 꽃이 피었습니다."
st.download_button('Download text',sample_text)

with open("data/flower.jpg","rb") as file:
    btn = st.download_button(
            label = "Download Image",
            data = file,
            file_name = "flower.jpg",
            mime = "image/jpg"
            )

# @st.cache

def convert_df(df):
    return df.to_csv().encode('utf-8')

df1 = pd.read_csv('data/addresses.csv')
csv = convert_df(df1)

st.download_button(
    label = "Download data as csv",
    data = csv,
    file_name = "large_df.csv",
    mime = "text/csv")
