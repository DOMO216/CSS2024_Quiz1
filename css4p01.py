#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:46:35 2024

@author: thabangmolefi
"""

import pandas as pd
import numpy as np

df = pd.read_csv('movie_dataset.csv')

df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
"""

df.describe()
"""

              Rank         Year  ...  Revenue (Millions)   Metascore
count  1000.000000  1000.000000  ...          872.000000  936.000000
mean    500.500000  2012.783000  ...           82.956376   58.985043
std     288.819436     3.205962  ...          103.253540   17.194757
min       1.000000  2006.000000  ...            0.000000   11.000000
25%     250.750000  2010.000000  ...           13.270000   47.000000
50%     500.500000  2014.000000  ...           47.985000   59.500000
75%     750.250000  2016.000000  ...          113.715000   72.000000
max    1000.000000  2016.000000  ...          936.630000  100.000000

[8 rows x 7 columns]
"""

df.columns
"""
Index(['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year',
       'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)',
       'Metascore'],
      dtype='object'
"""
df.head()
"""
 Rank                    Title  ... Revenue (Millions) Metascore
0     1  Guardians of the Galaxy  ...             333.13      76.0
1     2               Prometheus  ...             126.46      65.0
2     3                    Split  ...             138.12      62.0
3     4                     Sing  ...             270.32      59.0
4     5            Suicide Squad  ...             325.02      40.0
"""

df.tail()
"""
     Rank                   Title  ... Revenue (Millions) Metascore
995   996    Secret in Their Eyes  ...                NaN      45.0
996   997         Hostel: Part II  ...              17.54      46.0
997   998  Step Up 2: The Streets  ...              58.01      50.0
998   999            Search Party  ...                NaN      22.0
999  1000              Nine Lives  ...              19.64      11.0

[5 rows x 12 columns]
"""

df.duplicated().sum()

df.isnull().sum()
"""

Out[10]: 
Rank                    0
Title                   0
Genre                   0
Description             0
Director                0
Actors                  0
Year                    0
Runtime (Minutes)       0
Rating                  0
Votes                   0
Revenue (Millions)    128
Metascore              64
dtype: int64
"""

# Question 1
highest_rated_movie = df.loc[df['Rating'].idxmax()]
"""
Rank                                                                 55
Title                                                   The Dark Knight
Genre                                                Action,Crime,Drama
Description           When the menace known as the Joker wreaks havo...
Director                                              Christopher Nolan
Actors                Christian Bale, Heath Ledger, Aaron Eckhart,Mi...
Year                                                               2008
Runtime (Minutes)                                                   152
Rating                                                              9.0
Votes                                                           1791916
Revenue (Millions)                                               533.32
Metascore                                                          82.0
Name: 54, dtype: object
"""


# Question 2
average = df["Revenue (Millions)"].mean()

df['Revenue (Millions)'].fillna(average, inplace=True)

new_average = df["Revenue (Millions)"].mean()

# Question 3
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]


average_revenue = filtered_df["Revenue (Millions)"].mean()


# Question 4
movies_in_2016 = (df['Year'] == 2016).sum()

#Question 5
movies_by_nolan = (df['Director'] == 'Christopher Nolan').sum()


# Question 6
highly_rated_movies = (df['Rating'] >= 8.0).sum()


# Question 7
nolan_movies = df[df['Director'] == 'Christopher Nolan']

median_rating_nolan = nolan_movies['Rating'].median()

# Question 8
average_rating_by_year = df.groupby('Year')['Rating'].mean()

highest_average_rating_year = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

# Question 9
movies_2006 = (df['Year'] == 2006).sum()
movies_2016 = (df['Year'] == 2016).sum()


percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100


# Question 10
all_actors = df['Actors'].str.split(', ')

all_actors_flat = [actor for sublist in all_actors for actor in sublist]

actor_counts = pd.Series(all_actors_flat).value_counts()

most_common_actor = actor_counts.idxmax()
most_common_actor_count = actor_counts.max()


# Question 11 
unique_genres =  len(df['Genre'].unique())

# Question 12 
numeric_columns = ['Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']
df_numeric = df[numeric_columns]

cm = df_numeric.corr()

print(cm)

"""
  Year  Runtime (Minutes)  ...  Revenue (Millions)  Metascore
Year                1.000000          -0.164900  ...           -0.117562  -0.079305
Runtime (Minutes)  -0.164900           1.000000  ...            0.247834   0.211978
Rating             -0.211219           0.392214  ...            0.189527   0.631897
Votes              -0.411904           0.407062  ...            0.607941   0.325684
Revenue (Millions) -0.117562           0.247834  ...            1.000000   0.133328
Metascore          -0.079305           0.211978  ...            0.133328   1.000000

[6 rows x 6 columns]

"""
