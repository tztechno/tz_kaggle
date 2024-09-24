############################################################

from sklearn.utils import shuffle

data_shuffled, labels_shuffled = shuffle(data, labels, random_state=42) 

############################################################

from sklearn.utils import shuffle

dff = shuffle(df)
df = dff.sample(frac=0.10, replace=False, random_state=1)#Change the rate of f

############################################################

shuffled_df_with_seed = df.sample(frac=1, random_state=42).reset_index(drop=True)

print(shuffled_df_with_seed)

#########################################################

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': ['a', 'b', 'c', 'd', 'e']})

shuffled_df = df.sample(frac=1).reset_index(drop=True)

#########################################################
