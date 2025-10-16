
import streamlit as st
from db import get_connection
from datetime import date

st.title("Log Workout")

with st.form("log_form"):
    exercise = st.text_input("Exercise")
    weight = st.number_input("Weight (kg)", min_value=0.0)
    sets = st.number_input("Sets", min_value=1)
    reps = st.number_input("Reps", min_value=1)
    time = st.text_input("Time (if cardio)")
    rpe = st.slider("RPE", 1, 10)
    submitted = st.form_submit_button("Log Workout")

if submitted:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (user_id, date, exercise, weight, sets, reps, time, rpe) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (1, date.today().isoformat(), exercise, weight, sets, reps, time, rpe))
    conn.commit()
    conn.close()
    st.success("Workout logged!")
