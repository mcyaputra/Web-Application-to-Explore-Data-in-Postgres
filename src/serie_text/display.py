import streamlit as st

from src.serie_text.logics import TextColumn

def display_texts():
    """
    --------------------
    Description
    --------------------
    -> display_texts (function): Function that displays all the relevant information for every text column of a table
    --------------------
    Parameters
    --------------------
    
    None

    --------------------
    Pseudo-Code
    --------------------
    
    Connects the database and text class together to display all the text information

    --------------------
    Returns
    --------------------
    (table): Displays texts under streamlit expander

    """
    text_data = st.session_state.data
    text_data.set_date_columns()
    date_columns = text_data.text_cols

    for column_name in date_columns:
        with st.expander(column_name, expanded=False):
            display_text(column_name, None)

def display_text(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_text (function): Function that instantiates a TextColumn class from a dataframe column and displays all the relevant information for a single text column of a table
    --------------------
    Parameters
    --------------------
    
    None

    --------------------
    Pseudo-Code
    --------------------
    
    Connects the dataframe and fills the information requests

    --------------------
    Returns
    --------------------
    (Table): tables containing all the information

    """
    schema_name = st.session_state.schema_selected
    table_name = st.session_state.table_selected
    database = st.session_state.db
    df = st.session_state.data.df
    
    Text_Column_Class = TextColumn(schema_name, table_name, col_name, database, df[col_name])

    #Extracting Data
    Text_Column_Class.set_data()

    #Visualization
    st.table(Text_Column_Class.get_summary_df())
    st.text('Bar Chart')
    st.altair_chart(Text_Column_Class.set_barchart())
    st.text('The Most Frequent Values')
    st.dataframe(Text_Column_Class.frequent)