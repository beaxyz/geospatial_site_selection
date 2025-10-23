from data import *
import streamlit as st
from kepler import kepler_html, render_kepler
from data import *


st.set_page_config(layout="wide")

with st.container():
    st.title("Exeter Site Analysis")
    land_types = list(
        set(developed_land_df()["general_land_type"].unique()) | set(undeveloped_land_df()["general_land_type"].unique())
    )
    land_types.sort()

    general_land_type = st.selectbox("Select Land Type", ["All"] + land_types, index=0)
    square_size_m2 = st.number_input("Select Square Size", min_value=1000, max_value=30000, value=3000, step=100)
    number_of_sites = st.number_input("Select Number of Sites", min_value=1, max_value=100, value=3, step=1)
    distance_to_road = st.slider("Select Distance to Road (meters)", min_value=100, max_value=1000, value=[100,1000], step=100)
    distance_to_road_min = distance_to_road[0]
    distance_to_road_max = distance_to_road[1]

    data = {
        "Developed": developed_land_df(general_land_type),
        "Undeveloped Land": undeveloped_land_df(general_land_type),
        "Bounding Box": bounding_box_df(general_land_type, square_size_m2, number_of_sites, distance_to_road_min, distance_to_road_max),
        "Road Nodes": road_node_df(),
        "Road Links": road_links_df(),
    }

    kmap = render_kepler(data)
    html = kepler_html(kmap)
    st.components.v1.html(html, height=kmap.height + 10, scrolling=False)