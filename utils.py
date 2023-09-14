import pandas as pd;
import os

# Read csv file to get data frame
def get_dataframe(file_path):
    return pd.read_csv(file_path)

# Get current directory path 
def current_directory_path():
    return os.getcwd()
