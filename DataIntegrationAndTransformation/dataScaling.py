import pandas as pd

dataset = 'https://github.com/TrainingByPackt/Data-Science-with-Python/blob/master/Chapter01/Data/Wholesale%20customers%20data.csv'

df = pd.read_csv(dataset, header=0)

# check for null values 
null_ = df.isna().any()
dtypes = df.dtypes

info = pd.concat([null_,dtypes],axis = 1,keys = ['Null','type'])

print(info)

# StandardScalaer 
## Using scikit learn 
import sklearn

std_scale = sklearn.preprocessing.StandardScaler().fit_transform(df)

scaled_frame = pd.DataFrame(std_scale, columns=df.columns)

print(scaled_frame.head())

# MinMax Scaler 
minmax_scale = sklearn.preprocessing.MinMaxScaler().fit_transform(df)

scaled_frame = pd.DataFrame(minmax_scale,columns=df.columns)

