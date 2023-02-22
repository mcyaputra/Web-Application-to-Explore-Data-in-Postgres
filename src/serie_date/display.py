import streamlit as st

from src.serie_date.logics import DateColumn


def display_dates():
    """
    --------------------
    Description
    --------------------
    -> display_dates (function): Function that displays all the relevant information for every datetime column of a table

    --------------------
    Parameters
    --------------------
    None

    --------------------
    Pseudo-Code
    --------------------
    Extracting data from streamlit session state and save it to a variable
    Extracting datetime columns
    Assigning the result to a variable

    Using every columns in the date dataset:
        Build streamlit expander with columns as options:
            run display_date function with every columns as the variable


    --------------------
    Returns
    --------------------
    (table): Streamlit expander

    """
    #Configuration
    date_data = st.session_state.data
    date_data.set_date_columns()
    date_columns = date_data.date_cols

    # Datetime column dropdown/expander
    for column_name in date_columns:
        with st.expander(column_name, expanded=False):
            display_date(column_name, 'column')

def display_date(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_date (function): Function that instantiates a DateColumn class from a dataframe column and displays all the relevant information for a single datetime column of a table

    --------------------
    Parameters
    --------------------
    col_name (str): name of the column
    i (str): index

    --------------------
    Pseudo-Code
    --------------------
    Extracting schema name from streamlit session state and save it to a variable
    Extracting table name from streamlit sessions state and save it to a variable
    Extracting database details from streamlit session state and save it to a variable
    Extracting data from streamlit session state and save it to a variable

    Initiate DateColumn class using above variables and assign it to a variable

    Initiate method from DateColumn class to extract relevant information

    Extract summary from DateColumn method and present it using streamlit table

    Write text using streamlit text
    Display barchart using streamlit altair chart

    Write text using streamlit text
    Display most frequent values table using streamlit dataframe

    --------------------
    Returns
    --------------------
    (table): Streamlit table
    (chart): Streamlit barchart
    (table): Streamlit dataframe

    """
    #Configuration
    schema_name = st.session_state.schema_selected
    table_name = st.session_state.table_selected
    database = st.session_state.db
    df = st.session_state.data.df
    
    #Assigning objects to Date Column Class
    Date_Column_Class = DateColumn(schema_name, table_name, col_name, database, df[col_name])

    #Extracting Data
    Date_Column_Class.set_data()

    #Visualization
    st.table(Date_Column_Class.get_summary_df())

    #Barchart
    st.text('Bar Chart')
    st.altair_chart(Date_Column_Class.set_barchart())

    #Most Frequent Values
    st.text('The Most Frequent Values')
    st.dataframe(Date_Column_Class.frequent)
