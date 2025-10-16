
import streamlit as st
from db import init_db

st.set_page_config(page_title='Fitness App', layout='wide')
init_db()

st.title('🏋️‍♂️ Welcome to Your Fitness App')
st.markdown('Use the sidebar to navigate between modules.')
