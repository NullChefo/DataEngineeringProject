import extract
import transform
import load

# Extract data from the API endpoints
users_data = extract.extract_users_data()
products_data = extract.extract_products_data()

# Transform the extracted data
transformed_users_data = transform.transform_users_data(users_data)
transformed_products_data = transform.transform_products_data(products_data)

# Load the transformed data into Oracle
load.load_data_to_oracle(transformed_users_data, "users_table")
load.load_data_to_oracle(transformed_products_data, "products_table")
