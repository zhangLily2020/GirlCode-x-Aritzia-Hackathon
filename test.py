import pandas as pd
import numpy as np

data = 'stfore_train.xlsx'

# print(pd.read_excel('restocks.csv', usecols = [0]))
df = pd.read_excel(data)

color = 'grey'

sorted = df.loc[df['color'].isin([color])]

print(sorted)
print(len(sorted.index))

sorted.reset_index()

for i in sorted.index:
    print(df['category'][i])

# for i, row in sorted.iterrows():
#     print(row)


