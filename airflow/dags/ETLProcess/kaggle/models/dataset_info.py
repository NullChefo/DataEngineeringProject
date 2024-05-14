class DatasetInfo:
    def __init__(self, owner: str, name: str, destination_path: str):
        self.owner = owner
        self.name = name
        self.destination_path = destination_path

    def get_dataset_path(self):
        base_path = "~/kaggle_datasets"
        return f"{base_path}/{self.destination_path}"
