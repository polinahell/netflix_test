import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Load the dataset
df = pd.read_csv('/path/to/Netflix_dataset.csv', delimiter=';')

# Create a SQLite database and engine
engine = create_engine('sqlite:///netflix_data.db')

# Transform data to fit the normalized model
# This would involve creating separate DataFrames for each table in our model
# Example for the Users table
users_df = df[['User ID', 'Country', 'Age', 'Gender']].drop_duplicates()

# Load data into the database
# Each DataFrame can be written to a separate table in the SQLite database
users_df.to_sql('users', engine, index=False, if_exists='replace')

# Repeat the above steps for Subscriptions, Usage, and Payments tables

# To make this loading process repeatable, you could encapsulate the script into a function 
# or a standalone Python script and schedule it to run at regular intervals using a scheduler 
# like cron (for Linux/macOS) or Task Scheduler (for Windows). 
# This way, if the dataset is updated or needs to be reloaded periodically, the process can be automate