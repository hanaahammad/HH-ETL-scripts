import streamlit as st
import pandas as pd


data = {
    'Country': ['United States', 'Canada', 'Germany', 'France', 'Japan'],
    'Capital': ['Washington, D.C.', 'Ottawa', 'Berlin', 'Paris', 'Tokyo']
}


df = pd.DataFrame(data)
print(df)
print(type(df))
st.title('Countries and Their Capitals')

event = st.dataframe(
    df,
    on_select='rerun',
    selection_mode='single-row'
)

if len(event.selection['rows']):
    print(type(event))
    print(type(event.selection))
    st.write(event, type(event))
    st.write(event.selection, type(event.selection)) 
    selected_row = event.selection['rows'][0]
    
    country = df.iloc[selected_row]['Country']
    capital = df.iloc[selected_row]['Capital']

    st.session_state['country_data'] = {'country': country, 'capital': capital}
    st.page_link('pages/st_detail.py', label=f'Goto {country} Page', icon='🗺️')
