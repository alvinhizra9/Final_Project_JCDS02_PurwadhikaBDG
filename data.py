import pandas as pd
from sqlalchemy import create_engine

def data_clean():
    engine = create_engine("mysql+mysqlconnector://root:alvinista9@localhost/clean?host=localhost?port=3306")
    conn = engine.connect()
    result = conn.execute('SELECT * from clean.clean').fetchall()
    df = pd.DataFrame(result, columns = result[0].keys())
    return df

contract_type = ['A', 'B', 'C', 'D', 'E']

is_male = ['female', 'male']

province = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 
              'S', 'T', 'U']

group = ['A', 'B', 'C', 'D']

history_type = ['A', 'B', 'C', 'D']