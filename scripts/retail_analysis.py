import pandas as pd
import numpy as np
from pathlib import Path
import sys


# ETL Pipeline 
data_path = Path('../data/raw/data.csv')

# Step 1: Extract - Loading Superstore dataset with proper encoding
try :
    df = pd.read_csv(data_path, encoding='ISO-8859-1')
except UnicodeDecodeError:
    print("Error : Failed to read CSV with ISO-8859-1. Now Trying Latin-1")
    df = pd.read_csv(data_path, encoding='latin-1')
except FileNotFoundError:
    print(f"Error File {data_path} not found. Please ensure data.csv is in data/raw/")
    sys.exit(1)
    
# Step 2: Transform - Clean data
# Handle Missing Data

