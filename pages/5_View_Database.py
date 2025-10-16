
import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 View Database Contents")

# Connect to the database
conn = sqlite3.connect('fitness_app.db')

# Function to load table data
def load_table(table_name):
    try:
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        return df
    except Exception as e:
        return f"Error loading {table_name}: {e}"

# Display each table in an expander
for table in ['users', 'programs', 'logs']:
    with st.expander(f"View {table} table"):
        data = load_table(table)
        if isinstance(data, pd.DataFrame):
            st.dataframe(data)
        else:
            st.error(data)

conn.close()
