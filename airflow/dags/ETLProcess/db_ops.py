import os

import pandas as pd
import mysql.connector
import psycopg2
import cx_Oracle
# import re
import pandas as pd
# from sqlalchemy import create_engine


# # Tried to use sqlalchemy but with no great success
# def load_data_to_db(table_name: str, connection_type: str, csv_path_directory: str):
#     csv_files = [file_name for file_name in os.listdir(csv_path_directory) if file_name.endswith(".csv")]
#
#     for file_name in csv_files:
#         csv_path = os.path.join(csv_path_directory, file_name)
#         # Read the CSV file into a pandas DataFrame
#         csv_file = csv_path # Replace with the path to your CSV file
#         df = pd.read_csv(csv_file)
#
#         # Define your MySQL connection string
#         # Replace 'username', 'password', 'database', and 'host' with your MySQL credentials
#         # Example: 'mysql+mysqlconnector://username:password@localhost:3306/database'
#         mysql_connection_string = 'mysql+mysqlconnector://your_mysql_user:your_mysql_password@127.0.0.1:3306/data_engineering_project'
#
#         # Create a SQLAlchemy engine and connect to MySQL
#         engine = create_engine(mysql_connection_string)
#
#         # Define the table schema
#         df.to_sql(table_name, engine, index=False, if_exists='replace')
#
#         # Commit the changes
#         engine.dispose()
#
#         print(f'Table "{table_name}" created and data saved successfully.')


def load_imdb_top_1000_database(table_name: str, connection_type: str, csv_path_directory: str):
    csv_files = [file_name for file_name in os.listdir(csv_path_directory) if file_name.endswith(".csv")]

    for file_name in csv_files:
        csv_path = os.path.join(csv_path_directory, file_name)
        print(str(csv_path))
        data = pd.read_csv(csv_path)
        df = pd.DataFrame(data)

        conn = None
        if connection_type == "postgresql":
            conn = con_to_postgresql()

        if connection_type == "mysql":
            conn = conn_to_mysql()

        if connection_type == "oracle":
            conn = conn_to_oracle()

        cursor = conn.cursor()

        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            Poster_Link TEXT,
            Series_Title VARCHAR(255),
            Released_Year VARCHAR(255),
            Certificate VARCHAR(10),
            Runtime VARCHAR(20),
            Genre VARCHAR(255),
            IMDB_Rating VARCHAR(255),
            Overview TEXT,
            Meta_score VARCHAR(255),
            Director VARCHAR(255),
            Star1 VARCHAR(255),
            Star2 VARCHAR(255),
            Star3 VARCHAR(255),
            Star4 VARCHAR(255),
            No_of_Votes VARCHAR(255),
            Gross VARCHAR(255)
        );
        '''
        cursor.execute(create_table_query)

        # Iterate over the first DataFrame and insert rows into the table
        for index, row in df.iterrows():
            # Check each value for validity and set to None if not valid
            data_tuple = (
                row['Poster_Link'] if pd.notna(row['Poster_Link']) else None,
                row['Series_Title'] if pd.notna(row['Series_Title']) else None,
                row['Released_Year'] if pd.notna(row['Released_Year']) else None,
                row['Certificate'] if pd.notna(row['Certificate']) else None,
                row['Runtime'] if pd.notna(row['Runtime']) else None,
                row['Genre'] if pd.notna(row['Genre']) else None,
                row['IMDB_Rating'] if pd.notna(row['IMDB_Rating']) else None,
                row['Overview'] if pd.notna(row['Overview']) else None,
                row['Meta_score'] if pd.notna(row['Meta_score']) else None,
                row['Director'] if pd.notna(row['Director']) else None,
                row['Star1'] if pd.notna(row['Star1']) else None,
                row['Star2'] if pd.notna(row['Star2']) else None,
                row['Star3'] if pd.notna(row['Star3']) else None,
                row['Star4'] if pd.notna(row['Star4']) else None,
                row['No_of_Votes'] if pd.notna(row['No_of_Votes']) else None,
                row['Gross'] if pd.notna(row['Gross']) else None
            )

            insert_query = f'''
            INSERT INTO {table_name} (
                Poster_Link,Series_Title, Released_Year, Certificate, Runtime, Genre, IMDB_Rating, 
                Overview, Meta_score, Director, Star1, Star2, Star3, Star4, No_of_Votes, Gross
            ) VALUES (
                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
            '''

            cursor.execute(insert_query, data_tuple)

        # Commit changes and close connections
        conn.commit()
        close_all(cursor, conn)

        print(f'Table "{table_name}" created and data saved successfully.')


def load_netflix_imdb_database(table_name: str, connection_type: str, csv_path_directory: str):
    csv_files = [file_name for file_name in os.listdir(csv_path_directory) if file_name.endswith(".csv")]

    for file_name in csv_files:
        csv_path = os.path.join(csv_path_directory, file_name)
        print(str(csv_path))
        data = pd.read_csv(csv_path)
        df = pd.DataFrame(data)

        conn = None
        if connection_type == "postgresql":
            conn = con_to_postgresql()

        if connection_type == "mysql":
            conn = conn_to_mysql()

        if connection_type == "oracle":
            conn = conn_to_oracle()

        # Create a cursor
        cursor = conn.cursor()

        # Define the table schema based on the CSV columns
        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            `index` VARCHAR(255),
            `id` VARCHAR(255),
            `title` VARCHAR(255),
            `type` VARCHAR(255),
            `description` TEXT,
            `release_year` VARCHAR(255),
            `age_certification` VARCHAR(255),
            `runtime` VARCHAR(255),
            `imdb_id` VARCHAR(255),
            `imdb_score` VARCHAR(255),
            `imdb_votes` VARCHAR(255)
        );
        '''
        cursor.execute(create_table_query)

        # Iterate over the DataFrame and insert rows into the table
        for index, row in df.iterrows():
            # Check each value for validity and set to None if not valid
            data_tuple = (
                row['index'],
                row['id'] if pd.notna(row['id']) else None,
                row['title'] if pd.notna(row['title']) else None,
                row['type'] if pd.notna(row['type']) else None,
                row['description'] if pd.notna(row['description']) else None,
                row['release_year'] if pd.notna(row['release_year']) else None,
                row['age_certification'] if pd.notna(row['age_certification']) else None,
                row['runtime'] if pd.notna(row['runtime']) else None,
                row['imdb_id'] if pd.notna(row['imdb_id']) else None,
                row['imdb_score'] if pd.notna(row['imdb_score']) else None,
                row['imdb_votes'] if pd.notna(row['imdb_votes']) else None
            )

            insert_query = f'''
            INSERT INTO {table_name} (
                `index`, `id`, `title`, `type`, `description`, `release_year`, 
                `age_certification`, `runtime`, `imdb_id`, `imdb_score`, `imdb_votes`
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            '''

            cursor.execute(insert_query, data_tuple)

        # Commit changes and close connections
        conn.commit()
        close_all(cursor, conn)


def load_imdb_movies_dataset_database(table_name: str, connection_type: str, csv_path_directory):
    csv_files = [file_name for file_name in os.listdir(csv_path_directory) if file_name.endswith(".csv")]

    for file_name in csv_files:
        csv_path = os.path.join(csv_path_directory, file_name)
        print(str(csv_path))
        data = pd.read_csv(csv_path)
        df = pd.DataFrame(data)

        conn = None
        if connection_type == "postgresql":
            conn = con_to_postgresql()

        if connection_type == "mysql":
            conn = conn_to_mysql()

        if connection_type == "oracle":
            conn = conn_to_oracle()

        cursor = conn.cursor()

        # Define the table schema for the third CSV

        create_table_query_3 = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            names VARCHAR(255),
            date_x VARCHAR(255),
            score VARCHAR(255),
            genre VARCHAR(255),
            overview TEXT,
            crew TEXT,
            orig_title VARCHAR(255),
            status VARCHAR(255),
            orig_lang VARCHAR(255),
            budget_x VARCHAR(255),
            revenue VARCHAR(255),
            country VARCHAR(255)
        );
        '''
        cursor.execute(create_table_query_3)

        # Iterate over the third DataFrame and insert rows into the table
        for index, row in df.iterrows():
            # Check each value for validity and set to None if not valid
            data_tuple = (
                row['names'] if pd.notna(row['names']) else None,
                row['date_x'] if pd.notna(row['date_x']) else None,
                row['score'] if pd.notna(row['score']) else None,
                row['genre'] if pd.notna(row['genre']) else None,
                row['overview'] if pd.notna(row['overview']) else None,
                row['crew'] if pd.notna(row['crew']) else None,
                row['orig_title'] if pd.notna(row['orig_title']) else None,
                row['status'] if pd.notna(row['status']) else None,
                row['orig_lang'] if pd.notna(row['orig_lang']) else None,
                row['budget_x'] if pd.notna(row['budget_x']) else None,
                row['revenue'] if pd.notna(row['revenue']) else None,
                row['country'] if pd.notna(row['country']) else None
            )

            insert_query_3 = f'''
            INSERT INTO {table_name} (
                names, date_x, score, genre, overview, crew, orig_title, 
                status, orig_lang, budget_x, revenue, country
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
            '''

            cursor.execute(insert_query_3, data_tuple)

        # Commit changes and close connections
        conn.commit()
        close_all(cursor, conn)

        print(f'Table "{table_name}" created and data saved successfully.')


def close_all(cursor, connection):
    cursor.close()
    connection.close()


def get_data_from_table(table_name: str, connection_type: str):
    conn = None
    if connection_type == "postgresql":
        conn = con_to_postgresql()

    if connection_type == "mysql":
        conn = conn_to_mysql()

    if connection_type == "oracle":
        conn = conn_to_oracle()

    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"

    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Get column names from the cursor description
    columns = [col[0] for col in cursor.description]

    # Create a Pandas DataFrame
    df = pd.DataFrame(rows, columns=columns)

    close_all(cursor, conn)

    return df


def load_to_table(table_name, conn_type, df):
    if conn_type == "mysql":
        connection = conn_to_mysql()
    elif conn_type == "postgresql":
        connection = con_to_postgresql()
    else:
        connection = conn_to_oracle()

    cursor = connection.cursor()
    for index, row in df.iterrows():
        values = tuple(row)
        query = f'INSERT INTO {table_name} VALUES {values}'
        print(query)
        cursor.execute(query)
    connection.commit()
    close_all(cursor, connection)


# Not in use
def conn_to_oracle():
    oracle_instant_client_dir = '/Users/<your_user_name>/OracleClient'

    cx_Oracle.init_oracle_client(oracle_instant_client_dir)

    dsn_tns = cx_Oracle.makedsn('server', '1521', service_name='DATABASE')
    connection = cx_Oracle.connect(user='admin', password='password', dsn=dsn_tns)

    return connection


def con_to_postgresql():
    connection_string_params = {
        "host": "127.0.0.1",
        "user": "postgres",
        "password": "example_password",
        "database": "data_engineering_project",
        "port": "5432"
    }
    conn = psycopg2.connect(**connection_string_params)

    return conn


def conn_to_mysql():
    connection_string_params = {
        "host": "127.0.0.1",
        "user": "your_mysql_user",
        "password": "your_mysql_password",
        "db": "data_engineering_project",
        "port": "3306"
    }
    conn = mysql.connector.connect(**connection_string_params)

    return conn


def load_the_transformed_data_to_database(table_name: str, connection_type: str, data_frame):
    conn = None
    if connection_type == "postgresql":
        conn = con_to_postgresql()

    if connection_type == "mysql":
        conn = conn_to_mysql()

    if connection_type == "oracle":
        conn = conn_to_oracle()

    cursor = conn.cursor()

    # Define the table schema for the unified DataFrame
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        Title VARCHAR(255),
        Release_Year VARCHAR(255),
        IMDB_Score VARCHAR(255),
        Votes VARCHAR(255),
        Meta_Score VARCHAR(255),
        Budget VARCHAR(255),
        Original_Language VARCHAR(255)
    );
    '''
    cursor.execute(create_table_query)

    # Iterate over the DataFrame and insert rows into the table
    for index, row in data_frame.iterrows():
        # Check each value for validity and set to None if not valid
        data_tuple = (
            row['Title'] if pd.notna(row['Title']) else None,
            row['Release_Year'] if pd.notna(row['Release_Year']) else None,
            row['IMDB_Score'] if pd.notna(row['IMDB_Score']) else None,
            row['Votes'] if pd.notna(row['Votes']) else None,
            row['Meta_Score'] if pd.notna(row['Meta_Score']) else None,
            row['Budget'] if pd.notna(row['Budget']) else None,
            row['Original_Language'] if pd.notna(row['Original_Language']) else None
        )

        insert_query = f'''
        INSERT INTO {table_name} (
            Title, Release_Year, IMDB_Score, Votes, Meta_Score, 
            Budget, Original_Language
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s
        );
        '''

        cursor.execute(insert_query, data_tuple)
    # Commit changes and close connections
    conn.commit()
    close_all(cursor, conn)

    print(f'Table "{table_name}" created and data saved successfully.')
