import teradatasql
import pandas as pd
from dotenv import load_dotenv
import os
from teradataml import *

# Load the .env file
load_dotenv()

# Get environment variables

def create_table(script):
    print(script)

def establish_TD_connection():
    user_name = os.getenv("TD_DB_USER")
    password = os.getenv("TD_DB_PASSWORD")
    host = os.getenv("TD_DB_HOST")
    #db_name = os.getenv("DB_NAME")user_name
    query = 'select top 5 * from jaffle_shop.raw_customers'
    query = 'SELECT DISTINCT DatabaseName FROM DBC.TablesV'
    print(query)
    with teradatasql.connect(host=host, user=user_name, password=password) as connect:
        data = pd.read_sql(query, connect)
        print(data)
    return data, query

def list_objects(database_name='ETLTEST'):
    #'jaffle_shop'
    user_name = os.getenv("TD_DB_USER")
    password = os.getenv("TD_DB_PASSWORD")
    host = os.getenv("TD_DB_HOST")
    query = 'SELECT TOP 5 TableName, DatabaseName FROM DBC.TablesV ORDER BY TableName;'

   
    query = """SELECT DatabaseName , TableName, CreateTimeStamp, LastAlterTimeStamp FROM  DBC.TablesV WHERE   DatabaseName = """ 
    #+ 'jaffle_shop'
    # f"'{A}'  '{B}'"
    query = f"{query} '{database_name}'"
    print(query)
    with teradatasql.connect(host=host, user=user_name, password=password) as connect:
        tables = pd.read_sql(query, connect)
        print(tables)

    #create_context(host = host, username=user_name, password=password)

    #data=db_list_tables(None, 'DBC', 'table')
    return tables, query

def create_core_tables(sql_script):
    print('connect to clear scape : in create core tables =======================')
    print(sql_script)
    user_name = os.getenv("TD_DB_USER")
    password = os.getenv("TD_DB_PASSWORD")
    host = os.getenv("TD_DB_HOST")

    query = sql_script
    
    for query in sql_script:
        print(query)
        print('query type ===========================================')
        print(type(query))
        try:
            with teradatasql.connect(host=host, user=user_name, password=password) as connect:
                response = pd.read_sql(query, connect)
                print(response)
                return response
        except teradatasql.DatabaseError as db_err:
        # Handle any errors that occur during the database connection
            print("Error while connecting to the Teradata database:", db_err)
            return db_err



def create_core(sql_script):
    user_name = os.getenv("TD_DB_USER")
    password = os.getenv("TD_DB_PASSWORD")
    host = os.getenv("TD_DB_HOST")
    try:
    # Establish a connection to the Teradata database
        with teradatasql.connect(host=host, user=user_name, password=password) as con:
        # Create a cursor to execute queries
            with con.cursor() as cur:
                try:
                    # Creating the table SampleEmployee
                    cur.execute (f"CREATE SET TABLE {USER}.SampleEmployee \
                            (Associate_Id     INTEGER, \
                            Associate_Name   CHAR(25), \
                            Job_Title        VARCHAR(25)) \
                            UNIQUE PRIMARY INDEX (Associate_Id);")
                
                    print(f"Sample table {user_name}.SampleEmployee created.")

                except teradatasql.DatabaseError as db_err:
                # Handle any errors that occur during query execution
                    print("Error while executing the query:", db_err)

    except teradatasql.DatabaseError as db_err:
    # Handle any errors that occur during the database connection
        print("Error while connecting to the Teradata database:", db_err)
