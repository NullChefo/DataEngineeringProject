import pandas as pd
from sqlalchemy import create_engine

# Replace 'your_database_url' with the actual connection string for your database
connection_string = "mysql://your_mysql_user:your_mysql_password@localhost:3306/data_engineering_project"

engine = create_engine(connection_string)

# Replace 'your_table_name' with the desired table name
table_name = 'test'

# Replace 'your_csv_file.csv' with the path to your CSV file
csv_file_path = '../airflow/dags/ETLProcess/kaggle/resource/imdb-top-1000/imdb_top_1000.csv'

# Read CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Write the DataFrame to a SQL table
df.to_sql(table_name, engine, index=False, if_exists='replace')

print(f'Table {table_name} created successfully from CSV.')