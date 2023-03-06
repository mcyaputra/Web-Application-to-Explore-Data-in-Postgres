import streamlit as st
import pandas as pd
import altair as alt
import psycopg2 

from src.database.logics import PostgresConnector
from src.serie_numeric.queries import get_negative_number_query, get_std_query, get_unique_query

class NumericColumn:
    """
    --------------------
    Description
    --------------------
    -> NumericColumn (class): Class that manages a column loaded from Postgres

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
    -> col_mean (int): Average value of a serie (optional)
    -> col_std (int): Standard deviation value of a serie (optional)
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> col_median (int): Median value of a serie (optional)
    -> n_zeros (int): Number of times a serie has values equal to 0 (optional)
    -> n_negatives (int): Number of times a serie has negative values (optional)
    -> histogram (int): Altair histogram displaying the count for each bin value of a serie (optional)
    -> frequent (int): Datframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, schema_name=None, table_name=None, col_name=None, db=None, serie=None):
        self.schema_name = schema_name
        self.table_name = table_name
        self.col_name = col_name
        self.db = db
        self.serie = serie
        self.n_unique = None
        self.n_missing = None
        self.col_mean = None
        self.col_std = None
        self.col_min = None
        self.col_max = None
        self.col_median = None
        self.n_zeros = None
        self.n_negatives = None
        self.histogram = None
        self.frequent = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Numeric section of Streamlit app 

        --------------------
        Parameters
        --------------------

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        self.is_serie_none()
        self.set_unique()
        self.set_missing()
        self.set_zeros()
        self.set_negatives()
        self.set_mean()
        self.set_std()
        self.set_min()
        self.set_max()
        self.set_median()
        self.set_histogram()
    

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        -> serie: Pandas serie loading the content of a column 

        --------------------
        Pseudo-Code
        --------------------
        if self.serie is None, return a message saying 'self.serie is none', if self.serie is empty, 
        return a message saying 'self.serie is empty'

        --------------------
        Returns
        --------------------
        -> (string): 'self.serie is none' if self.serie is None
        -> (string): 'self.serie is empty' if self.serie is empty

        """
        check_serie_empty = self.serie.empty
        return check_serie_empty

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a column using a SQL query (get_unique_query())

        --------------------
        Parameters
        --------------------
        -> schema_name (str): Name of the dataset schema 
        -> table_name (str): Name of the dataset table (mandatory)
        -> col_name (str): Name of the column (mandatory)

        --------------------
        Pseudo-Code
        --------------------
        -> return the unique values of a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (list) return the unique values of a column in a loaded postgres sql table

        """
        query = get_unique_query(self.schema_name, self.table_name, self.col_name)
        self.db.open_connection()
        cursor=self.db.open_cursor()
        cursor.execute(query)
        fetch=cursor.fetchall()
        self.n_unique=pd.DataFrame(fetch)
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
        -> serie: Pandas serie loading the content of a column 

        --------------------
        Pseudo-Code
        --------------------
        -> return the number of missing values of a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (int) return the number of missing values of a column in a loaded postgres sql table

        """
        self.n_missing = self.serie.isnull().sum()
        return self.n_missing

    def set_zeros(self):
        """
        --------------------
        Description
        --------------------
        -> set_zeros (method): Class method that computes the number of times a serie has values equal to 0

        --------------------
        Parameters
        --------------------
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> return the count of values equal to 0 of a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (int) return the count of values equal to 0 of a column in a loaded postgres sql table

        """
        self.n_zeroes = (self.serie == 0).sum()
        return self.n_zeroes

    def set_negatives(self):
        """
        --------------------
        Description
        --------------------
        -> set_negatives (method): Class method that computes the number of times a serie has negative values using a SQL query (get_negative_number_query())

        --------------------
        Parameters
        --------------------
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> return the count of negative values in a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (list) return the count of negative values in a column in a loaded postgres sql table

        """
        self.n__negatives = (self.serie < 0).sum()
        return self.n_negatives

    def set_mean(self):
        """
        --------------------
        Description
        --------------------
        -> set_mean (method): Class method that computes the average value of a serie

        --------------------
        Parameters
        --------------------
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> return the mean of a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (float) return the mean of a column in a loaded postgres sql table

        """
        self.col_mean = round(self.serie.mean(),2)
        return self.col_mean

    def set_std(self):
        """
        --------------------
        Description
        --------------------
        -> set_std (method): Class method that computes the standard deviation value of a serie using a SQL query (get_std_query)

        --------------------
        Parameters
        --------------------
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> return the standard deviation value of a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (float) return the standard deviation value of a column in a loaded postgres sql table

        """
        query=get_std_query(self.schema_name, self.table_name, self.col_name)
        self.db.open_connection()
        cursor=self.db.open_cursor()
        cursor.execute(query)
        fetch=cursor.fetchall()
        self.col_std=pd.DataFrame(fetch)
        return self.col_std
    
    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie

        --------------------
        Parameters
        --------------------
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> return the minimum value of a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (int) return the minimum value of a column in a loaded postgres sql table

        """
        self.col_min = self.serie.min()
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
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> return the maximum value of a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (int) return the maximum value of a column in a loaded postgres sql table

        """
        self.col_max = self.serie.max()
        return self.col_max

    def set_median(self):
        """
        --------------------
        Description
        --------------------
        -> set_median (method): Class method that computes the median value of a serie

        --------------------
        Parameters
        --------------------
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> return the median of a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (int) return the median of a column in a loaded postgres sql table

        """
        self.col_median = self.serie.median()
        return self.col_median

    def set_histogram(self):
        """
        --------------------
        Description
        --------------------
        -> set_histogram (method): Class method that computes the Altair histogram displaying the count for each bin value of a serie

        --------------------
        Parameters
        --------------------
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> displaying the Altair histogram displaying the count for each bin value of a serie

        --------------------
        Returns
        --------------------
        -> (histogram) the Altair histogram displaying the count for each bin value of a serie

        """

        serie = self.serie
        serie.columns = self.col_name
        serie = pd.DataFrame(serie)
        serie = serie.astype(int)
        self.histogram = alt.Chart(serie).mark_bar().encode(
            x = alt.X(f'{self.col_name}'),
            y= alt.Y('count()')
        )
        return self.histogram

    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie

        --------------------
        Parameters
        --------------------
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> return the most frequent value of a column in a loaded postgres sql table

        --------------------
        Returns
        --------------------
        -> (int) return the most frequent value of a column in a loaded postgres sql table

        """
        value = self.serie.value_counts()
        percentage = self.serie.value_counts(normalize=True)
        self.frequent={'value': value.index,
               'occurence': value.values,
               'percentage': percentage.values}

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
        -> serie: Pandas serie loading the content of a column

        --------------------
        Pseudo-Code
        --------------------
        -> formats requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Returns
        --------------------
        -> the requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        """
        self.set_data()
        overall_df = {'Description': ['Number of Unique Values', 
        'Number of Rows with Missing Values', 'Number of Rows with 0', 'Number of Rows with Negative Values', 
        'Average Value' , 'Standard Deviation Value' , 'Minimum Value' , 
        'Maximum Value' , 'Median Value'], 
        'Value':[self.n_unique, self.n_missing, self.n_zeros, self.n_negatives, self.col_mean, self.col_std, 
        self.col_min, self.col_max, self.col_median]}
        overall_section_df = pd.DataFrame(overall_df)
        return overall_section_df