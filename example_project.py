"""
    Pandas Lab utilizing given data and tasks to manipulate data
    via pandas to practice 
"""
import numpy as np
import pandas as pd


top3 = pd.read_csv('epa_ca_tx_pa.csv')
print(top3.head())

# MetaData
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 546 entries, 0 to 545
# Data columns (total 5 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   state_code   546 non-null    int64
#  1   state_name   546 non-null    object
#  2   county_code  546 non-null    int64
#  3   county_name  546 non-null    object
#  4   aqi          546 non-null    float64
# dtypes: float64(1), int64(2), object(2)
# memory usage: 21.5+ KB
print(top3.info())

# Summary statistics
#       state_code  county_code     aqi
# count	546.000000	546.000000	546.000000
# mean	20.593407	83.179487	8.906593
# std	19.001484	92.240873	9.078479
# min	6.000000	1.000000	0.000000
# 25%	6.000000	29.000000	3.000000
# 50%	6.000000	66.000000	6.000000
# 75%	42.000000	98.500000	11.000000
# max	48.000000	479.000000	93.000000
print(top3.describe())

# California      342
# Texas           104
# Pennsylvania    100
# Name: state_name, dtype: int64
print(top3['state_name'].value_counts())

top3_sorted = top3.sort_values(by=['aqi'], ascending=False)
print(top3_sorted.head(10))

ca_mask = top3_sorted['state_name'] == 'California'
ca_df = top3_sorted[ca_mask]

print(ca_df.head())
print(ca_df.shape()) # 342 - matches value_counts output

print(ca_df[ca_df['county_name'] == 'Los Angeles']['aqi'].mean()) # mean of aqi for LA

# 	                aqi
#                   mean
# state_name
# California	    9.412281
# Pennsylvania	    6.690000
# Texas	            9.375000

# print(top3.groupby('state_name').agg({'aqi': ['mean']}))
print(top3.groupby('state_name').mean()[['aqi']])

# Adding new data
other_states = pd.read_csv('epa_others.csv')
combined_df = pd.concat([top3, other_states], axis=0)

# Show increased length of data
print(len(combined_df) > len(top3))

# According to the EPA, AQI values of 51-100 are considered of "Moderate" concern.
# You've been tasked with examining some data for the state of Washington.
concern_mask = (combined_df['aqi'] >= 51) & (combined_df['aqi'] <=100)
moderate_aqi = combined_df[concern_mask]
print(moderate_aqi.head())
