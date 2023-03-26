#virtual_rating_dataset

import numpy as np
import pandas as pd

# Set up parameters
num_users = 100
num_items = 100
min_rating = 1
max_rating = 5
num_scores = 20

# Generate random user and item IDs
user_ids = np.arange(num_users)
item_ids = np.arange(num_items)

# Generate random scores
scores = np.random.randint(min_rating, max_rating+1, size=(num_users*num_scores, 3))

# Assign user and item IDs to scores
user_indices = np.random.choice(user_ids, size=num_users*num_scores)
item_indices = np.random.choice(item_ids, size=num_users*num_scores)
scores[:, 0] = user_indices
scores[:, 1] = item_indices

# Shuffle the scores
np.random.shuffle(scores)

# Split the scores into training and test sets
num_train = int(len(scores) * 0.8)
train_scores = scores[:num_train]
test_scores = scores[num_train:]

# Convert to pandas dataframes
train_df = pd.DataFrame(train_scores, columns=['user_id', 'item_id', 'rating'])
test_df = pd.DataFrame(test_scores, columns=['user_id', 'item_id', 'rating'])

# Save the data to CSV files
train_df.to_csv('train_data.csv', index=False)
test_df.to_csv('test_data.csv', index=False)
