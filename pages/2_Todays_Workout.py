
import streamlit as st
from db import get_programs_by_date
from datetime import date

st.title("Today's Workout")

response = get_programs_by_date(date.today().isoformat())
if response.data:
    for row in response.data:
        st.write(f"**{row['exercise']}** – {row['sets']} sets × {row['reps']} reps (Rest: {row['rest']}s)")
else:
    st.info("No workout scheduled for today.")
