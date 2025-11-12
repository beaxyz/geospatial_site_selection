from data import *
import streamlit as st
from kepler import *
from kepler import config
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static
from genie import start_genie_conversation, genie_follow_up_questions
from databricks.sdk import WorkspaceClient


st.set_page_config(layout="wide")
w = WorkspaceClient()
genie_space_id = "01f0af66c3d31bea950683a024e50e86"

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

    map, chat = st.columns([2,1])
    with map:
        kmap = render_kepler(data)
        #keplergl_static(kmap, height = 800, width=3000)
        html = kepler_html(kmap)
        st.components.v1.html(html, height=kmap.height+10, scrolling=False)

    with chat:
        
        st.subheader("💬 Genie")
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "conversation_id" not in st.session_state:
            st.session_state.conversation_id = None
        
        @st.fragment()
        def chat_interface(general_land_type, square_size_m2, number_of_sites, distance_to_road_min, distance_to_road_max):
            chat_container = st.container(height = 600)
            with chat_container:
                for messages in st.session_state.messages:
                    #with st.chat_message(name=messages["question"]):
                    st.chat_message("User").write(messages["question"])
                    st.chat_message("Assistant").dataframe(messages["response"], hide_index=True)

            if st.session_state.conversation_id is None:
                question = f"What are the proposed sites if i have a requirement of {square_size_m2} square size in m^2, min distance to road of {distance_to_road_min} and max distance to road of {distance_to_road_max}, {number_of_sites} potential sites and {general_land_type} general land types?"
                response, conversation_id = start_genie_conversation(genie_space_id, question)
                st.session_state.conversation_id = conversation_id
                st.session_state.messages.append({"question": question, "response": response})

            if question:=st.chat_input("What do you want to ask of your data?"):
                with st.spinner("🤔 Genie is thinking..."):
                    response = genie_follow_up_questions(genie_space_id, question ,conversation_id = st.session_state.conversation_id)
                    
                st.session_state.messages.append({"question": question, "response": response})
                st.rerun(scope = "fragment")


        chat_interface(general_land_type, square_size_m2, number_of_sites, distance_to_road_min, distance_to_road_max)

        # Done - Initially add in context for bounding box based on parameters
        # Done - Make the chat scrollable
        # Manage non tabular responses
        # Add some sample questions
        # Clear button to refresh state

            
        
            




