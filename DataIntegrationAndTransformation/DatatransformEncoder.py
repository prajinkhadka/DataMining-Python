
# Label Encoding 
## -> Replacing each value in categorical column wiht number 0 ot N-1. 
## Will be using scikit learn label encoder() 


import numpy as np 
import pandas as pd 

dataset = 'https://github.com/TrainingByPackt/Master-Data-Science-with-Python/blob/master/Chapter%201/Data/Banking_Marketing.csv'

df = pd.read_csv(dataset, header=0)
# drop missing ros 
df = df.dropna()

# select non-numeric colums.

data_column_category = df.select_dtypes(exclude=[np.number]).columns

from sklearn.preprocessing import LabelEncoder

# object instantication 
label_encoder = LabelEncoder()

for i in data_column_category:
    df[i] = label_encoder.fit_transform(df[i])
   

 # One Hot Encoding
dataset_bank = 'https://github.com/TrainingByPackt/Master-Data-Science-with-Python/blob/master/Chapter%201/Data/Banking_Marketing.csv'

#reading the data into the dataframe into the object data

df_bank = pd.read_csv(dataset_bank, header=0)
df_bank.dropna(inplace=True)

data_column_category_bank = df_bank.select_dtypes(exclude=[np.number]).columns

# First perform label encoding.

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder = LabelEncoder()

for i in data_column_category_bank:
    df_bank[i] = label_encoder.fit_transform(df_bank[i])

onehot_encoder = OneHotEncoder(sparse=False)
onehot_encoded = onehot_encoder.fit_transform(df[data_column_category_bank])

onehot_encoded_frame_bank = pd.DataFrame(onehot_encoded, columns = onehot_encoder.get_feature_names(data_column_category_bank))