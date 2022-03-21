import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import streamlit.components.v1 as components


# Page config
st.set_page_config(
    page_title="Smart Worker Dashboard",
    layout="wide"
)

# Tiles
col1, col2, col3, col4 = st.columns((7, 1, 1, 1))
col1.title("Mayor overview: Building's stats")
col2.button("Mayor")
col3.button('Employee')
col4.button("Worker")

# Metrics
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
col1.metric("Amount Spend", "354 000 EUR", "8000 EUR")
col2.metric("Work Hours", "475h", "-12%")
col3.metric("Humidity", "86%", "4%")
col4.metric("protected volume", "200 cube meter", "150 cube meter")
col5.metric("PEB", "A", "B")
col6.metric("pression", "86%", "4%")
col7.metric("luminosity", "60%", "6%")
col8.metric("renewable energy", "90%", "1%")

st.text("")

# Map
col1, col2 = st.columns((2, 3))
with col1:

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['electricity used', 'gas used', 'water used'])
    st.area_chart(chart_data)

    chart_data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["raw material", "recycled material", "transformed material"])
    st.bar_chart(chart_data)

with col2:
    components.iframe(
        "https://joffreybvn.github.io/dashboard_hackathon/map.html",
        height=600
    )

# Metrics
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Amount Spend", "354 000 EUR", "8000 EUR")
col2.metric("Work Hours", "475h", "-12%")
col3.metric("Humidity", "86%", "4%")
col4.metric("protected volume", "200 m3", "5 m3")

with col5:
    uploaded_files = st.file_uploader(label="Upload reports", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)


# Add custom styles
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
