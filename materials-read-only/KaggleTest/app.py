import kaggle

kaggle.api.authenticate
dataset_owner = "sazidthe1"
dataset_name = "world-population-data"
path = "./resource"

kaggle.api.dataset_download_files(f'{dataset_owner}/{dataset_name}', path=path, unzip=True)