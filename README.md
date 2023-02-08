## Description

Containerised (Docker) interactive web application (Streamlit) built on Python to help users explore their data or tables. The web application helps user connects to a database (Postgres), allowing user to access and display the content of the database.

After successful connection, web app will display:

1. Menu to connect to a database
2. Dropdown to select available tables in database
3. 5 tabs: Overall, Explore, Numeric, Text and Date

The 5 tabs containing information about the table selected are
Overall, Explore, Numeric, Text and Date tabs.

1.  ***Overall tab***: contains general overview of the dataset
    including number of rows and columns, table name,
    total duplicated rows and missing values. It also displays
    schema information such as data types and primary/foreign key of
    each column in the table.

2.  ***Explore tab***: In this tab, users will be able to explore the rows
    and columns of the dataset. It provides options for users to see the top or bottom rows and random samples.
    Users can also adjust the number of rows they want to see at a given time.

3.  ***Numeric tab***: provides more detailed information of the dataset,
    displaying statistical information of numeric columns. Users will
    be able to select numeric columns to analyze, when expanded,
    several statistical information will be shown such as total unique
    values, missing values, negative values, standard deviation, min/max
    and median values. Histogram will show the
    distribution of the values in the column as well as a table
    containing more detailed information on most frequently found
    values.

4.  ***Text tab***: similar to the numeric tab, contains statistical
    information of text columns. Users will also be able to select the
    text columns to analyze and when expanded, statistical information
    shown includes the total number of unique and missing values, lower
    or upper case characters, empty strings and the mode. Barchart is
    used to show the distribution or count of each value in the selected
    column, with more detailed information displayed in the following
    table.

5.  ***Date tab***: similar to numeric and text tabs, holds statistical
    details on date time columns in the dataset. Users select columns
    they are interested in and statistical data will be provided such as
    min/max dates, number of weekday/weekend dates, missing/unique
    values and future dates. Barchart is also included to give better
    visuals on the distribution of the values with the details further
    provided in the following table.

<img src='/Images/Diagram.png'>

## Setting up

1. Install Docker from www.docker.com

2. Go to: https://github.com/mcyaputra/Postgres-Docker-Streamlit-Database-Explorer-Web-App
3. Go to "Code" drop down and select "Download Zip" - This will download the entire repository to your local machine

OR


4. In terminal, type: git clone https://github.com/mcyaputra/Postgres-Docker-Streamlit-Database-Explorer-Web-App.git - This will also download the entire repository to your local machine
5. Save/move project in your designated folder

## Starting the web app

1. Set terminal working directory to the project folder/location
2. In terminal, type "docker compose up -d"
3. Go to browser, type "localhost:8501"

Note: Pre installation of Python, Postgres, Streamlit etc are not necessary. Dockerfile and Dockercompose will set up required environment for the application to run on your machine.

## Citations

<Mention authors and provide links code you source externally>
