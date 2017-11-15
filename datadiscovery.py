# This file is for importing, cleaning, and preparing the data for analysis
import numpy as np
import pandas as pd
from utility import abspaths_data

"""Loading the data"""

period = range(2009, 2018)

# Creates generator expression containing absolute paths of play-by-play .csv files
abspaths_data_files = abspaths_data('nflscrapR-data/season_play_by_play/')

# Load data as Dictionary: values are play-by-play Dataframes (keyed by season)
# User on StackOverflow warned about storing dataframes in dictionaries???
# Seems ok for now...but will keep this in mind as project/data grows
pbp_dataframes = {season: pd.read_csv(file) for season, file in zip(period, abspaths_data_files)}

"""Data Inspection"""

# Can view the metadata of each season by passing the year into `df_metadata`
df_metadata = lambda season: pbp_dataframes[season].info(verbose=False)

# TODO inspect why 2011 season only has 23414 values (all other seasons have 44K-45K plays)
#  Could the 2017 (current/unfinished) season be falsely tagged as 2011 season?
# If so, we need to check key-value pairs of `pbp_dataframes` are correct
print(df_metadata(2011)) 

dimensions = [pbp_df.shape for pbp_df in pbp_dataframes.values()]
rows = [shape[0] for shape in dimensions]
columns = [shape[1] for shape in dimensions]

# Checks if each season's dataset have same number of features
assert min(columns) == max(columns)

"""Merge data vertically by season"""

pbp_merged = pd.concat(pbp_dataframes.values())
assert pbp_merged.shape[0] == sum(rows)
assert pbp_merged.shape[1] == columns[np.random.randint(len(columns))]

print(pbp_merged.info(verbose=False))
