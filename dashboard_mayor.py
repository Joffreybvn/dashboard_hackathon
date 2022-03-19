import streamlit as st
from PIL import Image
import leafmap.foliumap as leafmap


# Page config
st.set_page_config(
    page_title="Smart Worker Dashboard",
    layout="wide"
)

# Tiles
col1, col2, col3, col4 = st.columns((7, 1, 1, 1))
col1.title("Smart Worker Dashboard")
col2.button("Mayor")
col3.button('Employee')
col4.button("Worker")

# Metrics
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
col1.metric("Amount Spend", "354 000 EUR", "8000 EUR")
col2.metric("Work Hours", "475h", "-12%")
col3.metric("Humidity", "86%", "4%")
col4.metric("Humidity", "86%", "4%")
col5.metric("Humidity", "86%", "4%")
col6.metric("Humidity", "86%", "4%")
col7.metric("Humidity", "86%", "4%")
col8.metric("Humidity", "86%", "4%")

# Map
col1, col2 = st.columns((2, 3))
with col1:
    st.button("Town hall")
    st.button("Daycare")
    st.button("CPAS")
    st.button("Residential care")
    st.button("Hospital")
    st.button("Cultural center")
    st.button("Theatre")

with col2:
    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    m = leafmap.Map(tiles='openstreetmap')
    m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="pop_max", name="Heat map", radius=20)
    m.to_streamlit(width=700, height=500, add_layer_control=True)


# Add custom styles
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
