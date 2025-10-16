
import streamlit as st
from db import insert_log
from datetime import date

st.title("Log Workout")

with st.form("log_form"):
    user_id = st.number_input("User ID", min_value=1)
    exercise = st.text_input("Exercise")
    weight = st.number_input("Weight (kg)", min_value=0.0)
    sets = st.number_input("Sets", min_value=1)
    reps = st.number_input("Reps", min_value=1)
    time = st.text_input("Time (if cardio)")
    rpe = st.slider("RPE", 1, 10)
    submitted = st.form_submit_button("Log Workout")

    if submitted:
        response = insert_log(user_id, date.today().isoformat(), exercise, weight, sets, reps, time, rpe)
        if response.error is None:
            st.success("Workout logged to Supabase!")
        else:
            st.error(f"Failed to log workout: {response.error}")
