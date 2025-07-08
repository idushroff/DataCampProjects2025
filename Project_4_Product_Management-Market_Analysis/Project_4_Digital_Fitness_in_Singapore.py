'''Task: to do a market analysis to understand how to place digital fitness products in Singapore.

The project is provided with a number of CSV files which offer international data on Google Trends and YouTube keyword
searches related to fitness and related products. Two helper functions have also been provided, read_file and read_geo,
to help process and visualize these CSV files for further analysis.

1. Determine the month with the highest global fitness interest using pandas and other coding methods. Store the month in
the variable month_str.

2. Analyze global interest in three keywords and identify the keyword with the most interest from 2022 to 2023 (variable
current) and during 2020 (variable peak_covid).

3. Extract the top 25 countries with the highest interest in workouts from the geo_three_keywords.csv file and save it as
MESA.

4. Analyze the split of interest in these three keywords in the MESA countries by country and category. Identify the
country with the highest interest in home workouts and save it as top_home_workout_country.

5. Analyze YouTube keyword searches to identify the top two media types (excluding "workout") worth piloting in digital
form in Singapore and Philippines. Store these media types in the list pilot_content.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='white', palette = 'Pastel2')
import os

filepath = '/home/lumi/PyCharmProjects/DataCampProjects2025/Project_4_Product_Management-Market_Analysis/'

three_keywords = filepath + 'three_keywords.csv'
'''Week  home workout: (Worldwide) gym workout: (Worldwide) home gym: (Worldwide)'''

geo_three_keywords = filepath + 'geo_three_keywords.csv'
'''Country  home workout: (3/16/18 - 3/16/23) gym workout: (3/16/18 - 3/16/23)  home gym: (3/16/18 - 3/16/23)'''

workout_global = filepath + 'workout_global.csv'
'''Country    workout: (3/16/18 - 3/16/23) '''

workout = filepath + 'workout.csv'
'''Week  workout: (Worldwide) '''

yoga_zumba_phl = filepath + 'yoga_zumba_phl.csv'
'''Week    yoga: (Philippines) workout: (Philippines) zumba: (Philippines) bodybuilding: (Philippines)  weight loss: (Philippines)'''

print(pd.read_csv(workout, header=0))

def read_file(filepath, plot = True):
    """
    Read a CSV file from a given filepath, convert it into a pandas DataFrame
    and return a processed DataFrame with three columns: 'week', 'region', and 'interest'.
    Generate a line plot using Seaborn to visualize the data.
    This corresponds to the first graphic (time series) returned by trends.google.com
    """
    file = pd.read_csv(filepath, header=1)
    df=file.set_index('Week').stack().reset_index()
    df.columns = ['week', 'region', 'interest']
    df['week'] = pd.to_datetime(df['week'])
    plt.figure(figsize=(8,3))
    df=df[df['interest']!="<1"]
    df['interest']= df['interest'].astype(float)

    if plot:
        sns.lineplot(data=df, x='week', y='interest', hue='region')
    return df

print(read_file(workout))
workout_by_month = workout.set_index('week').resample('MS').mean()
month_high = workout_by_month[workout_by_month['interest']==workout_by_month['interest'].max()]
month_str = str(month_high.index[0].date())

def read_geo(filepath, multi=False):
    """
    Read a CSV file from a given filepath, convert it into a pandas DataFrame,
    and return a processed DataFrame with two columns: 'country' and 'interest'. Generate a bar plot using Seaborn to visualize the data. This corresponds to the second graphic returned by trends.google.com. Use multi=False if only one keyword is being analyzed, and multi=True if more than one keyword is being analyzed.
    """
    file = pd.read_csv(filepath, header=1)

    if not multi:
        file.columns = ['country', 'interest']
        plt.figure(figsize=(8,4))
        sns.barplot(data = file.dropna().iloc[:25,:], y = 'country', x='interest')

    if multi:
        plt.figure(figsize=(3,8))
        file = file.set_index('Country').stack().reset_index()
        file.columns = ['country','category','interest']
        file['interest'] = pd.to_numeric(file['interest'].apply(lambda x: x[:-1]))
        sns.barplot(data=file.dropna(), y = 'country', x='interest', hue='category')

    file = file.sort_values(ascending=False,by='interest')
    return file

print(read_geo(filepath1))