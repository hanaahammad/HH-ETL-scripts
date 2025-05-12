import pandas as pd
import util.concat_util as cu
from datetime import datetime

import streamlit as st

#the_file_to_read = "file_example_XLSX_5000.xlsx"
#the_file_to_read = "WAVEZ_SMX_Version_0.1.xlsx"

#xl.parse(sheet_name)  
 
def get_sheets(xl):
    print(type(xl))
    sheet_names = xl.sheet_names  # see all sheet names
    print(sheet_names)
    return sheet_names



#df_names from sheet names
def df_names(sheet_names) :
    print("====================================")
    print(sheet_names)
    print(type(sheet_names))
    signals = [s.replace(" ",'') for s in sheet_names]
    print(signals)
    df_names = list(map(lambda x: 'df_' + x , signals))
    print(df_names)
    return df_names


# this part is used to check
'''
for tab in sheet_names:
    print(tab)
    # data=pd.read_excel(the_file_to_read, tab)
    # print(data)
    tab_content =xl.parse(tab)
    print(tab_content)
    #data=xl.(tab) 
    #print(data)
'''



def read_tabs_contents(xl, tabs):
    content_list = [xl.parse(t) for t in tabs]
    return content_list
     

def process_system_tab(sheet_content):
    print("============= process system tab ==============")
   
    print(sheet_content.columns)
    '''
    (['Source System ID', 'Source System Name', 'Source System Alias',
       'Schema', 'Loading Type', 'Source Type']
    EXEC GCFR_Register_System('1','/','CB','Core Banking');
    '''
    pref = "EXEC GCFR_Register_System( "
    sufx = ");"
    #new_sheet_content =  pd.DataFrame(sheet_content[:2]) # this is here to avoid empty lines 

    sys_cols = sheet_content.columns

    generated_script = []
    for indices, row in sheet_content.iterrows():
        print(type(row))
        a = cu.concat_4(row['Source System ID'], '/', row['Source System Alias'], row['Source System Name'])
        generated_script.append(pref+ a + sufx )

    
    print(generated_script)
    return generated_script 


def process_stream_tab(sheet_content):
    print("============= process stream tab ==============")
    #print(type(sheet_content))
    #print(sheet_content)
    print(sheet_content.columns)
    '''
    ['System Id', 'System Name', 'Stream Key', 'Stream Name',
       'Loading Frequency']

    CALL GCFR_UT_Register_Stream(1,1,'CB_STG','2025-04-13');

       '''
    pref = "CALL GCFR_UT_Register_Stream( "
    sufx = ");"
    # next line will be removed when working with the actual sheet 
    new_sheet_content =  pd.DataFrame(sheet_content[:4])

    

    generated_script = []
    for indices, row in new_sheet_content.iterrows():
        print(type(row))
        today = datetime.today().strftime('%Y-%m-%d')
        print(str(row))
        a= str(int(row['System Id'])) + ',' + str(int(row['Stream Key'])) + ','
        print(a)
        a =  a + cu.concat_2(row['Stream Name'], today )
        generated_script.append(pref+ a + sufx )

    #print(new_sheet_content)
    print(generated_script)
    for s in generated_script:
        print(s)
    return generated_script 

'''
STG_tables functions takes a dataframe and returns the generates script
'''
def STG_tables_(sheet_content):
    st.write(sheet_content)
    #st.write(type(sheet_content))
    st.write(sheet_content.columns)


def STG_tables(sheet_content):
    print("============= process STG tables tab ==============")
    print(type(sheet_content))
    print(sheet_content.columns)
    # ['table name source', 'attr'],
    print(type(sheet_content['attr']))
    attr_df=sheet_content['attr'].to_frame()
    print(type(attr_df))
    print(attr_df)
    print(attr_df.columns)
    print(attr_df.shape)
    print(type(attr_df['attr']))
    attrs=sheet_content['attr'].to_dict()
    print(attrs)
    
    pref1 = "CREATE MULTISET TABLE GDEV1T_STG."
    #table_name='sheet_content['attr']'
    #table_name = sheet_content['table name stg']
    pref2=', '
    table_name=''
    pref_fall_back = 'NO FALLBACK'
    #if sheet_content['Fallback']=='Y':
    #    pref_fall_back ='FALLBACK'

    pref3 = "NO BEFORE JOURNAL, NO AFTER JOURNAL, CHECKSUM = DEFAULT,DEFAULT MERGEBLOCKRATIO, MAP= TD_MAP1 ( "
    pref=f'{pref1} {table_name} {pref2} {pref_fall_back} {pref3} '
    
    
    sufx = """ BATCH_ID VARCHAR(20), Start_Ts TIMESTAMP(6) WITH TIME ZONE,
    End_Ts TIMESTAMP(6) WITH TIME ZONE,     Start_Date DATE,     End_Date DATE,
    Record_Deleted_Flag BYTEINT,
    Ctl_Id SMALLINT COMPRESS 997,
    File_Id SMALLINT COMPRESS 997,
    Process_Name VARCHAR(128) CHARACTER SET LATIN NOT CASESPECIFIC,
    Process_Id INTEGER,
    Update_Process_Name VARCHAR(128) CHARACTER SET LATIN NOT CASESPECIFIC,
    Update_Process_Id INTEGER)
    UNIQUE PRIMARY INDEX """
    print(sufx)

    # next line will be removed when working with the actual sheet 
    #new_sheet_content =  pd.DataFrame(sheet_content[:4])

    
    

    generated_script = []
    '''
    for indices, row in sheet_content.iterrows():
        print(type(row))
        today = datetime.today().strftime('%Y-%m-%d')
        print(str(row))
        a= str(int(row['System Id'])) + ',' + str(int(row['Stream Key'])) + ','
        print(a)
        a =  a + cu.concat_2(row['Stream Name'], today )
        generated_script.append(pref+ a + sufx )
    '''
    s = f'{pref1} {table_name} {pref2} {pref_fall_back} {pref3} {sufx}'
    #print(new_sheet_content)
    generated_script.append(s)
    print(generated_script)
    for s in generated_script:
        print(s)
    return generated_script 


'''
FUNCTION CALLS starts here
'''
#xl = pd.ExcelFile(the_file_to_read)
#workbook_sheets_names = get_sheets(xl)
# the workbook sheets are returned in a dataframe with column index
#print(workbook_sheets_names)


#new_names_list = df_names(workbook_sheets_names)
#print(new_names_list)
#df= pd.DataFrame(list(zip(workbook_sheets_names, df_names(workbook_sheets_names))))

#df.columns= ['tab', 'df_name']
#print(df)
''' Now we get the content of the tabs. let's make it in a function'''
#df['content'] = read_tabs_contents(xl, df['tab'])

''' Now our dataframe has three columns: original tab names, modified tab names and the content'''
#print(df)
#print(df.shape)

#df['script'] = [list() for x in range(len(df.index))]
#print(df)
''' Now our dataframe has four columns: original tab names, modified tab names and the content
and the script column '''

#print("---- returned values to be assigned to the dataframe ------------")
#print(df['content'][1])
#gen_script = process_system_tab(df['content'][1])

#df['script'][1]=gen_script
#print(df)

''' STREAM processing '''
'''
print("======================== STREAM script generator ========== ")
print(df['content'][2])
gen_script = process_stream_tab(df['content'][2])
#df.loc[2, 'script'] = gen_script
df['script'][2].append(gen_script)
#df['script'][2]=gen_script
print(df)
'''

''' BKEY processing '''
'''
print("======================== STREAM script generator ========== ")
'''


'''Core tables processing'''
def core_tables_script(df):
    print(' In core Tables script generator')
    print(df)
    print(type(df))
    print(df.shape)
    print(df.columns)
    DB_name='ETLTEST'
    print(DB_name)
    script_list = []
   
    

    for index, row in df.iterrows():
        print('========================================== \n iterating the df')
        print(type(row))
        print(row['table name'])
        tbl_name=DB_name+'.'+row['table name']
        print('the table name is : ----- ',tbl_name)
        attr= row['attr']
        print('The attr col contains the following ', attr)
        print(type(attr))
        sql_string = 'CREATE MULTISET TABLE ' +  tbl_name+ ' (' 
        print('attr list length = ', len(attr))
        f_string = ''
        PARTY_ID=''
        for f in attr:
            print (f)
            mand=''
            if f['mandatory']=='Y' :
                mand = "NOT NULL"
            if f['column name'] == 'PARTY ID':
                PARTY_ID = f['column name']
            added_field = f['column name']+' '+f['data type']+' '+mand+','
            print(added_field)
            f_string=f_string +' '+added_field

        print(f_string)  
        print('============================================== PARTY _ID', PARTY_ID)
        #f_string=f_string[:-1]+ ' ) UNIQUE PRIMARY INDEX('+ PARTY_ID+')' 
        f_string=f_string[:-1]+ ' ) UNIQUE PRIMARY INDEX(PARTY_ID)' 

        print(f_string)
        sql_string = sql_string+f_string
        script_list.append(sql_string)
       
    """
    CREATE MULTISET TABLE GDEV1T_CORE.PRTY (
    PARTY_ID INTEGER NOT NULL, 
    PARTY_DESC VARCHAR(250),
    PARTY_NUM VARCHAR(100)
    ) UNIQUE PRIMARY INDEX(PARTY_ID)
    """
    

    return script_list