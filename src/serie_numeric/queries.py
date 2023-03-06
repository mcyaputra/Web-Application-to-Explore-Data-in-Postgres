def get_negative_number_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_negative_number_query (method): Function that returns the query used for computing the number of times a column from a Postgres table has negative values 

    --------------------
    Parameters
    --------------------
    -> schema_name(string): name of the postgres schema
    -> table_name(string): name of the postgres table
    -> col_name(string): name of the columns in the postgres table

    --------------------
    Pseudo-Code
    --------------------
    -> Read postgres sql table, then return the count of negative values in a column

    --------------------
    Returns
    --------------------
    -> integer of the number of times a column has negative values 

    """
    negative_number = (f"SELECT SUM(CASE WHEN {col_name} < 0 THEN 1 ELSE 0 END) AS negative FROM {schema_name}.{table_name}")
    return negative_number

 
def get_std_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_std_query (method): Function that returns the query used for computing the standard deviation value of a column from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name(string): name of the postgres schema
    -> table_name(string): name of the postgres table
    -> col_name(string): name of the columns in the postgres table

    --------------------
    Pseudo-Code
    --------------------
    -> Read postgres sql table, then return the standard deviation of each column

    --------------------
    Returns
    --------------------
    -> a float of a column's standard deviation

    """
    std = (f"SELECT stddev_samp({col_name}) FROM {schema_name}.{table_name}")
    return std

def get_unique_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_unique_query (method): Function that returns the query used for computing the number of unique values of a column from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name(string): name of the postgres schema
    -> table_name(string): name of the postgres table
    -> col_name(string): name of the columns in the postgres table

    --------------------
    Pseudo-Code
    --------------------
    -> Read postgres sql table, then return the unique values of a column

    --------------------
    Returns
    --------------------
    -> (list): a list of the unique values of a column

    """
    unique = (f"SELECT COUNT (DISTINCT ({col_name})) FROM {schema_name}.{table_name}")
    return unique
