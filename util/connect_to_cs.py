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

def list_objects(database_name='jaffle_shop'):
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


#establish_TD_connection()
#list_objects()
