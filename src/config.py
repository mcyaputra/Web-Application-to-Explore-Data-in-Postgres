import streamlit as st

def set_app_config():
    """
    --------------------
    Description
    --------------------
    -> set_app_config (function): Function that sets the configuration of the Streamlit app

    --------------------
    Pseudo-Code
    --------------------
    -> set title to Database Explorer
    ->initiate page config function


    """
    page_title= 'Database Explorer'
    st.set_page_config(
        page_title=page_title)
        

def set_session_state(key, value):
    """
    --------------------
    Description
    --------------------
    -> set_session_state (function): Function that saves a key-value pair to the Streamlit session state

    --------------------
    Pseudo-Code
    --------------------
    -> if key is not exist in session state yet, then create a key on session state with the inputted values


    """

    if key not in st.session_state:
        if key == 'db_user':
            st.session_state[key] = os.environ['POSTGRES_USER']
        elif key == 'db_pass':
            st.session_state[key] = os.environ['POSTGRES_PASSWORD']
        elif key == 'db_host':
            st.session_state[key] = os.environ['POSTGRES_HOST']
        elif key == 'db_name':
            st.session_state[key] = os.environ['POSTGRES_DB']
        elif key == 'db_port':
            st.session_state[key] = os.environ['POSTGRES_PORT']
        else:
            st.session_state[key] = value

    # if key not in st.session_state:
    #     st.session_state[key] = value

def set_session_states(keys, value=None):
    """
    --------------------
    Description
    --------------------
    -> set_session_states (function): Function that saves a list of key-value pairs to the Streamlit session state using set_session_state() (default value: None)

    --------------------
    Pseudo-Code
    --------------------
    -> go through each list given and assign them as session state key if its not present yet
    -> default value none, so empty if not specified

    """
    for key in keys:
        if key not in st.session_state:
            st.session_state[key] = value
        
    

def display_session_state():
    """
    --------------------
    Description
    --------------------
    -> display_session_state (function): Function that displays the current values of Streamlit session state

    --------------------
    Pseudo-Code
    --------------------

    -> print the current session state on streamlit
    """
    st.write (st.session_state)



