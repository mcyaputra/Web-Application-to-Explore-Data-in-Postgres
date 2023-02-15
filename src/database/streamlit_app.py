import streamlit as st

from config import set_app_config, set_session_states, display_session_state
from display import display_db_connection_menu, display_table_selection


set_session_states(['db', 'db_host', 'db_name', 'db_port', 'db_user', 'db_pass', 'db_status', 'db_infos_df', 'schema_selected', 'table_selected', 'data'])

set_app_config()
st.title("Database Explorer")

# Add Debugger
with st.expander("Streamlit Session State", expanded=False):
    display_session_state()

# Add Menu
with st.expander("ℹ️ - Streamlit application for performing data exploration on a database", expanded=True):
    display_db_connection_menu()

if st.session_state.db_status:
    display_table_selection() 
    
    

