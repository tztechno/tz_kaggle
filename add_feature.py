
#####################################################

def categorize_data_train_test(train, test, column_name, n_categories=5):
    """
    トレーニングデータに基づいてカテゴリ境界を決め、テストデータにも同じ境界を適用する関数。
    
    Parameters:
    - train: pandas DataFrame (トレーニングデータ)
    - test: pandas DataFrame (テストデータ)
    - column_name: 数値データの列名
    - n_categories: カテゴリー数（デフォルトは5）
    
    Returns:
    - train: カテゴリを追加したトレーニングデータ
    - test: カテゴリを追加したテストデータ
    """
    # トレーニングデータの最小値と最大値を取得
    min_value = train[column_name].min()
    max_value = train[column_name].max()

    # 境界値を等間隔で設定
    bins = np.linspace(min_value, max_value, n_categories + 1)

    # トレーニングデータをカテゴリに変換
    train[column_name + '_category'] = np.digitize(train[column_name], bins, right=True)

    # テストデータにも同じ境界を適用
    test[column_name + '_category'] = np.digitize(test[column_name], bins, right=True)
    
    return train, test
#####################################################

def categorize_data(df, column_name, n_categories=5):
    """
    指定した列の数値データを最大最小を基にn段階にカテゴライズする関数。
    
    Parameters:
    - df: pandas DataFrame
    - column_name: 数値データの列名
    - n_categories: カテゴリー数（デフォルトは5）
    
    Returns:
    - df: カテゴリを追加したDataFrame
    """
    # 指定した列の最小値と最大値を取得
    min_value = df[column_name].min()
    max_value = df[column_name].max()

    # 境界値を等間隔で設定
    bins = np.linspace(min_value, max_value, n_categories + 1)

    # データをカテゴリに変換
    df[column_name + '_category'] = np.digitize(df[column_name], bins, right=True)
    
    return df

#####################################################
import itertools
import pandas as pd

def create_combined_features(df, columns):
    combined_features = {}
    
    # Iterate through all pairs of columns
    for col1, col2 in itertools.combinations(columns, 2):
        # Create new column name
        new_col_name = f"{col1}_{col2}"
        # Create combined feature
        combined_features[new_col_name] = df[col1].astype(str) + "_" + df[col2].astype(str)
    
    # Convert dictionary to DataFrame
    df_combined = pd.concat([df, pd.DataFrame(combined_features)], axis=1)
    
    return df_combined, list(combined_features.keys())

#####################################################

from sklearn.preprocessing import OneHotEncoder

def one_hot_encode(df, columns):
    """
    df: pandas DataFrame
    columns: list of column names that contain categorical data
    
    Returns a DataFrame with One-Hot Encoding applied to the specified columns.
    """
    encoder = OneHotEncoder(sparse=False, drop='first')
    one_hot_encoded = encoder.fit_transform(df[columns])
    
    # Create a DataFrame for the one-hot encoded columns
    one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(columns))
    
    # Drop the original categorical columns and concatenate the one-hot encoded columns
    df_encoded = pd.concat([df.drop(columns, axis=1), one_hot_df], axis=1)
    
    return df_encoded
#####################################################


#####################################################
One-Hot Encoding の代替方法
もし カテゴリが多い場合、以下のような代替エンコーディング方法を検討することもできます：

ターゲットエンコーディング (Target Encoding):
各カテゴリに対してターゲット変数の平均を割り当てる方法です。これにより、次元数を増やさずにカテゴリの情報をモデルに伝えることができます。特に回帰や分類問題で有効ですが、過学習のリスクがあるため、適切な交差検証や正則化が必要です。

頻度エンコーディング (Frequency Encoding):
各カテゴリの出現頻度を特徴量として使う方法です。これにより、次元数を抑えながらカテゴリの情報を表現できます。

埋め込み層 (Embedding Layer):
ニューラルネットワークを使用している場合、カテゴリデータを低次元の埋め込みベクトルに変換することができます。この方法では、各カテゴリをベクトルで表現し、そのベクトル空間内で学習を進めることができます。高次元のカテゴリデータに対して効率的であり、特にディープラーニングにおいて効果的です。

ハッシュエンコーディング (Hashing Encoding):
カテゴリ数が非常に多い場合に、カテゴリを一定のハッシュ値にマッピングする方法です。これにより、メモリを節約できますが、ハッシュ衝突が起こる可能性があるため、注意が必要です。
#####################################################
この式は一般的ではない（カテゴリの組み合わせエンコーディングで、割り算を使う方法はほぼ見ない）。
Label Encoding を使う方法は、ペア (c1, c2) の全組み合わせを個別にユニークな整数へ変換するため、衝突の心配がない。
------------------------------------------------
# NEW FEATURE - COMBINATIONS OF CATS
PAIRS = []
for i,c1 in enumerate(CATS[:-1]):
    for j,c2 in enumerate(CATS[i+1:]):
        n = f"{c1}_{c2}"
        m1 = train[c1].max()+1
        m2 = train[c2].max()+1
        train[n] = ((train[c1]+1 + (train[c2]+1)/(m2+1))*(m2+1)).astype("int8")
        test[n] = ((test[c1]+1 + (test[c2]+1)/(m2+1))*(m2+1)).astype("int8")
        COMBO.append(n)
        PAIRS.append(n)
        
#####################################################
この方法では、digit{i+1} の最大値 M に対して M+1 を超える 11 を掛けていますが、
カテゴリの組み合わせがユニークになる保証はない ため、衝突（異なる (c1, c2) が同じ値になる）が発生する可能性があります。
Label Encoding を使う方法は、ペア (c1, c2) の全組み合わせを個別にユニークな整数へ変換するため、衝突の心配がない。
------------------------------------------------
# NEW FEATURE - COMBINATIONS OF DIGITS 
for i in range(4):
    for j in range(i+1,5):
        n = f"digit_{i+1}_{j+1}"
        train[n] = ((train[f'digit{i+1}']+1)*11 + train[f'digit{j+1}']+1).astype("int8")
        test[n] = ((test[f'digit{i+1}']+1)*11 + test[f'digit{j+1}']+1).astype("int8")
        COMBO.append(n)
#####################################################
数字の桁ごとの特徴量を作成する手法は、特に数値の各桁が何らかの意味を持つ場合や、桁ごとに異なる情報を抽出したい場合に有効です
------------------------------------------------
# NEW FEATURE - DIGIT EXTRACTION FROM WEIGHT CAPACITY
for k in range(1,10):
    train[f'digit{k}'] = ((train['Weight Capacity (kg)'] * 10**k) % 10).fillna(-1).astype("int8")
    test[f'digit{k}'] = ((test['Weight Capacity (kg)'] * 10**k) % 10).fillna(-1).astype("int8")
DIGITS = [f"digit{k}" for k in range(1,10)]
#####################################################
Weight Capacity (kg)をそれぞれ小数点以下7桁、8桁、9桁に丸めるという処理を行います。
------------------------------------------------
# NEW FEATURE - BIN WEIGHT CAPACITY USING ROUNDING
for k in range(7,10):
    n = f"round{k}"
    train[n] = train["Weight Capacity (kg)"].round(k)
    test[n] = test["Weight Capacity (kg)"].round(k)
    COMBO.append(n)
#####################################################
この特徴量は、NaN（欠損値）の存在をビットフラグとして格納するために使われます。初期値はすべて0です。
------------------------------------------------
CATS=test.columns.tolist()
COMBO = ["NaNs"]
train["NaNs"] = np.float32(0)
test["NaNs"] = np.float32(0)

for i,c in enumerate(CATS):

    # NEW FEATURE - ENCODE ALL NAN AS ONE BASE-2 FEATURE
    train["NaNs"] += train[c].isna()*2**i
    test["NaNs"] += test[c].isna()*2**i

    # NEW FEATURE - COMBINE EACH COLUMN'S NAN WITH WEIGHT CAPACITY
    n = f"{c}_nan_wc"
    train[n] = train[c].isna()*100 + train["Weight Capacity (kg)"]
    test[n] = test[c].isna()*100 + test["Weight Capacity (kg)"]
    COMBO.append(n)
    
    combine = pd.concat([train[c],test[c]],axis=0)
    combine,_ = pd.factorize(combine)
    train[c] = combine[:len(train)].astype("float32")
    test[c] = combine[len(train):].astype("float32")
    n = f"{c}_wc"
    train[n] = train[c]*100 + train["Weight Capacity (kg)"]
    test[n] = test[c]*100 + test["Weight Capacity (kg)"]
    COMBO.append(n)
#####################################################
