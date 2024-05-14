import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the Google Sheets credentials and scope
SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Define your credentials JSON file path
CREDENTIALS_FILE = 'credentials.json'

class GoogleSheetDataManipulator:
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE, SCOPE
        )
        self.client = gspread.authorize(self.credentials)

    def fetch_data(self, sheet_name):
        # Open the specified sheet
        sheet = self.client.open_by_key(self.spreadsheet_id).worksheet(sheet_name)
        
        # Get all values from the sheet
        data = sheet.get_all_values()

        # Convert the data to a Pandas DataFrame
        df = pd.DataFrame(data[1:], columns=data[0])

        return df

    def manipulate_data(self, df):
        # Perform data manipulation using Pandas
        # Replace this with your desired data manipulation logic
        # For example, let's capitalize the 'Name' column
        df['Name'] = df['Name'].str.upper()

        return df

    def split_data(self, df, condition_column, condition_value):
        # Split the data into multiple files based on a condition
        # For example, let's split the data where the 'Category' column equals 'A'
        filtered_data = df[df[condition_column] == condition_value]

        # Save the filtered data to separate files
        # You can modify the file names and formats as per your needs
        filtered_data.to_csv('filtered_data.csv', index=False)
        filtered_data.to_excel('filtered_data.xlsx', index=False)

# Usage example
spreadsheet_id = '1vfEG6xrJE0YRWxxGq69vXbz4j0Iinbt9e6q3ft46jg0'  # Replace with your actual Google Sheet ID

data_manipulator = GoogleSheetDataManipulator(spreadsheet_id)

# Fetch data from a sheet named 'Data'
data = data_manipulator.fetch_data('Data')

# Manipulate the data
manipulated_data = data_manipulator.manipulate_data(data)

print(manipulated_data)

# Split the data where the 'Category' column equals 'A'
# data_manipulator.split_data(manipulated_data, 'Category', 'A')