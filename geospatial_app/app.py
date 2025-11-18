from pandas._libs.lib import count_level_2d
from data import *
import streamlit as st
from kepler import *
from kepler import config
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static
from genie import start_genie_conversation, genie_follow_up_questions
from databricks.sdk import WorkspaceClient


st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(160deg, #f1f4ff 0%, #fef5e5 45%, #ffffff 100%);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

w = WorkspaceClient()
genie_space_id = "01f0af66c3d31bea950683a024e50e86"

with st.sidebar:
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
        "Road Links": road_links_df()
    }

    display_df = st.session_state.get("display_polygon")
    if display_df is not None:
        data["Display"] = display_df

st.title("Exeter Site Analysis")  
with st.container():
    map, chat = st.columns([3,2])

    with map:
        kmap = render_kepler(data)
        html = kepler_html(kmap)
        st.components.v1.html(html, height=kmap.height+10, scrolling=False)


    with chat:
        st.subheader("💬 Genie")
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "conversation_id" not in st.session_state:
            st.session_state.conversation_id = None
        if "submit_from_button" not in st.session_state:
            st.session_state.submit_from_button = False
        if "pending_question" not in st.session_state:
            st.session_state.pending_question = None
        if "display_polygon" not in st.session_state:
            st.session_state.display_polygon = None

        @st.fragment()
        def chat_interface(general_land_type, square_size_m2, number_of_sites, distance_to_road_min, distance_to_road_max):
            chat_container = st.container(height = 600)
            if st.session_state.conversation_id is None:
                question = f"What are the proposed sites if i have a requirement of {square_size_m2} square size in m^2, min distance to road of {distance_to_road_min} and max distance to road of {distance_to_road_max}, {number_of_sites} potential sites and {general_land_type} general land types?"
                response = start_genie_conversation(genie_space_id, question)
                st.session_state.conversation_id = response["conversation_id"]
                st.session_state.messages.append({"question": question, "response_data": response["response_data"], "response_text": response["response_text"]})

            with chat_container:
                sample_questions = [
                    "What are the most common general land types in the developed land?",
                    "What is the average area of undeveloped land by detailed land type?",
                    "What types of buildings are next to these proposed sites?"
                ]

                for messages in st.session_state.messages:
                    st.chat_message("User").write(messages["question"])
                    if isinstance(messages["response_data"], pd.DataFrame):
                        if messages["response_text"] is not None:
                            st.chat_message("Assistant").write(messages["response_text"])
                            st.chat_message("Assistant").dataframe(messages["response_data"], hide_index=True)
                        else:
                            st.chat_message("Assistant").dataframe(messages["response_data"], hide_index=True)
                        
                    elif messages["response_text"] is not None and isinstance(messages["response_text"], str):
                        st.chat_message("Assistant").write(messages["response_text"])

                st.markdown("<div style='margin-bottom: 0.8rem;'>Suggested questions:</div>", unsafe_allow_html=True)
                prefix = "Using parameters from the previous message"
                for idx, sample in enumerate(sample_questions, start=1):
                    if st.button(f"{idx}. {sample}", key=f"sample_q_{idx}", use_container_width=True):
                        st.session_state.pending_question = sample
                        st.session_state.submit_from_button = True
                        st.rerun(scope="fragment")

                question = st.chat_input("What do you want to ask of your data?")

                if st.session_state.submit_from_button:
                    with st.spinner("🤔 Genie is thinking..."):
                        response = genie_follow_up_questions(genie_space_id, f"{prefix}: {st.session_state.pending_question}" ,conversation_id = st.session_state.conversation_id)    
                        st.session_state.messages.append({"question": st.session_state.pending_question, "response_data": response["response_data"], "response_text": response["response_text"]})
                        st.session_state.submit_from_button = False
                        st.session_state.pending_question = None
                        st.rerun(scope = "fragment")

                elif question:
                    with st.spinner("🤔 Genie is thinking..."):
                        response = genie_follow_up_questions(genie_space_id, f"{prefix}: {question}" ,conversation_id = st.session_state.conversation_id)    
                        st.session_state.messages.append({"question": question, "response_data": response["response_data"], "response_text": response["response_text"]})
                        st.rerun(scope = "fragment")

                # if question:=st.chat_input("What do you want to ask of your data?"):
                #     with st.spinner("🤔 Genie is thinking..."):
                #         response = genie_follow_up_questions(genie_space_id, question ,conversation_id = st.session_state.conversation_id)
                        
                #     st.session_state.messages.append({"question": question, "response_data": response["response_data"], "response_text": response["response_text"]})
                #     st.rerun(scope = "fragment")

            def clear_conversation():
                st.session_state.messages = []
                st.session_state.conversation_id = None

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Refesh & Clear Chat"):
                    clear_conversation()
                    st.rerun(scope = "fragment")
            with col2:
                if st.button("Display on Map"):
                    display_df = pd.DataFrame(st.session_state.messages[-1]["response_data"])
                    st.session_state.display_polygon = display_df
                    st.rerun()


        chat_interface(general_land_type, square_size_m2, number_of_sites, distance_to_road_min, distance_to_road_max)


        

        # Done - Manage non tabular responses
        # Add some sample questions
        # Done - Clear button to refresh state
        # Done -Get a cut of polygon from the end user & showcase this on Kepler, then ask questions about it from Genie. 

            
        
            




