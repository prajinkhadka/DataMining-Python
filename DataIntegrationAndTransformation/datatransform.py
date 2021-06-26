
# Data types 
# Numerical - Nuemric data , quantifable data 
	# 1. Discrete - Discrete ( fixied vale)
	# 2. Continous - Data that is mesaurable is continus eg. height of person

# Categorical : String/Character, Qualitative 
	# Ordeted: Follows some order ( s, m, l, xl)
	# Nominal: No Ordering ( name of countires)



import numpy as np 
import pandas as pd 

dataset = "https://github.com/TrainingByPackt/Data-Science-with-Python/blob/master/Chapter01/Data/student.csv"

df = pd.read_csv(dataset, header = 0)

# handlingCategorical data 
# Spearate categorical columns
df_cat = df.select_dtpyes(exclue=[np.number])

# Grade is a categorical columsn.

print(df_cat['Grade'].unique())

# Number of datapoints in each category. 

print(df_cat['Grade'].value_counts())

# Replacing 1st Class: 1, 2nd Class:2, 3rd Class:3 with
df_cat.Grade.replace({'1st Class':1, "2nd Class":2, "3rd Class":3}, inplace=True)
df_cat.Gender.replace({"Male":0,"Female":1}, inplace= True)

