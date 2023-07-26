############################################################

from sklearn.utils import shuffle

# Assuming you have your data and labels in separate arrays or lists
data = [...]  # Your data, e.g., a list of feature vectors
labels = [...]  # Your corresponding labels, e.g., a list of target values

# Shuffle the data and labels together while maintaining the correspondence between them
data_shuffled, labels_shuffled = shuffle(data, labels, random_state=42)  # You can use any random_state value you like

############################################################

from sklearn.utils import shuffle

dff = shuffle(df)
df = dff.sample(frac=0.10, replace=False, random_state=1)#Change the rate of f

############################################################
