import streamlit as st
import pandas as pd
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
import urllib.parse 

MONGO_DB_NAME = 'ETL_DB'

# takes a dict of dataframes and returns the last version from the first worksheet
#  

def insert_data_to_mongo(db, collection_name, records):
    st.header("insert data")

    collection = db[collection_name]
    st.write(records)
    #records = df.to_dict(orient='records')
    #st.write(records)
    st.write(type(records))
    st.write(records.keys())
    for key, value in records.items():
        print(f"{key}: {value}")
        v=value.to_dict(orient='records')
        #st.write(v)
        records[key] = v
        
    st.write(records)
    st.write(type(records))
    #list_from_dict = list(records.items())

    collection.insert_one(records)


def get_workbook_version(df):
    st.write(df.keys())
    res=list(df)[0]
    st.write(res)
    res_content = df[res]
    st.write(res_content)
    last_version =res_content['Version'].iloc[-1] 
    return last_version

def persist_df(df):
    st.write("persisting ... ")
    username = 'hanaashammad'
    u_name = ''
    pswd = ''
    username = urllib.parse.quote_plus(u_name)
    password = urllib.parse.quote_plus(pswd)
    uri =  "mongodb+srv://" +username+':'+password+ '@etlcluster.regns8u.mongodb.net' #[/[database][?options]]
    st.write(uri)
    client=MongoClient(uri)
    st.write(client)
   
    st.write(client)
    # Send a ping to confirm a successful connection
    
    st.write('Try block')
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    st.write('Pinged your deployment. You successfully connected to MongoDB!')
    st.write(client.list_database_names())
    db_names = client.list_database_names()
    db=client[db_names[0]]
    st.write(type(db))
    st.write(db.list_collection_names())
    coll_name = "ETL_COLL"
    st.write(coll_name)
    st.write(" ===  they type of the DF")
    st.write(type(df))
    insert_data_to_mongo(db, coll_name, df)


    
    



uploaded_file = st.file_uploader("Select the MEV list file:", type="xlsx")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name=None)
    #df = pd.read_excel(uploaded_file)
    st.write(type(df))

    #st.write(get_workbook_version(df))
    st.header('before calling persitence module')
    st.write(df)
    persist_df(df)




