
import streamlit as st
from supabase import create_client

# Supabase credentials (replace with your actual values)
SUPABASE_URL = "https://kbohrthtkhjrcfmkxyuh.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtib2hydGh0a2hqcmNmbWt4eXVoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA1NTQ1MTksImV4cCI6MjA3NjEzMDUxOX0.CAJUDA4cSplorG4xhLhX7-_OWkV879yZHHXUG8t8__s"

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Streamlit app config
st.set_page_config(page_title='Fitness App', layout='wide')

# Display welcome message
st.title("🏋️‍♂️ Welcome to Your Fitness App")
st.markdown("Use the sidebar to navigate between modules.")

# Test connection to Supabase
try:
    response = supabase.table("users").select("*").limit(1).execute()
    if response.data:
        st.success("Connected to Supabase successfully!")
    else:
        st.warning("Connected to Supabase, but no user data found.")
except Exception as e:
    st.error(f"Failed to connect to Supabase: {e}")
