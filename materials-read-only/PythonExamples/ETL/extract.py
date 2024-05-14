import requests

def extract_users_data():
    response = requests.get("https://dummyjson.com/users")
    return response.json()

def extract_products_data():
    response = requests.get("https://dummyjson.com/products")
    return response.json()
