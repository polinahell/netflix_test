# Netflix Test Project

This project is designed to load and analyze Netflix usage data. 
## Project Structure

- `control.py`: Script for data validation and pre-processing.
- `load.py`: Script to load the data from CSV files into the SQLite database.
- `construct.txt`: Contains SQL statements for constructing the database schema.
- `queries.txt`: Contains SQL queries used for data analysis.
- `README.md`: This file, describing the project and its components.
- `netflix.db`: SQLite database that stores the user data and activities.

## How to Use

1. Run the SQL statements in `construct.txt` to set up your database schema.
2. Execute `load.py` to load data from `Netflix_dataset.csv` into the `netflix.db` database.
3. Run `control.py` to validate the data for any inconsistencies or issues.
4. Use the queries within `queries.txt` to analyze the data.

## Requirements

- Python 3
- Pandas Library
- SQLAlchemy Library

Make sure to install the necessary Python libraries using the following command:

pip install pandas sqlalchemy
