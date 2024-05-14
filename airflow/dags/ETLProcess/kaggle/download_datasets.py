import os
import kaggle

# # Set your Kaggle API credentials with json file
# kaggle.api.config_file = r'C:\Users\stefa\.kaggle\kaggle.json'
# kaggle.api.authenticate()

kaggle_username = os.environ.get("KAGGLE_USERNAME")
kaggle_key = os.environ.get("KAGGLE_KEY")

# if not kaggle_username or not kaggle_key:
#     raise Exception("Please set KAGGLE_USERNAME and KAGGLE_KEY")

kaggle.api.authenticate()


def download_dataset(dataset_info):
    dataset_path = dataset_info.get_dataset_path()
    kaggle.api.dataset_download_files(f'{dataset_info.owner}/{dataset_info.name}', path=dataset_path, unzip=True)
    # api.dataset_download_files(f'{dataset_info.owner}/{dataset_info.name}', path=dataset_path, unzip=True)
    return dataset_path
