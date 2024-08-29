import numpy as np
import pandas as pd
import warnings

pd.__version__

url = 'leads_data.csv'
raw = pd.read_csv(url, parse_dates=['Date Created'], engine='python')

# Convert 'Date Created' column to pandas datetime format if not already
raw['Date Created'] = pd.to_datetime(raw['Date Created'], errors='coerce')

# print(raw.shape)
#
# print(raw.head())
# print(" ")
# print(raw.describe())
# print(raw.dtypes)

print("Missing values in each column:\n", raw.isnull().sum())

raw_cleaned = raw.fillna({
    'First Name': 'Unknown',
    'Last Name': 'Unknown',
    'State': 'Unknown',
    'City': 'Unknown',
    'ZIP': 00000,  # or use median
    'Date Created': pd.Timestamp('2023-01-01'),  # Default date
    'Worked': False
})

print("Missing values after cleaning:\n", raw_cleaned.isnull().sum())

raw_cleaned.to_csv('cleaned_leads.csv', index=False)

# Suppress specific FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)
