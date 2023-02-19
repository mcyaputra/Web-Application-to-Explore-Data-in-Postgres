import streamlit as st

from src.dataframe.logics import Dataset

def read_data():
    """
    --------------------
    Description
    --------------------
    -> read_data (function): Function that loads the content of the Postgres table selected, extract its schema information and instantiate a Dataset class accordingly

    --------------------
    Parameters
    --------------------
    None

    --------------------
    Pseudo-Code
    --------------------
    Extract schema name from streamlit session state and save it to a variable
    Extract table name from streamlit session state and save it to a variable
    Extract database information from streamlit session state and save it to a variable
    Extract data table from the database and save it to a variable
    Initiate Dataset class and save it to streamlit session state

    --------------------
    Returns
    --------------------
    (str): Streamlit session state containing Dataset Class

    """

    #Initializing data for streamlit
    schema_name = st.session_state.schema_selected
    table_name = st.session_state.table_selected
    database = st.session_state.db
    df = database.load_table(schema_name, table_name)
    st.session_state.data = Dataset(schema_name, table_name, database, df)

def display_overall():
    """
    --------------------
    Description
    --------------------
    -> display_overall (function): Function that displays all the information on the Overall section of the streamlit app

    --------------------
    Parameters
    --------------------
    None

    --------------------
    Pseudo-Code
    --------------------
    Initiate function to extract the table required for streamlit and save it to a variable
    Set the table title
    Display the result using streamlit table

    Set the dataframe title
    Extract schema name from streamlit session state and save it to a variable
    Extract table name from streamlit session state and save it to a variable
    Extract schema information from the database and save it to a variable
    Display the result using streamlit dataframe

    --------------------
    Returns
    --------------------
    (table): Streamlit table and dataframe

    """
    #Overall Information Display
    overall_information = st.session_state.data.get_summary_df()
    st.title('Overall Information')
    st.table(overall_information)

    #Schema Information Display
    st.title ('Table Schema:')
    schema_name = st.session_state.schema_selected
    table_name = st.session_state.table_selected
    schema_information = st.session_state.db.get_table_schema(schema_name, table_name)
    st.dataframe(schema_information)

def display_dataframes():
    """
    --------------------
    Description
    --------------------
    -> display_dataframes (function): Function that displays all the information on the Explore section of the streamlit app

    --------------------
    Parameters
    --------------------
    None

    --------------------
    Pseudo-Code
    --------------------
    Set display title
    Set streamlit slider with value from 0 to 100
    Display value from the slider
    Set display title

    Initiate function to extract relevant informations

    Setting Streamlit Radio with selection options
    If user select "Head" option:
        Show the first n rows of the dataset
    If user select "Tail" option:
        Show the last n rows of the dataset
    Everything else:
        Show n sample rows of the dataset
    --------------------
    Returns
    --------------------
    (table): Streamlit user selection options and the resulting table

    """
    
    #Setting display
    st.title("Explore Dataframe")
    x = st.slider('Select number of rows to be displayed', 0, 100, 5)
    st.write("Slider Number:",  x)
    st.title("Exploration method")
    
    #Extracting data
    st.session_state.data.set_data()

    #Visualization
    type = st.radio("Exploration method", ('Head', 'Tail', 'Sample'))
    if type == 'Head':
        st.table(st.session_state.data.get_head(x))
    elif type == 'Tail':
        st.table(st.session_state.data.get_tail(x))
    else:
        st.table(st.session_state.data.get_sample(x))
