import streamlit as st
import langchain_helper

st.title("Restaurnt Suggestor")

location=st.sidebar.text_input(
    label="Enter a location :round_pushpin:"
)
cuisine=st.sidebar.selectbox(
    label="Cuisine Preference :knife_fork_plate:",
    options=("Arabic","American","Chinese","Indian"," Italian"," Mexican"),
)

meal=st.sidebar.selectbox(
    label="Type of meal :curry:",
    options=("Breakfast","Lunch","Dinner")
    )

budget=st.sidebar.text_input(
    label="Budget :money_with_wings:",
)

no_of_people=st.sidebar.slider(
    label="Number of people :woman-pouting: :man-pouting:",
    min_value=1,
    max_value=50,
    step=1
)


process_button_clicked=st.sidebar.button("Suggest restaurants")

if process_button_clicked:
    with st.spinner("Generating..."):
        response=langchain_helper.generate_restaurant_name(cuisine,no_of_people,meal,budget,location)
        st.write(response)








