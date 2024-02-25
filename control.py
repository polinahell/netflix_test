import pandas as pd

# Load the dataset
df = pd.read_csv('Netflix_dataset.csv', delimiter=';')

# Check for duplicate User IDs
if df['User ID'].duplicated().any():
    print("Duplicate User IDs found.")

# Validate Age range
if not df['Age'].between(0, 120).all():
    print("Invalid Age values found.")

# Example: Convert Join Date and Last Payment Date to datetime and validate
df['Join Date'] = pd.to_datetime(df['Join Date'], errors='coerce')
df['Last Payment Date'] = pd.to_datetime(df['Last Payment Date'], errors='coerce')
if df['Join Date'].isnull().any() or df['Last Payment Date'].isnull().any():
    print("Invalid dates found.")

# After validation, you can proceed with data transformation and loading
