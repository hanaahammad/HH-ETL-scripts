import streamlit as st
import openpyxl
import pandas as pd



st.markdown(
    """<style>
        .element-container:nth-of-type(3) button {
            height: 3em;
        }
        </style>""",
    unsafe_allow_html=True,
)

def check_difference(df1, df2):
    difference = df1[df1!=df2]
    st.write(difference) 

st.header("Sheet view")
data_file = st.sidebar.file_uploader("Upload Excel file",type=['xlsx'])  

if data_file:
    file_details = {
        "Filename":data_file.name,
        "FileType":data_file.type,
        "FileSize":data_file.size}

    wb = openpyxl.load_workbook(data_file)

    ## Show Excel file
    st.sidebar.subheader("File details:")
    st.sidebar.json(file_details,expanded=False)
    st.sidebar.markdown("----")

    ## Select sheet
    sheet_selector = st.sidebar.selectbox("Select sheet:",wb.sheetnames)     
    df = pd.read_excel(data_file,sheet_selector)
    st.markdown(f"### Currently Selected: `{sheet_selector}`")
    st.write(df)
    mycomment = '''
    ## Do something after a button
    doLogic_btn = st.button("➕")
    if doLogic_btn:
        df2 = df.sum().transpose()
        st.write(df2)

        # Do something more after the previous button
        # >> But this will fail because the button will go back to _False_ 
        # >> so nothing will be shown afterwards
        another_btn = st.checkbox("Another +")
        if another_btn:
            df3 = df2.sum()
            st.write(df3)

            '''
    
data_file2 = st.sidebar.file_uploader("Upload the previous Excel file ",type=['xlsx'])  

if data_file2:
    file_details2 = {
        "Filename":data_file2.name,
        "FileType":data_file2.type,
        "FileSize":data_file2.size}

    wb = openpyxl.load_workbook(data_file2)

    ## Show Excel file
    st.sidebar.subheader("File 2 details:")
    st.sidebar.json(file_details2,expanded=False)
    st.sidebar.markdown("----")

    ## Select sheet
    sheet_selector2 = st.sidebar.selectbox("Select sheet from the second file:",wb.sheetnames)     
    df2 = pd.read_excel(data_file2,sheet_selector)
    st.markdown(f"### Currently Selected: `{sheet_selector2}`")
    st.write(df2)
    event = st.dataframe(
        df2,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="multi-row",
        )
    if st.button('compare'):
        check_difference(df, df2)


