import pandas as pd
from sqlalchemy import create_engine

# Load the dataset
df = pd.read_csv(r'C:\Users\37259\Desktop\Programming\Inbank\Netflix_dataset.csv', delimiter=';')
print(f"Rows read from CSV: {len(df)}")

# Rename the columns to match the database schema. For example, 'User ID' becomes 'User_ID'
df.columns = df.columns.str.strip() 
df.columns = df.columns.str.replace(' ', '_')  

# Create a SQLite database and engine
engine = create_engine('sqlite:///C:/Users/37259/Desktop/Programming/Inbank/netflix.db')

# Transform data to fit the model
# Users table
users_df = df[['User_ID', 'Country', 'Age', 'Gender']].drop_duplicates()
print(f"Rows to insert into Users table: {len(users_df)}")
users_df.to_sql('users', engine, index=False, if_exists='append')


# Subscriptions table
df['Subscription_ID'] = range(1, len(df) + 1)  # Creates a unique ID for each row
print(f"Rows to insert into Subscriptions table: {len(users_df)}")
subscriptions_df = df[['Subscription_ID', 'User_ID', 'Subscription_Type', 'Monthly_Revenue', 'Plan_Duration']].drop_duplicates()
subscriptions_df.to_sql('subscriptions', engine, index=False, if_exists='append')


# Usage table
df['Usage_ID'] = range(1, len(df) + 1)  # Creates a unique ID for each row
print(f"Rows to insert into Usage table: {len(users_df)}")
usage_df = df[['Usage_ID', 'User_ID', 'Device', 'Movies_Watched', 'Series_Watched']].drop_duplicates()
usage_df.to_sql('usage', engine, index=False, if_exists='append')


# Payments table
df['Payment_ID'] = range(1, len(df) + 1)  # Creates a unique ID for each row
print(f"Rows to insert into Payments table: {len(users_df)}")
payments_df = df[['Payment_ID', 'User_ID', 'Join_Date', 'Last_Payment_Date', 'Active_Profiles', 'Household_Profile_Ind']].drop_duplicates()
payments_df.to_sql('payments', engine, index=False, if_exists='append')


#How would you make loading repeatable on a regular basis?

#1.Task scheduler:
#For Windows: Task Scheduler can be used to run the load.py script.
#For Linux/Mac: cron jobs can be used to schedule script. 
#OR
#2.CI/CD Pipelines:
#For more complex systems good to use CI/CD tools like Jenkins, GitLab CI, or GitHub Actions. 
#These tools can provide more control over the execution and better integration with infrastructure.