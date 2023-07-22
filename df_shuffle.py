#########################################################

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': ['a', 'b', 'c', 'd', 'e']})

shuffled_df = df.sample(frac=1).reset_index(drop=True)

#########################################################

shuffled_df_with_seed = df.sample(frac=1, random_state=42).reset_index(drop=True)
print(shuffled_df_with_seed)

#########################################################
