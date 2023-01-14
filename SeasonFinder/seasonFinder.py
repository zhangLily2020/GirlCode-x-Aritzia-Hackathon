#0 -> neutral
#1 -> cool/ light
#2 -> warm/ dark
import pandas as pd
import numpy as np
from random import *

results = []

def compute_hc() -> None:
    light_hc = ['chesnut', 'dark brown', 'red', 'strawberry', 'blonde', 'amber']
    dark_hc = ['black', 'ashy brown', 'grey', 'ashy blonde']

    while True:
        hc = input("")
        if hc in light_hc:
            results.append(1)
            return
        elif hc in dark_hc:
            results.append(2)
            return
        else:
            print("invalid color: please enter a new one")

def compute_undertone() -> None:
    warm_tone = ['warm']
    cool_tone = ['cool']
    neutral_tone = ['cannot tell']

    while True:
        ut = input("")
        if ut in warm_tone:
            results.append(2)
            return
        elif ut in cool_tone:
            results.append(1)
            return
        elif ut in neutral_tone:
            results.append(0)
        else:
            print("invalid answer: please enter a new one")

def find_color(season: str) -> str:
    i = randint(0,3)
    if season == 'spring':
        return spring[i]
    elif season == 'fall':
        return fall[i]
    elif season == 'winter':
        return winter[i]
    else:
        return summer[i]

print("Please choose from one of the following undertone of your skin:")
print("warm | cool | cannot tell")

compute_undertone()

print("Please choose from one of the following hair colors:")
print("chesnut | ashy brown | grey | blonde | chesnut")
print("dark brown | red | ashy blonde | amber | black")

compute_hc()

print("Do you wear glasses?")
print("yes | no")
input()

print("What is your eye color?")
print("amber | blue | brown | grey | hazel | red")
input()

season = ""

if(results[0] == 1):
    if results[1] == 1:
        season = "winter"
    if results[1] == 2:
        season = "summer"
else:
    if results[1] == 2:
        season = "spring"
    else:
        season = "fall"

print("your season is: ", season)

spring = ['yellow','brown','white','black']
summer = ['violet','yellow','grey','white']
fall = ['green','yellow','brown','red']
winter = ['red', 'violet', 'blue', 'green']


color = find_color(season)
print("your color is: ", color)
print("---------------")
print("Computing similar clothing...")

data = 'SeasonFinder/stfore_train.xlsx'

# print(pd.read_excel('restocks.csv', usecols = [0]))
df = pd.read_excel(data)

sorted = df.loc[df['color'].isin([color])]

# for i in sorted.index:
#     print(df['category'][i])

df_trends = pd.read_excel('SeasonFinder/most_trendy.xlsx')
sl = sorted.values.tolist()
tl = df_trends.values.tolist()


c = 0
jan16 = tl[4][2]
jan17 = tl[50][2]
jan19 = tl[42][2]
duplicate = []
for _ in range(len(sorted.index) - 1):
    i = randint(3, len(sorted.index)-3)
    if c == 10:
        break
     
    if (sl[i][3] == jan16 or sl[i][3] == jan17 or sl[i][3] == jan19) and sl[i][5] not in duplicate:
        print(sl[i][0:7])
        duplicate.append(sl[i][5])
        c += 1


    

# for _ in range(len(sorted.index) - 3):war
#     i =3
#     a = df_trends['most_trendy_material'][50]
#     c = df_trends['most_trendy_material'][15]
#     d = df_trends['most_trendy_material'][38]

#     b = sorted['fabric'][i]
#     if a == b or b == c or b == d:
#         pass
#     i += 1


# for _ in range(10):
#     i = randint(3, len(sorted.index)-3)
#     print(sl[i][0:7])
#     print("----------")


    










