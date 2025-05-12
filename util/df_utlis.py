
import pandas as pd 

def initalize_test_df():
    cols = ['Subject Area','Table Name','Column Name','Data Type','Mandatory',	'PK','Historization Key','Version']

    df = pd.DataFrame(columns=cols)
    print(df.columns)

    df[df.columns[0]] = ['PARTY', 'PARTY', 'PARTY']
    df[df.columns[1]] = ['PARTY', 'PARTY', 'PARTY']
    df[df.columns[2]] = ['PARTY_ID', 'PARTY_DESC', 'PARTY_NUM'] 
    df[df.columns[3]] = ['INTEGER', 'VARCHAR(250)', 'VARCHAR(100)']

    df[df.columns[4]] = ['Y', '', '']
    df[df.columns[5]] = ['Y', '', '']
    df[df.columns[6]] = ['', '', '']
    df[df.columns[7]] = ['0.1', '0.1', '0.1']

    print(df)
    return df




def df_groupBy(df, col) :
    print('------------------------ GROUP BY')
    print('BUT first lets check the passed Dataframe ')
    print(df)
    print(f' group by the df {df.columns}')
    print(f' by the column {col}')
    #d = (df.groupby(['Table Name'])[['a','d']]
    '''
    d = (df.groupby([col])[df.columns]
       .apply(lambda x: x.to_dict('records'))
       .reset_index(name='attr')
       .to_dict('records'))
    '''
    d = (df.groupby([col])[df.columns]
       .apply(lambda x: x.to_dict('records'))
       .reset_index(name='attr'))
    print (d)
    df_returned  =pd.DataFrame(d)
    #df_returned['attr'] = df_returned['attr'].apply(lambda x: str(x))
    print(df_returned.columns)
    print(df_returned)
    return df_returned
    

df=initalize_test_df()
col = 'Table Name'
d=df_groupBy(df, col)
print('=========================')
print(type(d))
print(d)
print(d.shape)
print(d.columns)
#d['attr']=d['attr'].to_string()
print(d.columns)
