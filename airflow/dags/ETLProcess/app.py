# from ETLProcess.db_connector import get_data_from_table, load_to_table

# From the airflow ui errors out with missing module if you are not adding ETLProcess
from ETLProcess.db_ops import load_imdb_top_1000_database, load_netflix_imdb_database, \
    load_imdb_movies_dataset_database, \
    get_data_from_table, load_to_table, load_the_transformed_data_to_database

from ETLProcess.kaggle.models.dataset_info import DatasetInfo
from ETLProcess.kaggle.download_datasets import download_dataset
import pandas as pd

# (Kaggle -> MSSQL -> PostgreSQL).


# Kaggle objects
imdb_top_1000_info = DatasetInfo('harshitshankhdhar', 'imdb-dataset-of-top-1000-movies-and-tv-shows', 'imdb-top-1000')
imdb_movies_dataset_info = DatasetInfo('ashpalsingh1525', 'imdb-movies-dataset', 'imdb_movies_dataset')
netflix_imdb_scores_info = DatasetInfo('thedevastator', 'netflix-imdb-scores', 'netflix-imdb-scores')


def download_datasets():
    download_dataset(imdb_top_1000_info)
    download_dataset(imdb_movies_dataset_info)
    download_dataset(netflix_imdb_scores_info)

    print(f"Downloaded dataset to: {imdb_top_1000_info.get_dataset_path()}")
    print(f"Downloaded dataset to: {imdb_movies_dataset_info.get_dataset_path()}")
    print(f"Downloaded dataset to: {netflix_imdb_scores_info.get_dataset_path()}")


def transform_data():
    imdb_top_1000_dataframe = get_data_from_table("imdb_top_1000", "mysql")
    imdb_movies_dataframe = get_data_from_table("imdb_movies", "mysql")
    netflix_imdb_scores_dataframe = get_data_from_table("netflix_imdb", "mysql")

    imdb_top_100_df = imdb_top_1000_dataframe.rename(columns={
        'Series_Title': 'Title',
        'Released_Year': 'Release_Year',
        'IMDB_Rating': 'IMDB_Score',
        'No_of_Votes': 'Votes',
        'Meta_score': 'Meta_Score'
    })

    netflix_imdb_df = netflix_imdb_scores_dataframe.rename(columns={
        'title': 'Title',
        'release_year': 'Release_Year',
        'imdb_score': 'IMDB_Score',
        'imdb_votes': 'Votes'
    })

    imdb_movies_df = imdb_movies_dataframe.rename(columns={
        'date_x': 'Release_Year',
        'score': 'IMDB_Score',
        'orig_title': 'Title',
        'budget_x': 'Budget',
        'orig_lang': 'Original_Language'
    })

    merged_df = pd.concat([imdb_top_100_df, netflix_imdb_df, imdb_movies_df], ignore_index=True)

    all_data_df = merged_df.loc[~merged_df.index.duplicated(keep='first')]
    #
    # # Reset the index to avoid duplicate index values
    # all_data_df = all_data_df.reset_index(drop=True)

    # Fill NaN/None values
    all_data_df = all_data_df.fillna(999)
    #
    # # Convert all columns to VARCHAR in the DataFrame
    all_data_df = all_data_df.astype(str)

    return merged_df


def load_to_db():
    # load the data to mysql
    try:
        print(f"Loading dataset to: {netflix_imdb_scores_info.destination_path}")
        netflix_imdb_scores_info_path = f"~/kaggle_datasets/{netflix_imdb_scores_info.destination_path}"
        load_netflix_imdb_database("netflix_imdb", "mysql", netflix_imdb_scores_info_path)
    # errors
    except Exception as e:
        print("Error while loading data to db: " + str(e))
        raise Exception(e)
    # if no errors
    else:
        print("Datasets has been loaded")

    # load the data to mysql
    try:
        print(f"Loading dataset to: {imdb_top_1000_info.destination_path}")
        imdb_top_1000_info_path = f"~/kaggle_datasets/{imdb_top_1000_info.destination_path}"
        load_imdb_top_1000_database("imdb_top_1000", "mysql", imdb_top_1000_info_path)
    # errors
    except Exception as e:
        print("Error while loading data to db: " + str(e))
        raise Exception(e)
    # if no errors
    else:
        print("Datasets has been loaded")

    # load the data to mysql
    try:
        print(f"Loading dataset to: {imdb_movies_dataset_info.destination_path}")
        imdb_movies_dataset_info_path = f"~/kaggle_datasets/{imdb_movies_dataset_info.destination_path}"
        load_imdb_movies_dataset_database("imdb_movies", "mysql", imdb_movies_dataset_info_path)
    # errors
    except Exception as e:
        print("Error while loading data to db: " + str(e))
        raise Exception(e)
    # if no errors
    else:
        print("Datasets has been loaded")


def execute_load():
    # Download the assets
    try:
        download_datasets()
    # errors
    except Exception as e:
        print("Error while downloading: " + str(e))
    # if no errors
    else:
        print("Datasets has been downloaded")

    # Load the data to mysql
    try:
        load_to_db()
    # errors
    except Exception as e:
        print("Error while loading to db: " + str(e))
    # if no errors
    else:
        print("Datasets has been loaded")

    # Transform data
    try:
        dataframe = transform_data()
        print("\n Merged dataframe: " + str(dataframe))
        load_the_transformed_data_to_database("DIM_MOVIES", "postgresql", dataframe)
    # errors
    except Exception as e:
        print("Error while transforming data: " + str(e))
    # if no errors
    else:
        print("Datasets has been transformed")
