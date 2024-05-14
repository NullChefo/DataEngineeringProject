from ETLProcess.db_connector import get_data_from_table, load_to_table
import pandas as pd

def execute_load():
    users_df = get_data_from_table("USERS", "mysql")

    modified_users_df = users_df.rename(columns = {'id': 'user_gk', 'name': 'full_name', 'phone': 'user_phone'})
    modified_users_df = modified_users_df.fillna(999)

    load_to_table("DIM_USER", "oracle", modified_users_df)