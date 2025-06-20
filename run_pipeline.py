from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_sqlite

def main():
    df = extract_data()
    if df is not None:
        df = transform_data(df)
        load_to_sqlite(df)
        
if __name__ == '__main__' :
    main()