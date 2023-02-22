def get_min_date_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_min_date_query (method): Function that returns the query used for computing the earliest date of a datetime column from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name (str): schema name of the database to look into
    -> table_name (str): table name of the schema to look into
    -> column_name (str): column name of the table to look into

    --------------------
    Pseudo-Code
    --------------------
    Creating SQL query to extract minimum date and save it to a variable
    Return the variable containing the SQL query

    --------------------
    Returns
    --------------------
    (str): SQL query to extract minimum date in the column

    """
    min_date = (f"SELECT min({col_name}) FROM {schema_name}.{table_name}")
    return min_date

def get_weekend_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_weekend_count_query (method): Function that returns the query used for computing the number of times a date of a datetime column falls during weekends

    --------------------
    Parameters
    --------------------
    -> schema_name (str): schema name of the database to look into
    -> table_name (str): table name of the schema to look into
    -> column_name (str): column name of the table to look into

    --------------------
    Pseudo-Code
    --------------------
    Creating SQL query to calculate number of weekend dates and save it to a variable
    Return the variable containing the SQL query

    --------------------
    Returns
    --------------------
    (str): SQL query to extract number of weekend dates

    """
    weekend_count = (f"SELECT COUNT({col_name}) FROM {schema_name}.{table_name} WHERE extract(DOW FROM {col_name}) IN (0, 6)")
    return weekend_count

def get_1900_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_1900_count_query (method): Function that returns the query used for computing the number of times a datetime column has the value '1900-01-01'

    --------------------
    Parameters
    --------------------
    -> schema_name (str): schema name of the database to look into
    -> table_name (str): table name of the schema to look into
    -> column_name (str): column name of the table to look into

    --------------------
    Pseudo-Code
    --------------------
    Creating SQL query to calculate number of times the columns has 1900-01-01 value and save it to a variable
    Return the variable containing the SQL query

    --------------------
    Returns
    --------------------
    (str): SQL query to extract number of times the columns has 1900-01-01 value

    """
    count_1900 = (f"SELECT COUNT(*) FROM {schema_name}.{table_name} WHERE {col_name} = '1900-01-01'")
    return count_1900