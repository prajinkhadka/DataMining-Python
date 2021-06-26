import pandas as pd 
import numpy as np 

# example dataframe
df = pd.DataFrame({'a': [0, 1, 2, 3], 
                   'b': [4, 5, np.nan, 7], 
                   'c': [8, 9, 10, 11]})

# apply log(x+1) element-wise to a subset of columns
to_log = ['a', 'b']
df_log = df[to_log].applymap(lambda x: np.log(x+1))

# rename columns
df_log.columns = 'log_' + df_log.columns

# shift the index
df_log.index = df_log.index + 1