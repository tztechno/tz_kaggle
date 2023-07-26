def one_hot_to_category(one_hot_encoded, categories):
    index = np.argmax(one_hot_encoded, axis=1)
    return [categories[i] for i in index]
