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

# print("Missing values in each column:\n", raw.isnull().sum())

raw['First Name'].fillna('Unknown', inplace=True)
raw['Last Name'].fillna('Unknown', inplace=True)
raw['State'].fillna('Unknown', inplace=True)
raw['City'].fillna('Unknown', inplace=True)
raw['ZIP'].fillna(00000, inplace=True)  # For numeric columns
raw['Date Created'].fillna(pd.Timestamp('2023-01-01'), inplace=True)
raw['Worked'].fillna(False, inplace=True)

raw_cleaned = raw

print("Missing values after cleaning:\n", raw_cleaned.isnull().sum())

print(raw_cleaned[raw_cleaned.isnull().any(axis=1)])

raw_cleaned.to_csv('cleaned_leads.csv', index=False)

# Suppress specific FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)
