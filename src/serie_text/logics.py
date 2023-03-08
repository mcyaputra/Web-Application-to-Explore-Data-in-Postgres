import streamlit as st
import pandas as pd
import altair as alt

from src.database.logics import PostgresConnector
from src.serie_text.queries import get_missing_query, get_mode_query, get_alpha_query

class TextColumn:
    """
    --------------------
    Description
    --------------------
    -> TextColumn (class): Class that manages a column loaded from Postgres
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
    -> n_empty (int): Number of times a serie has empty value (optional)
    -> n_mode (int): Mode value of a serie (optional)
    -> n_space (int): Number of times a serie has only space characters (optional)
    -> n_lower (int): Number of times a serie has only lowercase characters (optional)
    -> n_upper (int): Number of times a serie has only uppercase characters (optional)
    -> n_alpha (int): Number of times a serie has only alphabetical characters (optional)
    -> n_digit (int): Number of times a serie has only digit characters (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
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
        self.n_empty = None
        self.n_mode = None
        self.n_space = None
        self.n_lower = None
        self.n_upper = None
        self.n_alpha = None
        self.n_digit = None
        self.barchart = None
        self.frequent = None
    
    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Text section of Streamlit app 
        --------------------
        Parameters
        --------------------

        None

        --------------------
        Pseudo-Code
        --------------------
        
        Initiating class method to check if the columns are empty
        Initiating class method to caculate unique values
        Initiating class method to caculate missing values
        Initiating class method to caculate empty value rows
        Initiating class method to caculate mode value rows
        Initiating class method to caculate rows that contain whitespace
        Initiating class method to caculate rows that contain lowercase
        Initiating class method to caculate rows that contain uppercase
        Initiating class method to caculate rows that contain alphabet
        Initiating class method to caculate rows that contain digits
        Initiating class method to set frequent table
        Initiating class method to set barchart

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description
        """
       
        self.is_serie_none()
        self.set_unique()
        self.set_missing()
        self.set_empty()
        self.set_mode()
        self.set_whitespace()
        self.set_lowercase()
        self.set_uppercase()
        self.set_alphabet()
        self.set_digit()
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
        
        Checks to see if the values contain empty values

        --------------------
        Returns
        --------------------
        (bool): If the dataset is empty or not

        """

        check = self.serie.empty
        return check

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
        
        Caculates the total rows that has unique values and returns as a integer value

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
        -> set_missing (method): Class method that computes the number of missing value of a serie using a SQL query (get_missing_query())
        --------------------
        Parameters
        --------------------
        
        None

        --------------------
        Pseudo-Code
        --------------------
        
        Caculates the total rows that has missing values and returns as a integer value though the missing query function

        --------------------
        Returns
        --------------------
        (int): total number of unqiue values
        

        """
        sql_query = get_missing_query(self.schema_name, self.table_name, self.col_name)
        self.n_missing = self.db.run_query(sql_query)
        return self.n_missing


    def set_empty(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty (method): Class method that computes the number of times a serie has empty value
        --------------------
        Parameters
        --------------------
        
        None

        --------------------
        Pseudo-Code
        --------------------
        
        Caculates the total rows that has empty values and returns as a integer value

        --------------------
        Returns
        --------------------
        (int): total number of empty values
        

        """

        df = pd.DataFrame(self.serie)
        self.n_empty = df.isna().sum()
        return self.n_empty

    def set_mode(self):
        """
        --------------------
        Description
        --------------------
        -> set_mode (method): Class method that computes the mode value of a serie using a SQL query (get_mode_query())
        --------------------
        Parameters
        --------------------
        
        None

        --------------------
        Pseudo-Code
        --------------------
        
        Caculates the total rows that has mode values and returns as a integer value though the mode query function


        --------------------
        Returns
        --------------------
        (int): total number of mode values

        """
        sql_query = get_mode_query(self.schema_name, self.table_name, self.col_name)
        self.n_mode = self.db.run_query(sql_query)
        return self.n_mode

    def set_whitespace(self):
        """
        --------------------
        Description
        --------------------
        -> set_whitespace (method): Class method that computes the number of times a serie has only space characters
        --------------------
        Parameters
        --------------------
        
        None

        --------------------
        Pseudo-Code
        --------------------
        
        Caculates the total rows that has whitespace values and returns as a integer value

        --------------------
        Returns
        --------------------
        (int): Total number of whitespace values
        
        """
        self.n_space= 0
        for i in range(0, len(self.serie)):
            if self.serie[i] == " ":
                self.n_space += 1
        return self.n_space

    def set_lowercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_lowercase (method): Class method that computes the number of times a serie has only lowercase characters
        --------------------
        Parameters
        --------------------
        
        None

        --------------------
        Pseudo-Code
        --------------------
        
        Caculates the total rows that has lowercase values and returns as a integer value

        --------------------
        Returns
        --------------------
        (int): Total number of lowercase values

        """
        lower=0
        index=0
        for i in self.serie[index]:
            index+=1
            if i.islower():
                lower +=1
            else:
                pass

        self.n_lower = lower

        return self.n_lower

    def set_uppercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_uppercase (method): Class method that computes the number of times a serie has only uppercase characters
        --------------------
        Parameters
        --------------------
        
        None

        --------------------
        Pseudo-Code
        --------------------
        
        Caculates the total rows that has uppercase values and returns as a integer value

        --------------------
        Returns
        --------------------
        (int): Total value of uppercase values

        """
        
        upper=0
        index=0
        for i in self.serie[index]:
            index+=1
            if i.islower():
                pass
            else:
                upper+=1

        self.n_upper = upper
        return self.n_upper
    
    def set_alphabet(self):
        """
        --------------------
        Description
        --------------------
        -> set_alphabet (method): Class method that computes the number of times a serie has only alphabetical characters using a SQL query (get_alpha_query())
        --------------------
        Parameters
        --------------------

        None

        --------------------
        Pseudo-Code
        --------------------
        
        Caculates the total rows that has alphabet values and returns as a integer value though the SQL query getalpha

        --------------------
        Returns
        --------------------
        (int): Total rows containing alphabet

        """
        sql_query = get_alpha_query(self.schema_name, self.table_name, self.col_name)
        self.n_alpha = self.db.run_query(sql_query)
        return self.n_alpha

    def set_digit(self):
        """
        --------------------
        Description
        --------------------
        -> set_digit (method): Class method that computes the number of times a serie has only digit characters
        --------------------
        Parameters
        --------------------
        
        None

        --------------------
        Pseudo-Code
        --------------------
        
        Caculates the total rows that only has digit values and returns as a integer value

        --------------------
        Returns
        --------------------
        (int): Total value of digits
        

        """
        
        # self.n_alpha,string=0, self.serie
        # for i in string:
        #     if (i.isalpha()):
        #         self.n_alpha +=1

        # self.n_digit = len(string)-self.n_alpha

        self.n_digit = self.serie.str.count(r'[0-9]')

        return self.n_digit

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
        
        Caculates the count based on each value and creates a bargraph on the frequenecy of values

        --------------------
        Returns
        --------------------
        (int): The barchart value

        """
        serie = self.serie
        serie.columns = self.col_name
        serie = pd.DataFrame(serie)
        serie = serie.astype(str)
        self.barchart = alt.Chart(serie).mark_bar().encode(
            x = alt.X(f'{self.col_name}'),
            y= alt.Y('count()')
        )
        return self.barchart
      
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie
        --------------------
        Parameters
        --------------------
        
        None

        --------------------
        Pseudo-Code
        --------------------
        
        Computes the frequent values of a series and percentage

        --------------------
        Returns
        --------------------
        (int): Frequent values

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
        
        Creates a table that contains all the classes that is used like unique values, missing values, empty rows etc.

        --------------------
        Returns
        --------------------
        (int): Table containing information mostly integers
        
        """
        self.set_data()
        overall_df = {'Description': ['Number Of Unique Values', 
        'Number of Rows with Missing Values', 'Number of Empty Rows', 
        'Number of Rows with Only Whitespace' , 'Number of Rows with Only Lowercases' , 'Number of Rows with Only Uppercases' , 
        'Number of Rows with Only Alphabet' , 'Number of Rows with Only Digits', 'Number of mode value in a serie'], 
        'Value':[self.n_unique, self.n_missing, self.n_empty, 
        self.n_space, self.n_lower, self.n_upper, self.n_alpha, self.n_digit, self.n_mode]}
        overall_section_df = pd.DataFrame(overall_df)
        return overall_section_df
