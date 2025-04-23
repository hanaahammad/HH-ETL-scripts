

import teradatasql
import pandas as pd
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get environment variables




def establish_TD_connection():
    user_name = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    with teradatasql.connect(host=host, user=user_name, password=password) as connect:
        data = pd.read_sql('select top 5 * from jaffle_shop.raw_customers;', connect)

    print(data)

establish_TD_connection()

