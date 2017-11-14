# This file is for importing, cleaning, and preparing the data for analysis
import pandas as pd
import numpy as np

# Reads in the CSV's as play-by-play dataframes classified by season (2009 - 2017)
pbp_folder = 'nflscrapR-data/data/season_play_by_play/pbp_'
pbp_csv_datasets = {year: f'{pbp_folder}{year}.csv' for year in range(2009, 2018)}

pbp2009 = pd.read_csv(pbp_csv_datasets[2009])
pbp2010 = pd.read_csv(pbp_csv_datasets[2010])
pbp2011 = pd.read_csv(pbp_csv_datasets[2011])
pbp2012 = pd.read_csv(pbp_csv_datasets[2012])
pbp2013 = pd.read_csv(pbp_csv_datasets[2013])
pbp2014 = pd.read_csv(pbp_csv_datasets[2014])
pbp2015 = pd.read_csv(pbp_csv_datasets[2015])
pbp2016 = pd.read_csv(pbp_csv_datasets[2016])
pbp2017 = pd.read_csv(pbp_csv_datasets[2017])

datasets = [pbp2009, pbp2010, pbp2011, pbp2012, pbp2013, pbp2014, pbp2015, pbp2016, pbp2017]

# Checks if datasets have same number of columns
columns = [pbpYEAR.shape[1] for pbpYEAR in datasets]
assert min(columns) == max(columns)

# print(pbp201.info())
# print(pbp201.head(10))
# print(pbp201.tail(10))
# print(pbp2009.head(10))
