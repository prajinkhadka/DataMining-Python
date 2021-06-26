
university_towns = list()

with open('datasets/university_towns.txt') as file:
    for line in file:
        if '[edit]' in line:
            state = line 
            print(state)
        else:
            university_towns.append((state, line))

print(university_towns[:5])


# Convert ot dataframe 
import pandas as pd 
town_df = pd.DataFrame(university_towns, columns=['State', 'RegionName']
)

town_df.to_csv("datasets/university_town.csv")


