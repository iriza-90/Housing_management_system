from sqlalchemy import create_engine
import pandas as pd

db_user: str = 'postgres'
db_port: int = 4221
db_host: str = 'localhost'
db_password: str = ''

db1_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/eb_ml"

# Create database engines
engine_db1 = create_engine(db1_url) # create_engine() func to connect to a PostgreSQL database by passing a connection string that includes the database name, username, password, host, and port.

# Example: Fetch data into DataFrames
query_db1 = "SELECT * FROM library_books;"
query_db2 = "SELECT * FROM authors;"

df_books = pd.read_sql(query_db1, engine_db1)
df_authors = pd.read_sql(query_db1, engine_db1)

# df_books.to_csv('books_data.csv', index=False)
# df_authors.to_csv('authors_data.csv', index=False)

# Load the CSVs
books_data = pd.read_csv('books_data.csv')
authors_data = pd.read_csv('authors_data.csv')

# print(books_data.head())
# print(authors_data.head())

# print(books_data.isnull().sum())
# print(authors_data.isnull().sum())

authors_data.dropna(axis=1, how='all', inplace=True) # axis=1: Operates on columns (rows is 0), inplace=True: Modifies the original DataFrame

df_merged = pd.merge(books_data, authors_data, on='author_id', how='inner')
df_merged.to_csv('merged_lib.csv', index=False)
merged_lib = pd.read_csv('merged_lib.csv')