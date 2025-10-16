
import streamlit as st
from db import get_connection

st.title("Program Builder")

with st.form("preferences_form"):
    name = st.text_input("Name")
    goal = st.selectbox("Goal", ["Strength", "Power", "Hypertrophy", "Endurance"])
    days = st.slider("Days per week", 1, 7)
    equipment = st.multiselect("Available Equipment", ["Barbell", "Dumbbells", "Kettlebells", "Pull-up Bar", "Ropes"])
    submitted = st.form_submit_button("Save Preferences")

if submitted:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, goal, days_per_week, equipment) VALUES (?, ?, ?, ?)", (name, goal, days, ",".join(equipment)))
    conn.commit()
    conn.close()
    st.success("Preferences saved!")
