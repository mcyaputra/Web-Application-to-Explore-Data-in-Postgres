## Description

This is a Streamlit web application in Python 3.8.2 that is
containerised with Docker. It will explore the content of a Postgres
database and analyse selected tables and columns. The first dropdown
“Streamlit Session State” displays the current session state, and this
is where you can debug the solution. The following menu connects you to
a database and allows you to select a table. Finally 5 different tabs
will allow you to analyse and view the datasets, it will display
information about any text columns, numeric columns and date columns.

The 5 tabs containing information about the database selected are
Overall, Explore, Numeric, Text and Date.

1.  **Overall tab**: contains the general overview of the dataset which
    includes number of rows, number of columns, name of the table,
    number of duplicated rows and missing values. It also provides
    schema information such as data types and primary/foreign key of
    each column in the table.

2.  **Explore tab**: In this tab, users will be able to explore the rows
    and columns of the dataset. It provides options for users to select
    whether they want to see the top or bottom rows and random samples.
    Users can also adjust how many rows they want to see at a time.

3.  **Numeric tab**: provides more detailed information of the dataset,
    it contains statistical information of numeric columns. Users will
    be able to select the numeric columns to analyze, when expanded,
    several statistical data will be shown including total unique
    values, missing values, negative values, standard deviation, min/max
    and median values. Histogram is also displayed to show the
    distribution of the values in the column as well as a table
    containing more detailed information on most frequently found
    values.

4.  **Text tab**: similar to the numeric tab, contains statistical
    information of text columns. Users will also be able to select the
    text columns to analyze and when expanded, statistical information
    shown includes the total number of unique and missing values, lower
    or upper case characters, empty strings and the mode. Barchart is
    used to show the distribution or count of each value in the selected
    column, with more detailed information displayed in the following
    table.

5.  **Date tab**: similar to numeric and text tabs, holds statistical
    details on date time columns in the dataset. Users select columns
    they are interested in and statistical data will be provided such as
    min/max dates, number of weekday/weekend dates, missing/unique
    values and future dates. Barchart is also included to give better
    visuals on the distribution of the values with the details further
    provided in the following table.

<p align="center">
    <img src='Images/Diagram.png">

## How to Setup

In order for the app to connect to the database, we have to figure out
the connection details including the database name, username that has
access to the database, the password corresponding, the host name, and
the port number. It is also important to make sure that the database has
at least one schema and one table, otherwise, the application will not
be able to produce any result.

## How to Run the Program

Start by clicking on the docker compose file and run the compose up command

From there it should establish both sessions and you log into the ip address 0.0.0.0:8501. If docker does not work, follow below step. If not keep going to connect the database section

**If docker is not working:** Open terminal and run: streamlit run
“pathway”

To connect the database, open the expander widget labeled “Streamlit
application for performing data exploration on a database”:

![](2.png?raw=true)

Then put in all of the postgresql connection details to the form, all of
the details must be accurate, otherwise the connection won’t be
established.

![](3.png)

If all of the required information is correct, then clicking the
“connect” button will result in a success message **“Connection to
database established”**.

![](4.png)

Once the connection has been established, then a dropdown menu will pop
up containing tables to be choosed. The next step then is to choose the
table that you want to analyze.

## Project Structure

![](1.png)

## Citations

<Mention authors and provide links code you source externally>
