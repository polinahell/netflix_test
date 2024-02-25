import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\37259\Desktop\Programming\Inbank\Netflix_dataset.csv', delimiter=';')
print(f"Rows read from CSV: {len(df)}")

# Check for duplicate User IDs
if df['User ID'].duplicated().any():
    print("Duplicate User IDs found.")

# Validate Age range and print invalid User IDs
invalid_ages = df[~df['Age'].between(18, 120)]
if not invalid_ages.empty:
    print("Invalid Age values found for User IDs:", invalid_ages['User ID'].tolist())

# Convert Join Date and Last Payment Date to datetime and validate
# Date format in the CSV is 'dd.mm.yyyy'
df['Join Date'] = pd.to_datetime(df['Join Date'], format='%d.%m.%Y', errors='coerce')
df['Last Payment Date'] = pd.to_datetime(df['Last Payment Date'], format='%d.%m.%Y', errors='coerce')

# Check for any invalid values
if df['Join Date'].isnull().any():
    print("Invalid Join Dates found.")
if df['Last Payment Date'].isnull().any():
    print("Invalid Last Payment Dates found.")

# Check that Last Payment Date is not earlier than Join Date
invalid_payment_dates = df[df['Last Payment Date'] < df['Join Date']]
if not invalid_payment_dates.empty:
    print(f"Found {len(invalid_payment_dates)} instances where Last Payment Date is earlier than Join Date.")
    print("Related User IDs:", invalid_payment_dates['User ID'].tolist())
