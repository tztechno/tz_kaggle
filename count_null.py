import numpy as np
n_missing_prices = np.count_nonzero(np.isnan(reviews['price']))


missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)


# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()


# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()
