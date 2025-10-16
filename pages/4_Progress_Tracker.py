
import streamlit as st
from db import get_logs_by_user

st.title("Progress Tracker")

user_id = st.number_input("Enter User ID", min_value=1)
response = get_logs_by_user(user_id)

if response.error is None and response.data:
    st.dataframe(response.data)
else:
    st.info("No logs found for this user or failed to fetch data.")
