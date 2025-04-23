

import teradatasql
import pandas as pd

def establish_TD_connection():
    host = '35.246.175.163'
    user_name = 'demo_user'
    password = 'lala@10@habibti'

    with teradatasql.connect(host=host, user=user_name, password=password) as connect:
        data = pd.read_sql('select top 5 * from jaffle_shop.raw_customers;', connect)

    print(data)

establish_TD_connection()

