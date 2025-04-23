import streamlit as st
import numpy as np
import pandas as pd
import util.connect_to_cs as cs

st.header("Connecting to Vantage example")

returned_data = cs.establish_TD_connection()
st.write(returned_data)
