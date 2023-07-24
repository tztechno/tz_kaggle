from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import MultiLabelBinarizer

multilabel_cols = ['japanese_name',"genres", "producers", "licensors", "studios"]
multilabel_dfs = list('01234')
n_components=10

for i,c in enumerate(multilabel_cols):
    list_srs = anime_df[c].map(lambda x: x.split(" ")).tolist()
    mlb = MultiLabelBinarizer()
    ohe_srs = mlb.fit_transform(list_srs)
    if c == "xxx":
        # ユニーク数が多くないのでOne-hot表現のまま
        col_df = pd.DataFrame(ohe_srs, columns=[f"ohe_{c}_{name}" for name in mlb.classes_])
    else:
        # ユニーク数が多いので、SVDで次元圧縮する
        svd = TruncatedSVD(n_components=10)
        svd_arr = svd.fit_transform(ohe_srs)
        col_df = pd.DataFrame(
            svd_arr,
            columns=[f"svd_{c}_{ix}" for ix in range(n_components)]
        )
    multilabel_dfs[i]=col_df

#multilabel_df = pd.concat(multilabel_dfs, axis=1)
#print(multilabel_df.shape)
