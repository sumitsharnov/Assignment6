import pandas as pd
import numpy as np

print("\n" + "___________________________________________________-STEP 3____________________________________________\n")
euro12 = pd.read_table('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', sep=',')

print("\n" + "___________________________________________________-STEP 4____________________________________________\n")
print("Goals Columns\n", euro12.Goals)

print("\n" + "___________________________________________________-STEP 5____________________________________________\n")
print("Teams Participated in Euro 2012\n")
print(euro12.shape[0])

print("\n" + "___________________________________________________-STEP 6____________________________________________\n")
print("Number of columns\n")
print(len(euro12.columns))

print("\n" + "___________________________________________________-STEP 6____________________________________________\n")
print("Number of columns\n")
print(len(euro12.columns))

print("\n" + "___________________________________________________-STEP 7____________________________________________\n")
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

print("\n" + "___________________________________________________-STEP 8____________________________________________\n")
print(discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False))

print("\n" + "___________________________________________________-STEP 9____________________________________________\n")
print(round(euro12['Yellow Cards'].mean()))


print("\n" + "___________________________________________________-STEP 10____________________________________________\n")
print(euro12[euro12.Goals>6])


print("\n" + "___________________________________________________-STEP 11____________________________________________\n")
print(euro12[euro12.Team.str.startswith('G')])

print("\n" + "___________________________________________________-STEP 12____________________________________________\n")
print(euro12.iloc[: , 0:7])

print("\n" + "___________________________________________________-STEP 13____________________________________________\n")
print(euro12.iloc[: , :-3])

print("\n" + "___________________________________________________-STEP 14____________________________________________\n")
print(euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']])