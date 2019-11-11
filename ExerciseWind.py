import pandas as pd
import datetime

print("\n" + "___________________________________________________-STEP 3____________________________________________\n")
url_Data = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'

data = pd.read_csv(url_Data, sep = "\s+", parse_dates = [[0,1,2]])
print(data.head())

print("\n" + "___________________________________________________-STEP 4____________________________________________\n")
def fix_year(x):

    if x.year > 1989:
        year = x.year - 100
    else:
        year = x.year

    return datetime.date(year, x.month, x.day)

data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_year)
print(data.head())




print("\n" + "___________________________________________________-STEP 5____________________________________________\n")
data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])
data = data.set_index('Yr_Mo_Dy')

print(data.head())

print("\n" + "___________________________________________________-STEP 6____________________________________________\n")
print(data.isnull().sum())

print("\n" + "___________________________________________________-STEP 7____________________________________________\n")
print(data.notnull().sum())

print("\n" + "___________________________________________________-STEP 8____________________________________________\n")
print(data.fillna(0).values.flatten().mean())

print("\n" + "___________________________________________________-STEP 9____________________________________________\n")
print(data.describe(percentiles=[]))

print("\n" + "___________________________________________________-STEP 10____________________________________________\n")
day_stats = pd.DataFrame()


day_stats['min'] = data.min(axis = 1)
day_stats['max'] = data.max(axis = 1)
day_stats['mean'] = data.mean(axis = 1)
day_stats['std'] = data.std(axis = 1)

print(day_stats.head())

print("\n" + "___________________________________________________-STEP 11____________________________________________\n")

print(data.loc[data.index.month == 1].mean())

print("\n" + "___________________________________________________-STEP 12____________________________________________\n")

print(data.groupby(data.index.to_period('A')).mean())

print("\n" + "___________________________________________________-STEP 13____________________________________________\n")
print(data.groupby(data.index.to_period('M')).mean())
print("\n" + "___________________________________________________-STEP 14____________________________________________\n")

print(data.groupby(data.index.to_period('W')).mean())

print("\n" + "___________________________________________________-STEP 15____________________________________________\n")

weekly = data.resample('W').agg(['min','max','mean','std'])

print(weekly.loc[weekly.index[1:53], "RPT":"MAL"] .head(10))
