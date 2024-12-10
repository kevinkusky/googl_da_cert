"""
    Pandas

    dataframes
        Methods
            apply, copy, describe, drop, groupby, head(n), 
            info, isna, sort_values, value_counts, where
        Attributes
            Columns, dtypes, iloc, loc, shape, values
    series

    null - NaN
"""
import numpy as np
import pandas as pd

# Not naming row indexs allows for enumerated 'named' indicies
df = pd.DataFrame({
   'A': ['alpha', 'apple', 'arsenic', 'angel', 'android'],
   'B': [1, 2, 3, 4, 5],
   'C': ['coconut', 'curse', 'cassava', 'cuckoo', 'clarinet'],
   'D': [6, 7, 8, 9, 10]
   },
   index=['row_0', 'row_1', 'row_2', 'row_3', 'row_4'])
print(df)

# Rows
# Returns row as a series object
print(df.loc['row_1'])
print(df.iloc[1])

# returns selected row(s) as df
print(df.loc[['row_1']])
print(df.iloc[[1]])
print(df.loc[['row_1', 'row_2']])
print(df.loc['row_0': 'row_3']) # named indicies are inclusive
print(df.iloc[0: 3]) # index are non-inclusive

# Columns
# Selectors
print(df['C'])
print(df.A) # dot notation works on columns

print(df[['A', 'C']])
print(df.loc[:, ['B', 'D']]) # All rows, columns B and D
print(df.iloc[:, [1, 3]]) # All rows, columns B and D

# pylint: disable=pointless-string-statement
"""
    Utilizing loc and iloc, rows must also be specified
    Cannot mixed numeric and named indicies (row_1 and column at index 2)

    To view rows [0:3] at column ‘D’ (if you don’t know the index number of column D)
    use selector brackets after an iloc[] statement:
"""

# This is most convenient for VIEWING:
print(df.iloc[0:3][['D']])

# But this is best practice/more stable for assignment/manipulation:
print(df.loc[df.index[0:3], 'D'])

# Follwoing errors out when row names are indexed
# print(df.loc[0:3, ['D']])

"""
    Boolean Masking
    View filtering that does not alter data
    & - and
    | - or
    ~ - not
"""
# Instantiate a dictionary of planetary data.
data = {'planet': ['Mercury', 'Venus', 'Earth', 'Mars',
                   'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
       'radius_km': [2440, 6052, 6371, 3390, 69911, 58232,
                     25362, 24622],
       'moons': [0, 0, 1, 2, 80, 83, 27, 14]
        }
# Use pd.DataFrame() function to convert dictionary to dataframe.
planets = pd.DataFrame(data)
print(planets)

# Create boolean mask based on dataframe and conditional logic
mask = planets['moons'] < 20

# Apply mask to dataframe
print(planets[mask])
print(planets[planets['moons'] < 20]) # in-line works too

# Create a Boolean mask of planets with more than 20 moons, excluding them if they
# have 80 moons or if their radius is less than 50,000 km.
mask_2 = (planets['moons'] > 20) & ~(planets['moons'] == 80) & ~(planets['radius_km'] < 50000)

# Apply the mask
print(planets[mask_2]) # Saturn

"""
    Grouping and Aggregation

    groupby()
        - Aggreggation Functions built in:
            count, sum, mean, median, min, max, std, var
    
    agg()
        - apply multible functions
"""

clothes = pd.DataFrame({'type': ['pants', 'shirt', 'shirt', 'pants', 'shirt', 'pants'],
                       'color': ['red', 'blue', 'green', 'blue', 'green', 'red'],
                       'price_usd': [20, 35, 50, 40, 100, 75],
                       'mass_g': [125, 440, 680, 200, 395, 485]})


print(clothes)

grouped = clothes.groupby('type')
print(grouped) # <pandas.core.groupby.DataFrameGroupBy object at 0x7f995bf11198>
print(type(grouped)) # <class 'pandas.core.groupby.DataFrameGroupBy'>
print(grouped.mean()) # df of average for each numeric value

#              mass_g  price_usd
# type  color
# pants blue      200         40
#       red       125         20
# shirt blue      440         35
#       green     395         50
print(clothes.groupby(['type', 'color']).min())


# type   color
# pants  blue     1
#        red      2
# shirt  blue     1
#        green    2
# dtype: int64
print(clothes.groupby(['type', 'color']).size())


# Agg
#       price_usd      mass_g
#            mean  max   mean  max
# color
# blue       37.5   40  320.0  440
# green      75.0  100  537.5  680
# red        47.5   75  305.0  485
print(clothes.groupby('color').agg({'price_usd': ['mean', 'max'],
                             'mass_g': ['mean', 'max']}))

"""
    Merging new data into existing DataFrames

        Concat
            Axis
                Axis=0 - Vertical
                Axis=1 - Horizontal (consider merge)

        Merge
            Keys (on='column_name')
                how=inner
                how=outer
                how=left
                how=right
"""



