import streamlit as st
import numpy as np
import pandas as pd
#import util.connect_to_cs as cs
from util import connect_to_cs as cs



# Initialize session state
if 'conn' not in st.session_state:
    st.session_state.conn = cs.establish_TD_connection()
if 'tables' not in st.session_state:
    st.session_state.tables = cs.list_objects()
if 'show_connection' not in st.session_state:
    st.session_state.show_connection = False
if 'show_tables' not in st.session_state:
    st.session_state.show_tables = False

  

def connect_and_show_data():
    # Fetch data from URL here, and then clean it up.
    returned_data, q =  cs.establish_TD_connection()
    return returned_data, q

def list_tables():
   tables , q=  cs.list_objects()
   return tables, q

# Button callbacks
def toggle_dataframe():
    st.session_state.show_connection = not st.session_state.show_connection

def toggle_plot():
    st.session_state.show_tables = not st.session_state.show_tables

     
# App layout
st.title("Connection to Vantage")
col1, col2 = st.columns(2)

with col1:
    st.button("Connect and show data", on_click=toggle_dataframe)

with col2:
    st.button("List DB Tables", on_click=toggle_plot)


mycomment = """
if button1:
    d1 = connect_and_show_data()
    st.write(d1)
    
   

if button2:
        #st.header('listing a database table')
        tables = cs.list_objects()
        st.write(tables)
"""
# Display dataframe if button is clicked
if st.session_state.show_connection:
    st.subheader("Connection and Sample Data")
    #st.dataframe(st.session_state.df)
    data, q=connect_and_show_data()
    st.code(q)
    st.dataframe(data)
    #st.write(connect_and_show_data())

# Display plot if button is clicked
if st.session_state.show_tables:
    st.subheader("Listing A database Tables")
    d, q = list_tables()
    st.code(q)
    st.dataframe(d)
    #st.write(list_tables)
    

#st.write(type(returned_data))

