import streamlit as st

from src.serie_numeric.logics import NumericColumn

def display_numerics():
    """
    --------------------
    Description
    --------------------
    -> display_numerics (function): Function that displays all the relevant information for every numerical column of a table

    --------------------
    Parameters
    --------------------
    -> serie: Pandas serie loading the content of a column

    --------------------
    Pseudo-Code
    --------------------
    -> apply numeric functions to a serie to find if the serie is none, its unique values, missing values, 
    zeroes, negative values, mean, standard deviation, mininum value, maximum value, median, 
    most frequent value, its summary

    --------------------
    Returns
    --------------------
    --> a serie's information on if is none, its unique values, missing values, 
    zeroes, negative values, mean, standard deviation, mininum value, maximum value, median, 
    most frequent value, its summary

    """

    numeric_data = st.session_state.data
    numeric_data.set_numeric_columns()
    numeric_columns = numeric_data.num_cols

    for column_name in numeric_columns:
        with st.expander(column_name, expanded=False):
            display_numeric(column_name, None)


def display_numeric(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_numeric (function): Function that instantiates a NumericColumn class from a dataframe column and displays all the relevant information for a single numerical column of a table

    --------------------
    Parameters
    --------------------
    -> serie: Pandas serie loading the content of a column

    --------------------
    Pseudo-Code
    --------------------
    --> instantiate a NumericColumn class from a dataframe column and display the relevant information 
    for a single numerical column of a table

    --------------------
    Returns
    --------------------
    --> a single column's information on if is none, its unique values, missing values, 
    zeroes, negative values, mean, standard deviation, mininum value, maximum value, median, 
    most frequent value, its summary

    """
    schema_name = st.session_state.schema_selected
    table_name = st.session_state.table_selected
    database = st.session_state.db
    df = st.session_state.data.df
    
    Numeric_Column_Class = NumericColumn(schema_name, table_name, col_name, database, df[col_name])
  
    Numeric_Column_Class.set_data()
    st.text('Summary')
    st.table(Numeric_Column_Class.get_summary_df())
    st.text('Chart')
    st.altair_chart(Numeric_Column_Class.set_histogram())

    
