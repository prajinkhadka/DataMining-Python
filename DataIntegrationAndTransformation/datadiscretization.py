
# Data Discretization is the process of converting continous data into discrete bucket by using binnning methods

import pandas as pd

dataset = "https://github.com/TrainingByPackt/Data-Science-with-Python/blob/master/Chapter01/Data/Student_bucketing.csv"

df = pd.read_csv(dataset, header = 0)

df['bucket']=pd.cut(df['marks'],5,labels=['Poor','Below_average','Average','Above_Average','Excellent'])