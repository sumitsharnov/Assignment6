import pandas as pd
import numpy as np

print("\n" + "___________________________________________________-STEP 3____________________________________________\n")
chipo = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')


print("\n" + "___________________________________________________-STEP 4____________________________________________\n")
print(chipo.iloc[:10])

print("\n" + "___________________________________________________-STEP 5____________________________________________\n")
print("\n Number of Observations", chipo.shape)
print("\nSolution 2")
print("\n" , chipo.count(axis=0))

print("\n" + "___________________________________________________-STEP 6____________________________________________\n")
print("Number of columns ", len(chipo.columns))

print("\n" + "___________________________________________________-STEP 7____________________________________________\n")
print("Name of columns \n")
for columnName in chipo.columns:
     print(columnName + "\n")

print("\n" + "___________________________________________________-STEP 8____________________________________________\n")
print("Index : ", chipo.index)

print("\n" + "___________________________________________________-STEP 9____________________________________________\n")
print("Most ordered Item:", chipo.item_name.value_counts().head(1))

print("\n" + "___________________________________________________-STEP 10____________________________________________\n")
total_items = chipo.item_name.value_counts()


print("Number of items ordered: \n", total_items)


print("\n" + "___________________________________________________-STEP 11____________________________________________\n")
print("Most ordered item in the choice_description column", chipo.choice_description.value_counts().head(1))

print("\n" + "___________________________________________________-STEP 12____________________________________________\n")
total_orders = chipo.quantity.sum()
print("Number of Items order in total:", total_orders)
print("\n" + "___________________________________________________-STEP 13____________________________________________\n")
#chipo['item_price'] = pd.to_numeric(chipo['item_price'],errors='coerce')
prices = list()
prices = chipo.item_price
for price in prices:
    chipo.item_price = str(price).replace('$', '')

chipo['item_price'] = chipo['item_price'].astype(float)
print(chipo['item_price'])
print(chipo.dtypes)


print("\n" + "___________________________________________________-STEP 14____________________________________________\n")
print("Revenue: ", chipo.item_price.sum())

print("\n" + "___________________________________________________-STEP 15____________________________________________\n")

print("Number of orders: ", chipo.order_id.value_counts().count())

print("\n" + "___________________________________________________-STEP 16____________________________________________\n")
order_grouped = chipo.groupby(by=['order_id']).sum()
print("Average amount per order",order_grouped.mean()['item_price'])
print("\n" + "___________________________________________________-STEP 17____________________________________________\n")
print("Different Items sold", chipo.item_name.value_counts().count())