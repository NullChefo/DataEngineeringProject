import kaggle

# Set your Kaggle API credentials (replace 'path/to/kaggle.json' with the path to your kaggle.json file)
kaggle.api.authenticate(api_key='/Users/angel.georgiev/Downloads/PythonExamples/KaggleDataLoad/kaggle.json')

# Replace 'dataset-owner/dataset-name' with the actual owner and dataset name from the Kaggle URL
dataset_owner = 'programmerrdai'
dataset_name = 'financing-healthcare'

# Specify the directory where you want to download the dataset
download_dir = '/Users/angel.georgiev/Downloads/PythonExamples/KaggleDataLoad'

# Use the Kaggle API to download the dataset
kaggle.api.dataset_download_files(f'{dataset_owner}/{dataset_name}', path=download_dir, unzip=True)