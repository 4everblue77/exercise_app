
import streamlit as st
from db import get_connection
from datetime import date

st.title("Today's Workout")

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM programs WHERE date = ?", (date.today().isoformat(),))
workout = cursor.fetchall()
conn.close()

if workout:
    for row in workout:
        st.write(f"**{row[4]}** – {row[5]} sets × {row[6]} reps (Rest: {row[7]}s)")
else:
    st.info("No workout scheduled for today.")
