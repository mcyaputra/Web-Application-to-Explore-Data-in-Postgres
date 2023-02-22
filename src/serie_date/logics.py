from locale import normalize
import streamlit as st
import pandas as pd
import altair as alt

from src.database.logics import PostgresConnector
from src.serie_date.queries import get_min_date_query, get_weekend_count_query, get_1900_count_query

class DateColumn:
    """
    --------------------
    Description
    --------------------
    -> DateColumn (class): Class that manages a column loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> schema_name (str): Name of the dataset schema (mandatory)
    -> table_name (str): Name of the dataset table (mandatory)
    -> col_name (str): Name of the column (mandatory)
    -> db (PostgresConnector): Instantation of PostgresConnector class for handling Postgres connection (mandatory)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (mandatory)
    -> n_unique (int): Number of unique value of a serie (optional)
    -> n_missing (int): Number of missing values of a serie (optional)
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> n_weekend (int): Number of times a serie has dates falling during weekend (optional)
    -> n_weekday (int): Number of times a serie has dates not falling during weekend (optional)
    -> n_future (int): Number of times a serie has dates falling in the future (optional)
    -> n_empty_1900 (int): Number of times a serie has dates equal to '1900-01-01' (optional)
    -> n_empty_1970 (int): Number of times a serie has dates equal to '1970-01-01' (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
    -> frequent (int): Dataframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, schema_name=None, table_name=None, col_name=None, db=None, serie=None):
        self.schema_name = schema_name
        self.table_name = table_name
        self.col_name = col_name
        self.db = db
        self.serie = serie
        self.n_unique = None
        self.n_missing = None
        self.col_min = None
        self.col_max = None
        self.n_weekend = None
        self.n_weekday = None
        self.n_future = None
        self.n_empty_1900 = None
        self.n_empty_1970 = None
        self.frequent = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Date section of Streamlit app 

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Initiating class method to check if the columns is empty
        Initiating class method to calculate total unique values
        Initiating class method to calculate total missing values
        Initiating class method to extract the minimum value of the column
        Initiating class method to extract the maximum value of the column
        Initiating class method to extract total number of weekend dates
        Initiating class method to extract total number of weekday dates
        Initiating class method to extract total number of future dates
        Initiating class method to extract total number of times a serie has dates equal to '1900-01-01'
        Initiating class method to extract total number of times a serie has dates equal to '1970-01-01'
        Initiating class method to extract top 20 most frequent values
        Initiating class method to display barchart showing total count of each values in the column
        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """

        self.is_serie_none()
        self.set_unique()
        self.set_missing()
        self.set_min()
        self.set_max()
        self.set_weekend()
        self.set_weekday()
        self.set_future()
        self.set_empty_1970()
        self.set_empty_1970()
        self.set_frequent()
        self.set_barchart()

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Check if the column is empty and store the result in a variable
        Return variable containing the result

        --------------------
        Returns
        --------------------
        (bool): whether the dataset is empty or not

        """
        check_serie_empty = self.serie.empty
        return check_serie_empty

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a serie

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calculate total number of unique values and store the result in a variable
        Return variable containing the result

        --------------------
        Returns
        --------------------
        (int): total number of unique values

        """
        self.n_unique = self.serie.nunique(dropna=True)
        return self.n_unique

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie

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
        (int): total number of missing values

        """
        self.n_missing = self.serie.isnull().sum()
        return self.n_missing

    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie using a SQL query (get_min_date_query())

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calling the function from queries.py containing SQL query to extract the minimum value of the column and save it to a variable
        Running the query and save the result to an instance variable
        Return the instance variable containing the result

        --------------------
        Returns
        --------------------
        (datetime): minimum value of the column

        """

        sql_query = get_min_date_query(self.schema_name, self.table_name, self.col_name)
        self.col_min = self.db.run_query(sql_query)
        return self.col_min

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Setting SQL query to extract the maximum value of the column and save it to a variable
        Running the query and save the result to an instance variable
        Return the instance variable containing the result

        --------------------
        Returns
        --------------------
        (datetime): maximum value of the column

        """
        sql_query = (f"SELECT max({self.col_name}) FROM {self.schema_name}.{self.table_name}")
        self.col_max = self.db.run_query(sql_query)
        return self.col_max

    def set_weekend(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekend (method): Class method that computes the number of times a serie has dates falling during weekend using a SQL query (get_weekend_count_query())

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calling the function from queries.py containing SQL query to calculate total number of weekend dates and save it to a variable
        Running the query and save the result to an instance variable
        Return the instance variable containing the result

        --------------------
        Returns
        --------------------
        (int): total number of weekend dates

        """

        sql_query = get_weekend_count_query(self.schema_name, self.table_name, self.col_name)
        self.n_weekend = self.db.run_query(sql_query)
        return self.n_weekend

    def set_weekday(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekday (method): Class method that computes the number of times a serie has dates not falling during weekend

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Setting SQL query to calculate total number of weekday dates and save it to a variable
        Running the query and save the result to an instance variable
        Return the instance variable containing the result

        --------------------
        Returns
        --------------------
        (int): total number of weekday dates

        """
        sql_query = (f"SELECT COUNT({self.col_name}) FROM {self.schema_name}.{self.table_name} WHERE extract(DOW FROM {self.col_name}) IN (1,2,3,4,5)")
        self.n_weekday = self.db.run_query(sql_query)
        return self.n_weekday

    def set_future(self):
        """
        --------------------
        Description
        --------------------
        -> set_future (method): Class method that computes the number of times a serie has dates falling in the future

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calculating the total number of future dates and save it to a variable
        Return the variable containing the result

        --------------------
        Returns
        --------------------
        (int): total number of future dates

        """
        self.n_future = sum(self.serie > pd.Timestamp('now'))
        return self.n_future

    def set_empty_1900(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1900 (method): Class method that computes the number of times a serie has dates equal to '1900-01-01' using a SQL query (get_1900_count_query())

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Calling the function from queries.py containing SQL query to calculate total number of times a serie has dates equal to '1900-01-01' and save it to a variable
        Running the query and save the result to an instance variable
        Return the instance variable containing the result

        --------------------
        Returns
        --------------------
        (int): total number of times a serie has dates equal to '1900-01-01'

        """

        sql_query = get_1900_count_query(self.schema_name, self.table_name, self.col_name)
        self.n_empty_1900 = self.db.run_query(sql_query)
        return self.n_empty_1900

    def set_empty_1970(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1970 (method): Class method that computes the number of times a serie has dates equal to '1970-01-01'

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Setting SQL query to calculate total number of times a serie has dates equal to '1970-01-01' and save it to a variable
        Running the query and save the result to an instance variable
        Return the instance variable containing the result

        --------------------
        Returns
        --------------------
        (int): total number of times a serie has dates equal to '1970-01-01'

        """
        
        sql_query = (f"SELECT COUNT(*) FROM {self.schema_name}.{self.table_name} WHERE {self.col_name} = '1970-01-01'")
        self.n_empty_1970 = self.db.run_query(sql_query)
        return self.n_empty_1970


    def set_barchart(self):  
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Saving the serie to a shorter variable
        Assigning name to serie's column
        Converting the serie to pandas dataframe
        Converting the serie to string data type
        Setting up Altair bar chart
        Return the barchat as a result

        --------------------
        Returns
        --------------------
        (barchart): Altair barchart

        """

        serie = self.serie
        serie.columns = self.col_name
        serie = pd.DataFrame(serie)
        serie = serie.astype(str)
        barchart = alt.Chart(serie).mark_bar().encode(
            x = alt.X(f'{self.col_name}'),
            y= alt.Y('count()')
        )
        return barchart
      
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie

        --------------------
        Parameters
        --------------------
        End: number of rows

        --------------------
        Pseudo-Code
        --------------------
        Counting number of value and save it to a variable
        Calculating the number of times each value showing up against the total count of values in percentage and save it to a variable
        Setting up the table to show the result and save it to instance variable
        Return the instance variable containing the table

        --------------------
        Returns
        --------------------
        (table): table containing the mode

        """
        value = self.serie.value_counts()
        percent = self.serie.value_counts(normalize=True)
        self.frequent={'value': value.index,
               'occurence': value.values,
               'percentage': percent.values}

        return self.frequent

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

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
        overall_df = {'Description':['Number of Unique Values', 'Number of Rows with Missing Values', 'Number of Weekend Dates', 'Number of Weekday Dates', 'Number of Dates in Future', 'Number of Rows with 1900-01-01', 'Number of Rows with 1970-01-01', 'Minimum Value', 'Maximum Value'], 'Value':[self.n_unique, self.n_missing, self.n_weekend, self.n_weekday, self.n_future, self.n_empty_1900, self.n_empty_1970, self.col_min, self.col_max]}
        overall_section_df = pd.DataFrame(overall_df)
        return overall_section_df


