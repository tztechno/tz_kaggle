# thereshold bigger, original_work_name smaller

# threshold=0.6  n=1
# threshold=0.51  n=1
# threshold=0.501  n=1
# threshold=0.5001  n=1
# threshold=0.5  n=633 ##### BEST
# threshold=0.4  n=1197
# threshold=0.2  n=1590
# threshold=0.1  n=1790

from tqdm.notebook import tqdm
from itertools import combinations
from IPython.display import display
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import DisjointSet
import Levenshtein

def get_original_work_name(df, threshold=0.5):

    _feature = df.japanese_name.tolist()
    _n = df.shape[0]

    _disjoint_set = DisjointSet(list(range(_n)))
    for i, j in tqdm(combinations(range(_n), 2)):
        if _feature[i] is np.nan or _feature[j] is np.nan:
            lv_dist, jw_dist = 0.5, 0.5
        else:
            lv_dist = 1 - Levenshtein.ratio(_feature[i], _feature[j])
            jw_dist = 1 - Levenshtein.jaro_winkler(_feature[i], _feature[j])
        _d = (lv_dist + jw_dist) / 2

        if _d < threshold:
            _disjoint_set.merge(i, j)

    _labels = [None] * _n
    for subset in _disjoint_set.subsets():
        label = _feature[list(subset)[0]]
        for element in subset:
            _labels[element] = label
    df["original_work_name"] = _labels

    return df


processed_anime_df = get_original_work_name(anime_df)
print(f"raw - japanese_name nunique: {anime_df.japanese_name.nunique()}")
print(f"processed - japanese_name nunique: {processed_anime_df.original_work_name.nunique()}")
#display(processed_anime_df.head(40))
