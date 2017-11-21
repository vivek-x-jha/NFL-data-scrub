# This file is for importing, cleaning, and preparing the data for analysis
import numpy as np
import pandas as pd
from utility import abspaths_data
from utility import isEqualNumberOfColumns, isEqualMergeDimensions

"""Loading the data"""

period = range(2009, 2018)

# Creates generator expression containing absolute paths of play-by-play .csv files
abspaths_data_files = abspaths_data('nflscrapR-data/season_play_by_play/')

# Load data as Dictionary: values are play-by-play Dataframes (keyed by season)
pbp_dataframes = {season: pd.read_csv(file, low_memory=False) for season, file in zip(period, abspaths_data_files)}

"""Data Inspection"""

# Can view the metadata of each season by passing the year into `df_metadata`
pbp_metadata = lambda season: pbp_dataframes[season].info(verbose=False)

dimensions = [pbp_df.shape for pbp_df in pbp_dataframes.values()]

# Contains the respective number of rows/columns for each dataframe
rowSizes = [shape[0] for shape in dimensions]
avg_plays_per_game = np.mean(rowSizes) / 32 / 17

columnSizes = [shape[1] for shape in dimensions]

# Checks if all datasets have same number of features
assert isEqualNumberOfColumns(columnSizes)

"""Merge data vertically by season"""

pbp_merged = pd.concat(pbp_dataframes.values())
# print(pbp_merged.info(verbose=False))
assert isEqualMergeDimensions(rowSizes, columnSizes, pbp_merged)
