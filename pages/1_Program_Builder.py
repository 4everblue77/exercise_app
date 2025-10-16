
import streamlit as st
from db import insert_user

st.title("Program Builder")

with st.form("preferences_form"):
    name = st.text_input("Name")
    goal = st.selectbox("Goal", ["Strength", "Power", "Hypertrophy", "Endurance"])
    days = st.slider("Days per week", 1, 7)
    equipment = st.multiselect("Available Equipment", ["Barbell", "Dumbbells", "Kettlebells", "Pull-up Bar", "Ropes"])
    submitted = st.form_submit_button("Save Preferences")

if submitted:
    response = insert_user(name, goal, days, ",".join(equipment))
    if response and response.data:
        st.success("Preferences saved to Supabase!")
    else:
        st.error("Failed to save preferences.")
