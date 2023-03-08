def get_missing_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_missing_query (method): Function that returns the query used for computing the number of missing values of a column from a Postgres table
    --------------------
    Parameters
    --------------------
    
    None

    --------------------
    Pseudo-Code
    --------------------
    
    Caculates all missing values based on query

    --------------------
    Returns
    --------------------
    (string): Returns column names that got selected

    """
    query= f'SELECT {col_name} FROM {schema_name}.{table_name} WHERE {col_name} IS NULL'
    return query

def get_mode_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_mode_query (method): Function that returns the query used for computing the mode value of a column from a Postgres table
    --------------------
    Parameters
    --------------------
    
    None

    --------------------
    Pseudo-Code
    --------------------
    
    Caculates the mode value of a column though SQL

    --------------------
    Returns
    --------------------
    (string): Returns columns that has the mode
    

    """
    query = f"SELECT mode() WITHIN GROUP (ORDER BY {col_name}) FROM {schema_name}.{table_name};"
    return query

def get_alpha_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_alpha_query (method): Function that returns the query used for computing the number of times a column from a Postgres table has only alphabetical characters
    --------------------
    Parameters
    --------------------
    
    None

    --------------------
    Pseudo-Code
    --------------------
    
    Caculates the number of times a column contains an alphabet via query

    --------------------
    Returns
    --------------------
    (int): caculates all the columns count that has alphabet
    
    """

    query = f"select count({col_name}) from {schema_name}.{table_name} where ({col_name} ~* '[a-z]') is true"
    return query