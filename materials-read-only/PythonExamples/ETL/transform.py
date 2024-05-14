import pandas as pd

def transform_users_data(users_data):
    df = pd.DataFrame(users_data)
    new_df = pd.json_normalize(df['users'])[['id', 'firstName', 'lastName', 'age']]
    # Perform transformations specific to users data
    return new_df

def transform_products_data(products_data):
    df = pd.DataFrame(products_data) 
    new_df = pd.json_normalize(df.drop(['total', 'skip', 'limit'], axis=1)['products']).drop(['thumbnail', 'images'], axis=1)
    
    # Perform transformations specific to products data
    return new_df
