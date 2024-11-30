## [create Import CSV page](https://claude.ai/chat/1155b0a5-38a0-4e0f-a230-a1c52fdd5612)

You are an expert streamlit app developer, please help me create an single-page app to import multiple CSV files into a SQLite database

Below are the exact requirements. 

This page should have 4 sections

### Upload CSV
- text_input field to specify dataset name
- "Create" button: a folder will be created under subfolder called "db"
- upload CSV files: those files are placed in "db/<dataset_name>/" sub-folder 
- create an SQLite database file called <dataset_name>.sqlite3 under subfolder called "db"

### Review data
One can review data from CSV files, additionally revises table schema definitions if necessary

For each CSV file, use pandas to create dataframe
- create table_name out of csv filename
- convert CSV header into table column names (normal column header into snake_case column names)
- show sample data from 5 rows 
- give user the option to rename table name, column names

### Create tables
- display DDL script for all the tables to be created
- add a button called "Create Tables"

### Load data
- add a button called "Load Data" to import all CSV data into respective tables

I will verify and test your streamlit app and iterate properly