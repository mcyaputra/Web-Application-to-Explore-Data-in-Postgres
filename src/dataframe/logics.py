import pandas as pd
import streamlit as st
import datetime

from src.database.logics import PostgresConnector
from src.dataframe.queries import get_numeric_tables_query, get_text_tables_query, get_date_tables_query


class Dataset:
    """
    --------------------
    Description
    --------------------
    -> Dataset (class): Class that manages a dataset loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> schema_name (str): Name of the dataset schema (mandatory)
    -> table_name (str): Name of the dataset table (mandatory)
    -> db (PostgresConnector): Instantation of PostgresConnector class for handling Postgres connection (mandatory)
    -> df (pd.Dataframe): Pandas dataframe where the table content has been loaded (mandatory)
    -> n_rows (int): Number of rows of dataset (optional)
    -> n_cols (int): Number of columns of dataset (optional)
    -> n_duplicates (int): Number of duplicated rows of dataset (optional)
    -> n_missing (int): Number of missing values of dataset (optional)
    -> num_cols (list): List of columns of numerical type (optional)
    -> text_cols (list): List of columns of text type (optional)
    -> date_cols (list): List of columns of datetime type (optional)
    """
    def __init__(self, schema_name=None, table_name=None, db=None, df=None):
        self.schema_name = schema_name
        self.table_name = table_name
        self.db = db
        self.df = df
        self.n_rows = None
        self.n_cols = None
        self.n_duplicates = None
        self.n_missing = None
        self.num_cols = None
        self.text_cols = None
        self.date_cols = None
        self.schema_df = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.df to be displayed in the Overall section of Streamlit app 

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Initiating class method to calculate total number rows and columns
        Initiating class method to calculate total duplicate values
        Initiating class method to calculate total missing values
        Initiating class method to extract list of numeric columns
        Initiating class method to extract list of text columns
        Initiating class method to extract list of date columns
        Initiating class method to extract the first n rows of the dataset
        Initiating class method to extract the last n rows of the dataset
        Initiating class method to extract n random samples of the dataset

        --------------------
        Returns
        --------------------
        (int): total number of rows and columns
        (int): total duplicate values
        (int): total missing values
        (str): list of numeric columns
        (str): list of text columns
        (str): list of date columns
        (table): first n rows of the dataset
        (table): last n rows of the dataset
        (table): n random samples of the dataset

        """

        self.set_dimensions()
        self.set_duplicates()
        self.set_missing()
        self.set_numeric_columns()
        self.set_text_columns()
        self.set_date_columns()
        self.get_head()
        self.get_tail()
        self.get_sample()
    
    def is_df_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_df_none (method): Class method that checks if self.df is empty or none 

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Check if the dataset is empty and store the result in a variable
        Return variable containing the result
        --------------------
        Returns
        --------------------
        (bool): whether the dataset is empty or not

        """
        check_empty = self.df.empty
        return check_empty

    def set_dimensions(self):
        """
        --------------------
        Description
        --------------------
        -> set_dimensions (method): Class method that computes the dimensions (number of columns and rows) of self.df and store them as attributes (self.n_rows, self.n_cols)

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calculate number of rows in the dataset and save it as an instance variable
        Calculate number of columns in the dataset and save it as an instance variable
        Return the variables containing the results

        --------------------
        Returns
        --------------------
        (int): number of rows and columns

        """
        self.n_rows = self.df.shape[0]
        self.n_cols = self.df.shape[1]
        return self.n_rows, self.n_cols

    def set_duplicates(self):
        """
        --------------------
        Description
        --------------------
        -> set_duplicates (method): Class method that computes the number of duplicated of self.df and store it as attribute (self.n_duplicates)

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calculate number of duplicate values and save it as an instance variable
        Return the variable containing the result

        --------------------
        Returns
        --------------------
        (int): number of duplicate values

        """
        self.n_duplicates = self.df.duplicated().sum()
        return self.n_duplicates

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing values of self.df and store it as attribute (self.n_missing)

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calculate number of missing values and save it as an instance variable
        Return the variable containing the result

        --------------------
        Returns
        --------------------
        (int): number of missing values

        """
        self.n_missing = self.df.isnull().sum().sum()
        return self.n_missing

    def set_numeric_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_numeric_columns (method): Class method that extract the list of numeric columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.num_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calling the function from queries.py containing SQL query to extract numeric columns and save it to a variable
        Running the query and save the result to a variable
        Convert the result to a list and save it to instance variable
        Return the instance variable containing the result

        --------------------
        Returns
        --------------------
        (str): numeric column names

        """

        sql_query = get_numeric_tables_query(self.schema_name, self.table_name)
        num_cols = self.db.run_query(sql_query)
        self.num_cols = list(num_cols['column_name'])
        return self.num_cols
        

    def set_text_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_text_columns (method): Class method that extract the list of text columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.text_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calling the function from queries.py containing SQL query to extract text columns and save it to a variable
        Running the query and save the result to a variable
        Convert the result to a list and save it to instance variable
        Return the instance variable containing the result

        --------------------
        Returns
        --------------------
        (str): text column names

        """

        sql_query = get_text_tables_query(self.schema_name, self.table_name)
        text_cols = self.db.run_query(sql_query)
        self.text_cols = list(text_cols['column_name'])
        return self.text_cols

    def set_date_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_date_columns (method): Class method that extract the list of datetime columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.date_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calling the function from queries.py containing SQL query to extract date columns and save it to a variable
        Running the query and save the result to a variable
        Convert the result to a list and save it to an instance variable
        Return the instance variable containing the result

        --------------------
        Returns
        --------------------
        (str): date column names

        """

        sql_query = get_date_tables_query(self.schema_name, self.table_name)
        date_cols = self.db.run_query(sql_query)
        self.date_cols = list(date_cols['column_name'])
        return self.date_cols       

    def get_head(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_head (method): Class method that computes the first rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        N: Number of rows

        --------------------
        Pseudo-Code
        --------------------
        Extract the first n rows of the dataset and save it to a variable
        Return the variable containing the result

        --------------------
        Returns
        --------------------
        (table): first n rows of the dataset

        """
        first_5_rows = self.df.head(n)
        return first_5_rows

    def get_tail(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_tail (method): Class method that computes the last rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        N: Number of rows

        --------------------
        Pseudo-Code
        --------------------
        Extract the last n rows of the dataset and save it to a variable
        Return the variable containing the result

        --------------------
        Returns
        --------------------
        (table): last n rows of the dataset

        """
        last_5_rows = self.df.tail(n)
        return last_5_rows

    def get_sample(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_sample (method): Class method that computes a random sample of rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        N: Number of rows

        --------------------
        Pseudo-Code
        --------------------
        Extract n sample rows of the dataset and save it to a variable
        Return the variable containing the result

        --------------------
        Returns
        --------------------
        (table): n sample rows of the dataset

        """
        random_sample = self.df.sample(n, replace = True)
        return random_sample

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.df to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Initiate set data function to extract all required information
        Create dataframe, assign values to it and save it to a variable
        Convert the dataframe to pandas dataframe and save it to a variable
        Return the variable containing the result

        --------------------
        Returns
        --------------------
        (table): table containing information for streamlit

        """
        
        self.set_data()
        overall_df = {'Description':['Name of Table', 'Number of Rows', 'Number of Columns', 'Number of Duplicated Rows', 'Number of Rows with Missing Values'], 'Value':[self.table_name, self.n_rows, self.n_cols, self.n_duplicates, self.n_missing]}
        overall_section_df = pd.DataFrame(overall_df)
        return overall_section_df

