import streamlit as st
import numpy as np
import pandas as pd
import util.connect_to_cs as cs


import streamlit as st

#@st.cache_data
def connect_and_show_data():
    # Fetch data from URL here, and then clean it up.
    returned_data =  cs.establish_TD_connection()
    return returned_data


# Actually executes the function, since this is the first time it was
# encountered.

st.header("Connecting to Vantage example")
if st.button('connect'):
    #code = '''def hello():
    #print("Hello, Streamlit to Teradata!")'''
    #st.code(code)
    #st.write('This page uses the utility connect to clearscape')
    d1 = connect_and_show_data()
    st.write(d1)
    if st.button('list database tables'):
        st.header('listing a database table')
        tables = cs.list_objects()
        st.write(tables)



#st.write(type(returned_data))

