import psycopg2
from psycopg2 import OperationalError
import pandas as pd
import numpy as np

from src.database.queries import get_tables_list_query, get_table_data_query, get_table_schema_query

class PostgresConnector:
    
    """
    --------------------
    Description
    --------------------
    -> PostgresConnector (class): Class that manages the connection to a Postgres database
    --------------------
    Attributes
    --------------------
    -> database (str): Name of Postgres database (mandatory)
    -> user (str): Username used for connecting to Postgres database (mandatory)
    -> password (str): Password used for connecting to Postgres database (mandatory)
    -> host (str): URL of Postgres database (mandatory)
    -> port (str): Port number of Postgres database (mandatory)
    -> conn (psycopg2._psycopg.connection): Postgres connection object (optional)
    -> cursor (psycopg2._psycopg.connection.cursor): Postgres cursor for executing query (optional)
    -> excluded_schemas (list): List containing the names of internal Postgres schemas to be excluded from selection (information_schema, pg_catalog)
    """

    def __init__(self, database="postgres", user='postgres', password='password', host='127.0.0.1', port='5432'):
       

        self.database=database
        self.user=user
        self.password= password
        self.host=host
        self.port= port
        self.conn= psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database)
        self.cursor=self.conn.cursor()
        self.excluded_schemas=['information_schema', 'pg_catalog' ]
        

    
    def open_connection(self):
        
        """
        --------------------
        Description
        --------------------
        -> open_connection (method): Class method that creates an active connection to a Postgres database
        --------------------
        Pseudo-Code
        --------------------
        -> Try to connect to postgresql
        -> If operational error, then return boleean false
        -> if sucessful then return boleean true
        """



        try:
            self.conn

        except psycopg2.OperationalError:
            return bool(0)


        else:
            return bool(1)
            
        

    def close_connection(self):

        """
        --------------------
        Description
        --------------------
        -> close_connection (method): Class method that closes an active connection to a Postgres database
        --------------------
        Pseudo-Code
        --------------------
        -> create an object to initiate psycopg2 connection to the database
        -> close the connection
        -> return connection closed or not, boleean true means connection is closed
        """


        conn=self.conn
        conn.close()
        
        return conn.closed

    def open_cursor(self):

        """
        --------------------
        Description
        --------------------
        -> open_cursor (method): Class method that creates an active cursor to a Postgres database
        --------------------
        Pseudo-Code
        --------------------
        -> Initiatiate the cursor by referring to the class attributes object
        -> Return the cursor object
        
        """
        cursor=self.cursor
        cursor

        return cursor


    def close_cursor(self):
        """
        --------------------
        Description
        --------------------
        -> close_cursor (method): Class method that closes an active cursor to a Postgres database 
        --------------------
        Pseudo-Code
        --------------------
        -> Initiate the connection cursor
        -> close the cursor
        -> return the status of the cursor whether its closed or not
        """
        
        
        cursor=self.cursor
        cursor.close()
        return cursor.closed 

    def run_query(self, sql_query):
        """
        --------------------
        Description
        --------------------
        -> run_query (method): Class method that executes a SQL query and returns the result as a Pandas dataframe
        --------------------
        Pseudo-Code
        --------------------
        -> initiate a connection cursor
        -> execute the query with the cursor
        -> fetch the data of the query
        -> close the cursor using close_cursor function defined
        -> close connection using close_connection function defined
        -> get the column name since psycopg2 query does not import the column name simultaneously
        -> assign the queries from the cursor to pandas dataframe
        -> rename the panda dataframe column to the column names that have been extracted separately
        -> return the renamed dataframe, include column names and the data.
        """
    
        run_query=self.open_connection()
        cursor=self.open_cursor()
        cursor.execute(sql_query)
        fetch=cursor.fetchall()

        
        #Attaching column names on panda data frame
        
        column_names=[ column[0] for column in cursor.description ]


        df=pd.DataFrame(np.array(fetch))
        df.columns= column_names
        return df

        
        
    def list_tables(self):

        """
        --------------------
        Description
        --------------------
        -> list_tables (method): Class method that extracts the list of available tables using a SQL query (get_tables_list_query())
        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description
        --------------------
        Pseudo-Code
        --------------------
        -> initiate the query imported from the query file
        -> run the query using run_query function defined
        -> return the dataframe pulled from run_query function
        
        
        """

        

        query=get_tables_list_query()  
        return self.run_query(query)
        

    def load_table(self, schema_name, table_name):

        """
        --------------------
        Description
        --------------------
        -> load_table (method): Class method that load the content of a table using a SQL query (get_table_data_query())
        --------------------
        Pseudo-Code
        --------------------
        -> initiate the query imported from the query file
        -> run the query using run_query function defined
        -> return the dataframe pulled from run_query function
        
        """

     
        query=get_table_data_query(schema_name, table_name)       
        return self.run_query(query)
        

    def get_table_schema(self, schema_name, table_name):

        """
        --------------------
        Description
        --------------------
        -> get_table_schema (method): Class method that extracts the schema information of a table using a SQL query (get_table_schema_query())
        --------------------
        Pseudo-Code
        --------------------
        -> initiate the query imported from the query file
        -> run the query using run_query function defined
        -> return the dataframe pulled from run_query function
        """



        
        query=get_table_schema_query(schema_name, table_name)
       
        return self.run_query(query)