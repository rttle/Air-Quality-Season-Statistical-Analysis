#importing packages
import numpy as np
import matplotlib.pyplot as plt #visualization
import pandas as pd

#function for categorizing data by season
def season_category(column):
  if 'Winter' in column:
    return 'Winter'
  elif 'Summer' in column: #else not used because 'Time Period' column includes more than just seasonal time periods
    return 'Summer'

#Apply preprocessing found in 'AirQuality_Preprocessing' notebook
def load_preprocess_data(file):
    df=pd.read_csv(file)

    #dropping column with 'NULL' values
    df=df.dropna(axis=1)
    df=df.drop_duplicates() #dropping any duplicates

    #creating new column 'Season'
    df['Season']=df['Time Period'].apply(season_category)

    #removal of datapoints with no season data
    df=df.dropna()

    return df