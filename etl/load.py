import sqlalchemy
from pathlib import Path

def load_to_sqlite(df , db_path ='database/retail_data.db', table_name ='retail_cleaned' ) :
    Path('database').mkdir(exist_ok= True)
    engine = sqlalchemy.create_engine(f'sqlite:///{db_path}')
    df.to_sql(table_name , con= engine , if_exists= 'replace' , index=False)
    print(f"Data loaded Sucessfully into SQLite DB at {db_path} in table '{table_name}'")