import pandas as pd

a = [1, 6, 10, 22, 16, 13, 20]

print(a)

seriesData = pd.Series(a)

print(seriesData)

print("Max Number:", seriesData.max())
print("Min Number", seriesData.min())

sorting = seriesData.sort_values()
sortingReverse = seriesData.sort_values(ascending=False)
print("Sort from lower: ", sorting)
print("Sort from higher: ", sortingReverse)

print(sorting[1:2])