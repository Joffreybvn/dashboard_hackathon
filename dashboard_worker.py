import streamlit as st
from PIL import Image

with col1:
    image = Image.open('./images/interior_1.jpeg')
    st.text('')
    st.image(image)