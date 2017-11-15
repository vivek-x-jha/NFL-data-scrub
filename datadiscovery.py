# This file is for importing, cleaning, and preparing the data for analysis
import pandas as pd

# Reads in the CSV's as play-by-play dataframes classified by season

period = range(2009, 2018)  # '09 season - '17 season
pbp_csv_PATH = 'nflscrapR-data/data/season_play_by_play/'

# Dictionary containing paths of play-by-play csv files
## dict pbp_csv_DIRECTORY[<int season>] -> str 'nflscrapR-data/data/season_play_by_play/pbp_<season>.csv'
pbp_csv_DIRECTORY = {season: f'{pbp_csv_PATH}pbp_{season}.csv' for season in period}

# Dictionary containing play-by-play data as DataFrames
## dict pbp_dataframes[<int season>] -> dataframe_obj pbp_<season>
pbp_dataframes = {season: pd.read_csv(file) for season, file in pbp_csv_DIRECTORY.items()}

# Checks if pbp_dataframes have same number of columns
columns = [pbp_df.shape[1] for season, pbp_df in pbp_dataframes.items()]
# columns = [pbp_dataframes[season].shape[1] for season in pbp_dataframes]

assert min(columns) == max(columns)

# print(pbp201.info())
# print(pbp201.head(10))
# print(pbp201.tail(10))
# print(pbp2009.head(10))
