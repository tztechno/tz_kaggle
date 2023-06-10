##############################

n=len(data_df3)
N=list(range(n))
random.seed(100)
M=random.sample(N,3000)
data_df4=data_df3.iloc[M].reset_index(drop=True)

##############################

import random

def weighted_random_choice(choices, weights):
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(choices, weights):
        if upto + w >= r:
            return c
        upto += w

choices = [1, 2, 3, 4, 5, 6]
weights = [1, 1, 1, 2, 2, 2]  # 大きい数字の重みを増やす

rating = weighted_random_choice(choices, weights)

##############################
