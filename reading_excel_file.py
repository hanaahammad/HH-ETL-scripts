import pandas as pd
import util.concat_util as cu
from datetime import datetime



#the_file_to_read = "file_example_XLSX_5000.xlsx"
the_file_to_read = "WAVEZ_SMX_Version_0.1.xlsx"

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
    #print(type(sheet_content))
    #print(sheet_content)
    print(sheet_content.columns)
    '''
    (['Source System ID', 'Source System Name', 'Source System Alias',
       'Schema', 'Loading Type', 'Source Type']


       EXEC GCFR_Register_System('1','/','CB','Core Banking');

       '''
    pref = "EXEC GCFR_Register_System( "
    sufx = ");"
    new_sheet_content =  pd.DataFrame(sheet_content[:2])

    sys_cols = new_sheet_content.columns

    generated_script = []
    for indices, row in new_sheet_content.iterrows():
        print(type(row))
        a = cu.concat_4(row['Source System ID'], '/', row['Source System Alias'], row['Source System Name'])
        generated_script.append(pref+ a + sufx )

    #print(new_sheet_content)
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
FUNCTION CALLS starts here
'''
xl = pd.ExcelFile(the_file_to_read)
workbook_sheets_names = get_sheets(xl)
# the workbook sheets are returned in a dataframe with column index
print(workbook_sheets_names)


new_names_list = df_names(workbook_sheets_names)
print(new_names_list)
df= pd.DataFrame(list(zip(workbook_sheets_names, df_names(workbook_sheets_names))))

df.columns= ['tab', 'df_name']
#print(df)
''' Now we get the content of the tabs. let's make it in a function'''
df['content'] = read_tabs_contents(xl, df['tab'])

''' Now our dataframe has three columns: original tab names, modified tab names and the content'''
#print(df)
print(df.shape)

df['script'] = [list() for x in range(len(df.index))]
print(df)
''' Now our dataframe has four columns: original tab names, modified tab names and the content
and the script column '''

print("---- returned values to be assigned to the dataframe ------------")
print(df['content'][1])
gen_script = process_system_tab(df['content'][1])

df['script'][1]=gen_script
print(df)

''' STREAM processing '''
print("======================== STREAM script generator ========== ")
print(df['content'][2])
gen_script = process_stream_tab(df['content'][2])
#df.loc[2, 'script'] = gen_script
df['script'][2].append(gen_script)
#df['script'][2]=gen_script
print(df)


''' BKEY processing '''
print("======================== STREAM script generator ========== ")

