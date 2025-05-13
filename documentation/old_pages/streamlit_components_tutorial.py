# streamlit_components_tutorial.py
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time
import plotly.express as px



def main():
    st.title("Streamlit UI Components Tutorial")
    # Sidebar Navigation
    section = st.sidebar.radio(
        "Choose a section",
        ["Basic Components", "Layout", "Input Widgets", "Charts & Media", "Advanced Components"]
    )
    if section == "Basic Components":
        show_basic_components()
    elif section == "Layout":
        show_layout_options()
    elif section == "Input Widgets":
        show_input_widgets()
    elif section == "Charts & Media":
        show_charts_and_media()
    else:
        show_advanced_components()


def show_basic_components():
    st.header("Basic Text Components")
    # ... [Code from above]
    st.subheader("1. Text Elements")
    st.write("Basic text using st.write()")
    st.text("Fixed width text using st.text()")
    st.markdown("**Markdown** formatting is *supported*")
    st.latex(r"E = mc^2")
    st.code("print('Hello, World!')", language='python')
    st.subheader("2. Status Elements")
    st.success("Success message")
    st.info("Info message")
    st.warning("Warning message")
    st.error("Error message")
    st.subheader("3. Progress Indicators")
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
    with st.spinner("Loading..."):
        pass  # Simulating work


def show_layout_options():
    st.header("Layout Options")
    # ... [Code from above]
    st.subheader("1. Columns")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Column 1")
        st.button("Button 1")
    with col2:
        st.write("Column 2")
        st.button("Button 2")
    with col3:
        st.write("Column 3")
        st.button("Button 3")
    st.subheader("2. Containers")
    with st.container():
        st.write("This is inside a container")
        st.button("Container Button")
    st.subheader("3. Expanders")
    with st.expander("Click to expand"):
        st.write("Hidden content revealed!")
        st.image("https://placehold.co/600x400")
    st.subheader("4. Tabs")
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    with tab1:
        st.write("Content for tab 1")
    with tab2:
        st.write("Content for tab 2")




def show_input_widgets():
    st.header("Input Widgets")
    # ... [Code from above]
    st.subheader("1. Text Inputs")
    text_input = st.text_input("Enter some text")
    text_area = st.text_area("Multiline text")
    st.subheader("2. Numeric Inputs")
    number = st.number_input("Enter a number", min_value=0, max_value=100)
    slider = st.slider("Select a range", 0, 100, (25, 75))
    st.subheader("3. Selection Widgets")
    option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
    options = st.multiselect("Select multiple options", ["Choice 1", "Choice 2", "Choice 3", "Choice 4"])
    st.subheader("4. Date and Time")
    date = st.date_input("Select a date")
    time_input = st.time_input("Set a time")
    st.subheader("5. File Uploader")
    uploaded_file = st.file_uploader("Choose a file")
    st.subheader("6. Forms")
    with st.form("my_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        submit = st.form_submit_button("Submit")
        if submit:
            st.write(f"Submitted: {name}, {age}")


def show_charts_and_media():
    st.header("Charts and Media")
    # ... [Code from above]
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
    st.subheader("1. Line Chart")
    st.line_chart(chart_data)
    st.subheader("2. Area Chart")
    st.area_chart(chart_data)
    st.subheader("3. Bar Chart")
    st.bar_chart(chart_data)
    st.subheader("4. Plotly Scatter Chart")
    chart_data['size'] = np.abs(chart_data['C']) * 20 + 10
    fig = px.scatter(
        chart_data,
        x='A',
        y='B',
        size='size',
        title='Scatter Plot with Varying Point Sizes'
    )
    st.plotly_chart(fig)
    st.subheader("5. Images")
    st.image("https://placehold.co/600x400", caption="Sample Image")
    st.subheader("6. Video")
    st.video("https://youtu.be/PRCFO-Z8k94")


def show_advanced_components():
    st.header("Advanced Components")
    # ... [Code from above]
    @st.cache_data
    def expensive_computation(a, b):
        return a + b
    
    st.subheader("1. Session State")
    if 'count' not in st.session_state:
        st.session_state.count = 0
    if st.button("Increment"):
        st.session_state.count += 1
    st.write("Count:", st.session_state.count)
    st.subheader("2. Cached Computation")
    result = expensive_computation(10, 20)
    st.write("Cached Result:", result)
    st.subheader("3. Custom HTML/CSS")
    st.markdown("""
        <style>
        .custom-text {
            color: red;
            font-size: 20px;
        }
        </style>
        <p class='custom-text'>Styled text using HTML and CSS!</p>
""", unsafe_allow_html=True)
    st.subheader("4. Fun Elements")
    if st.button("Celebrate"):
        st.balloons()

if __name__ == "__main__":
    main()