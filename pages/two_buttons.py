import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

import random
from faker import Faker

# Create dummy data
def create_dummy_data():
    np.random.seed(0)
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    data = {
        'Date': dates,
        'Sales': np.random.randint(100, 1000, size=len(dates)),
        'Customers': np.random.randint(10, 100, size=len(dates))
    }
    return pd.DataFrame(data)

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = create_dummy_data()
if 'show_dataframe' not in st.session_state:
    st.session_state.show_dataframe = False
if 'show_plot' not in st.session_state:
    st.session_state.show_plot = False

# Button callbacks
def toggle_dataframe():
    st.session_state.show_dataframe = not st.session_state.show_dataframe

def toggle_plot():
    st.session_state.show_plot = not st.session_state.show_plot

# App layout
st.title("Dummy Data Visualization")

col1, col2 = st.columns(2)

with col1:
    st.button("Show/Hide Dataframe", on_click=toggle_dataframe)

with col2:
    st.button("Show/Hide Plot", on_click=toggle_plot)

# Display dataframe if button is clicked
if st.session_state.show_dataframe:
    st.subheader("Sales Data")
    st.dataframe(st.session_state.df)

# Display plot if button is clicked
if st.session_state.show_plot:
    st.subheader("Sales Over Time")
    fig = px.line(st.session_state.df, x='Date', y=['Sales', 'Customers'], 
                  title='Sales and Customers Over Time')
    st.plotly_chart(fig)

st.title('trying switch case')
# Take user input for the day of the week
day =  st.text_input("Enter the day of the week: ")
# Match the day to predefined patterns
match day:
    case "Saturday" | "Sunday":
        st.write(f"{day} is a weekend.")  # Match weekends
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        st.write(f"{day} is a weekday.")  # Match weekdays
    case _:
        st.write("That's not a valid day of the week.")  # Default case