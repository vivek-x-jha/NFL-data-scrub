# This file is for importing, cleaning, and preparing the data for analysis
import pandas as pd
from utility import abspaths_data

# '09 season - '17 season
period = range(2009, 2018)

# Creates generator expression containing absolute paths of play-by-play .csv files
abspaths_data_files = abspaths_data('nflscrapR-data/season_play_by_play/')

# Load data as Dictionary
## keys -> season
## values -> play-by-play Dataframes
pbp_dataframes = {season: pd.read_csv(file) for season, file in zip(period, abspaths_data_files)}

# Checks if pbp_dataframes have same number of columns
columns = [pbp_df.shape[1] for pbp_df in pbp_dataframes.values()]
assert min(columns) == max(columns)
