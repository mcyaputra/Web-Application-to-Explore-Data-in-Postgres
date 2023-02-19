def get_numeric_tables_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_numeric_tables_query (method): Function that returns the query used for extracting the list of numeric columns from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name (str): schema name of the database to look into
    -> table_name (str): table name of the schema to look into

    --------------------
    Pseudo-Code
    --------------------
    Assigning list of numeric data types in Postgres to a variable
    Assigning SQL query to extract numeric columns to a variable
    Return the variable containing the complete SQL query

    --------------------
    Returns
    --------------------
    -> (str): SQL query to extract numeric columns from Postgres database

    """
    numeric_types = ('smallint', 'integer', 'bigint', 'decimal', 'numeric', 'real', 'double precision', 'serial', 'bigserial')
    numeric_columns = (f"Select column_name FROM information_schema.columns WHERE table_schema = '{schema_name}' AND table_name = '{table_name}' AND data_type IN {numeric_types}")
    return numeric_columns

def get_text_tables_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_text_tables_query (method): Function that returns the query used for extracting the list of text columns from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name (str): schema name of the database to look into
    -> table_name (str): table name of the schema to look into

    --------------------
    Pseudo-Code
    --------------------
    Assigning list of text data types in Postgres to a variable
    Assigning SQL query to extract text columns to a variable
    Return the variable containing the complete SQL query

    --------------------
    Returns
    --------------------
    -> (str): SQL query to extract numeric columns from Postgres database

    """

    character_types = ('character varying', 'varchar', 'character', 'char', 'text')
    text_columns = (f"Select column_name FROM information_schema.columns WHERE table_schema = '{schema_name}' AND table_name = '{table_name}' AND data_type IN {character_types}")
    return text_columns

def get_date_tables_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_date_tables_query (method): Function that returns the query used for extracting the list of datetime columns from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name (str): schema name of the database to look into
    -> table_name (str): table name of the schema to look into

    --------------------
    Pseudo-Code
    --------------------
    Assigning list of date data types in Postgres to a variable
    Assigning SQL query to extract date columns to a variable
    Return the variable containing the complete SQL query

    --------------------
    Returns
    --------------------
    -> (str): SQL query to extract date columns from Postgres database

    """
    datetime_types = ('date', 'timestamp', 'time', 'interval')
    datetime_columns = (f"Select column_name FROM information_schema.columns WHERE table_schema = '{schema_name}' AND table_name = '{table_name}' AND data_type IN {datetime_types}")
    return datetime_columns
