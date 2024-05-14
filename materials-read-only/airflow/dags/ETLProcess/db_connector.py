import pyodbc
import cx_Oracle
import mysql.connector
import pandas as pd


def conn_to_mssql():
    server = ''
    database = ''
    username = ''
    password = ''
    connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=YES'

    conn = pyodbc.connect(connection_string)
    return conn

def conn_to_oracle():
    oracle_instant_client_dir = '/Users/<your_user_name>/VsCodeProjects/PythonExamples/ETLProcess/OracleClient'

    cx_Oracle.init_oracle_client(oracle_instant_client_dir)

    dsn_tns = cx_Oracle.makedsn('server', '1521', service_name='DATABASE')
    connection = cx_Oracle.connect(user='admin', password='password', dsn=dsn_tns)

    return connection

def conn_to_mysql():
    db_config = {
        "user": "",
        "password": "",
        "host": "",
        "port": "",
        "database": ""
    }

    # Connect to MySQL
    connection = mysql.connector.connect(**db_config)

    return connection

def close_all(cursor, connection):
    cursor.close()
    connection.close()

def get_data_from_table(table_name, conn_type):
    if conn_type == "mysql":
        connection =  conn_to_mysql()
    elif conn_type == "oracle":
        connection =  conn_to_oracle()
    else: 
        connection =  conn_to_mssql()
    
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name}"

    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Get column names from the cursor description
    columns = [col[0] for col in cursor.description]

    # Create a Pandas DataFrame
    df = pd.DataFrame(rows, columns=columns)
    
    close_all(cursor, connection)
    return df;

def load_to_table(table_name, conn_type, df):
    if conn_type == "mysql":
        connection =  conn_to_mysql()
    elif conn_type == "oracle":
        connection =  conn_to_oracle()
    else: 
        connection =  conn_to_mssql()
    
    cursor = connection.cursor()
    for index, row in df.iterrows():
        values = tuple(row)
        query = f'INSERT INTO {table_name} VALUES {values}'
        print(query)
        cursor.execute(query)
    connection.commit()
    close_all(cursor, connection)