import pandas as pd
# Load the dataset
df = pd.read_csv("D:\Elevate Labs Intern\KaggleV2-May-2016.csv")
# Check missing values
print(df.isnull().sum())

# Handle missing values
df.fillna(method='ffill', inplace=True)  # Example: forward fill

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize text


# Convert dates
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')

# Rename columns
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Check data types
print(df.dtypes)
