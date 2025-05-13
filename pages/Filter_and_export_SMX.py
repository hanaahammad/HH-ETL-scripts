
import streamlit as st
import openpyxl
import pandas as pd



# Initialize session state: 
# we need the system tab contents to remain in the session
#if 'system_tab' not in st.session_state:
   # st.session_state.system_tab = ''#


sheet_names=[]

data_file = st.file_uploader("Upload Excel file",type=['xlsx'])  

if data_file:
    
    wb = openpyxl.load_workbook(data_file)
    sheet_names = wb.sheetnames
    st.write(sheet_names)
    #st.write(type(sheet_names))
    # fill the combo box with the system codes and names
    df=pd.read_excel(data_file,"System")
    st.session_state.system_tab = df

    selection =tuple(df.columns) 
    #st.write(selection)

    selection=tuple(df['Source System Alias'])
    #st.write(selection)

    option = st.selectbox("What do you want to generate?", 
                          selection, index=None, 
                          placeholder="Select contact method...",)

    st.write("You selected:", option)
    st.header(option)
    if option:
        # filtering stream tabs on the selected System Name
        st.write(f':blue[filtering the stream tab on {option}]')
        df =pd.read_excel(data_file,"Stream")
        df_s= df[(df['System Name']==option)]
        st.dataframe(df_s)
        st.markdown("""---""")

        st.write(f':blue[filtering the STG tables tab on {option}]')
        df=pd.read_excel(data_file,"STG Tables")
        df_STG_Tables = df[(df['Source System Alias']==option)]
        st.dataframe(df_STG_Tables)  
        st.markdown("""---""")    

        st.write(f':blue[filtering the BKEY tab on {option}]')
        df=pd.read_excel(data_file,"BKEY")
        df = pd.read_excel(data_file,"BKEY")
        #st.write(df.columns)
        #df_BKEY = df[(df['Source System Alias']==option)]
        #st.dataframe(df_STG_Tables)  
        st.markdown("""---""")     

        st.write(f':blue[filtering the BMAP tab on {option}]')
        df=pd.read_excel(data_file,"BMAP")
        df_BMAP = pd.read_excel(data_file,"BMAP")
        st.write(df.columns)
        df_BMAP = df[(df['Code Domain Name']==option)]
        st.dataframe(df_BMAP)  
        st.markdown("""---""")  

        st.write(f':red[filtering the BMAP Values tab on {option}]')
        df = st.session_state.system_tab
        
        st.write(df)
        id = df.loc[df['Source System Alias'] == option, 'Source System ID'].item() 

        df2 =pd.read_excel(data_file,"BMAP Values")

        df_BMAP_values = df2[(df2['Code Domain Id']==id)]
        st.dataframe(df_BMAP_values)  
        st.markdown("""---""")  

         # 
        st.write(f':green[filtering the CORE tables tab on {option}]')

        st.write(f':green[filtering the PL tables tab on {option}]')

        st.write(f':green[filtering the PL Table mapping on {option}]')

        st.write(f':green[filtering the PL Column mapping on {option}]')
        #filter on main source = stg tables.Table name




with st.expander("See Data"):
    st.write('''Showing tabs contents.''')
    if sheet_names !=[]:
        for sheet in sheet_names:
            df = pd.read_excel(data_file,sheet)
            st.header(sheet)
            st.write(df.columns)
            st.dataframe(df)


    