import pandas as pd
import numpy as np
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|')
usersDict = dict()
age = dict()

occupationsList = list()
occupationsList = users.occupation
ageList = users.age
for occupation in users.occupation:
    if occupation not in usersDict:
        usersDict[occupation] = 1

    else:
        usersDict[occupation]+=1

for key, value in usersDict.items() :
    position = 0;
    count = 0;
    for occupationValue in occupationsList:
        if key == occupationValue:
            count =  count + ageList[position]
            position += 1
        else:
            position+= 1

    #print("Mean age for the occupation " + key + " is", count/value, "\n")


print("\n" + "___________________________________________________-STEP 4____________________________________________\n")
print(users.groupby("occupation", as_index=False)["age"].mean())

male_ratio = users.pivot_table(index='occupation', columns='gender', aggfunc='size', fill_value=0)

# calculate male ratio
sums = male_ratio[['F', 'M']].sum(axis=1)
male_ratio['MaleRatio'] = round(100 * male_ratio['M'] / sums , 1)
print("\n" + "___________________________________________________-STEP 5 ___________________________________________\n")
# result
print("\n", male_ratio)

print("\n" + "___________________________________________________-STEP 6 ___________________________________________\n")
print("Maximum ages as per the occupation:")
print(users.groupby("occupation", as_index=False)["age"].max())

print("\nMinimum ages as per the occupation:")
print(users.groupby("occupation", as_index=False)["age"].min())
print("\n" + "___________________________________________________-STEP 7 ___________________________________________\n")
print(users.groupby(["occupation", "gender"], as_index=False)["age"].mean())

print("\n" + "___________________________________________________-STEP 8 ___________________________________________\n")
gender_ocup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})


occup_count = users.groupby(['occupation']).agg('count')


occup_gender = gender_ocup.div(occup_count, level = "occupation") * 100

print(" For each occupation the percentage of women and men")
print(occup_gender.loc[: , 'gender'])