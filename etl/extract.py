import pandas as pd
from pathlib import Path

def extract_data(filepath='data/processed/cleaned_retail_data.csv'): 
    try : 
        df = pd.read_csv(filepath)
        print("Data Extracted Sucessfully")
        return df
    except FileNotFoundError:
        print(f"File not found at {filepath}")
        return None
        