import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit.components.v1 as components


# Page config
st.set_page_config(
    page_title="St Catherine's public school - Building overview",
    layout="wide"
)

# Tiles
col1, col2, col3, col4 = st.columns((7, 1, 1, 1))
col1.title("Building overview: St Catherine's public school")
col2.button("Mayor")
col3.button('Employee')
col4.button("Worker")

# Metrics
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
col1.metric("Last intervention", "18 March 22", "Three days ago")
col2.metric("Last scan", "4 April 22", "47 days ago")
col3.metric("Remaining issues", "3", "-2")
col4.metric("Total reparations", "43", "+2")
col6.metric("Total cost", "45 000 EUR", "+ 3000 EUR")
col5.metric("PEB", "A", "B")
col7.metric("luminosity", "60%", "6%")

with col8:
    st.subheader("⬇️ page as file")
    with open("./images/report.xlsx", "rb") as file:
        btn = st.download_button(
            label="Download report (.xlsx)",
            data=file,
            file_name="report.xlsx",
            mime="application/vnd.ms-excel"
        )

st.text("")

# Map
col1, col2 = st.columns((3, 2))
with col1:
    # image = Image.open('./images/interior_3.jpeg')
    # st.image(
    #     image,
    #     width=800
    # )

    components.iframe(
        "https://joffreybvn.shapespark.com/demo-room/",
        height=600
    )

with col2:

    # Fies history
    df = pd.DataFrame({
        'Tag': ["#7680", "#8740", "#8926", "#9873", "#9904", "#9953"],
        'Worker': ["Heating Engineer", "Electrician", "School owner", "Electromechanician", "School owner", "Plumber"],
        'History': [
            "New boiler added to the main cellar room. Seems to get some imperfections on the injection system: The pipe seems to be fixed on the ground.",
            "Cables and electricity was been added. Boiler is now connected to the grid",
            "Automatic door for children to enter doesn't seems to work very well",
            "Fiex the door. We should take a look at all doors as this is an issue from the doors themself.",
            "Boiler have stopped here today, and don't turn back on. Could and intervention be done quickly ?",
            "Boiler is failing due to its cooling system. Temporary fix has been made by redirecting pool's water to the cooling system."
        ]
    })
    st.table(df)

    # Add comments to history
    text_area = st.text_area('Add a new event')
    st.button('Commit event')

# Charts
st.subheader("Overall building maintenances")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)


# Add custom styles
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)