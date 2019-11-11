import pandas as pd
import numpy as np


print("\n" + "___________________________________________________-STEP 2____________________________________________\n")
series_One = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
series_Two = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
series_Three = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))

print("\n" + "___________________________________________________-STEP 3____________________________________________\n")
houseExe = pd.concat([series_One, series_Two, series_Three], axis=1)
print(houseExe.head())

print("\n" + "___________________________________________________-STEP 4____________________________________________\n")
houseExe.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)
print(houseExe.head())

print("\n" + "___________________________________________________-STEP 5____________________________________________\n")
bigColumn = pd.concat([series_One, series_Two, series_Three], axis=0)
bigColumn = bigColumn.to_frame()
print(bigColumn)

print("\n" + "___________________________________________________-STEP 6____________________________________________\n")
print(len(bigColumn))

print("\n" + "___________________________________________________-STEP 7____________________________________________\n")

bigColumn.reset_index(drop=True, inplace=True)
print(bigColumn)