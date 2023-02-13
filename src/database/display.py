import streamlit as st

from src.database.logics import PostgresConnector
from src.dataframe.display import read_data

def display_db_connection_menu():
    """
    --------------------
    Description
    --------------------
    -> display_db_connection_menu (function): Function that displays the menu for connecting to a database and triggers the database connection
    --------------------
    Pseudo-Code
    --------------------
    -> Put a title called 'Database Connection Details'
    -> Create a form to enter username, password, database host, database name, database port. (form key:'Connection Menu')
    -> Create a submit button to end the form.
    -> Update db_user, db_pass, db_host, db_name an db_port on the session state, using the relevant inputted values from the form
    -> Try to connect with database using PostgresConnector class with the value stored on the session state.
    -> if fail then print the error message, if it does not fail then connect and print success message.
    
    """
    
        
    st.title('Database Connection Details')

    with st.form(key='connection_menu'):
                 
        username=st.text_input('Username:','postgres')

        password=st.text_input('Password:','Password')

        database_host=st.text_input('Database Host:','postgres')

        database_name=st.text_input('Database Name:','postgres')

        database_port=st.text_input('Database Port:','5432')

        st.session_state['db_user']=username
        st.session_state['db_pass']=password
        st.session_state['db_host']=database_host
        st.session_state['db_name']=database_name
        st.session_state['db_port']=database_port

        submit=st.form_submit_button('Connect')
        
    try:
        connect=PostgresConnector (
        st.session_state['db_name'],
        st.session_state['db_user'],
        st.session_state['db_pass'],
        st.session_state['db_host'],
        st.session_state['db_port']
        )

    except:
        st.session_state['db_status']=bool(0)
        st.error(f'connection to server at {database_name}({database_host}), port {database_port} failed: FATAL: password authentication failed for user "{database_name}"', icon="🚨")

    else:
        st.session_state['db_status']=bool(1)
        st.success('Connection to database established', icon="✅")
        st.session_state['db']=PostgresConnector (
                                st.session_state['db_name'],
                                st.session_state['db_user'],
                                st.session_state['db_pass'],
                                st.session_state['db_host'],
                                st.session_state['db_port']
                                )  
             
            

def connect_db():
    """
    --------------------
    Description
    --------------------
    -> connect_db (function): Function that connects to a database and instantiate a PostgresConnector class accordingly
    --------------------
    Pseudo-Code
    --------------------
    -> Initiate psycopg2 connection using the values stored in the session state
    -> Return the active connection.
    """

    #initiating class object
    conn= PostgresConnector (
        st.session_state['db_name'],
        st.session_state['db_user'],
        st.session_state['db_pass'],
        st.session_state['db_host'],
        st.session_state['db_port']
        )

    


    return conn
    

def display_table_selection():
    """
    --------------------
    Description
    --------------------
    -> display_table_selection (function): Function that displays the selection box for selecting the table to be analysed and triggers the loading of data (read_data())
    --------------------
    Pseudo-Code
    --------------------
    -> Initiate the connect_db function
    -> Get the list of tables using the list_tables function
    -> Create selectbox to choose the table available
    -> update the table selected on session state with the table choosen
    -> Initiate read data by read_data function
    -> If read_data is not None then Update session state for 'data' to be string ' Read Data Success'
    """
    

    #Initiate class object data
    data=connect_db()
    
    #run the list_tables function to get the tables list
    table_list= data.list_tables()

    def split_schema():
        st.session_state['schema_selected']= (st.session_state['table_choice'].split('.'))[0]
        st.session_state['table_selected']= (st.session_state['table_choice'].split('.'))[1]
        
    table_list_option=st.selectbox('Select a table name',table_list,key='table_choice',on_change=split_schema)

    read_data()
    