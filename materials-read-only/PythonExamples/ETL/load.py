import cx_Oracle
from sqlalchemy import create_engine, FLOAT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text


cx_Oracle.init_oracle_client(lib_dir="/Users/angelgeorgiev/Downloads/instantclient_19_8")

def load_data_to_oracle(df, target_table):
    # Replace the placeholder with your actual Oracle connection details
    engine = create_engine('oracle+cx_oracle://db_user:db_pass@localhost:1521?service_name=XEPDB1')
    
    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute(text(f'''DROP TABLE {target_table}'''))
    session.commit()
    session.close()

    # Load the transformed data into the target Oracle database
    # print(df)
    df.to_sql(target_table, engine, if_exists='append', index=False, dtype={"discountPercentage": FLOAT(), "rating": FLOAT()})

    # Close the connection
    engine.dispose()