# ヘルパー関数: Countを生成する関数 (例としてユニーク値のカウントを用意)
def _generate_count_feature(series):
    value_counts = series.value_counts().to_dict()  # マッピングを生成
    return series.map(value_counts), value_counts

# 訓練データ用の特徴量生成関数
def create_count_feature_train(input_df):
    use_columns = ['brakePressed', 'gasPressed', 'gearShifter', 'leftBlinker', 'rightBlinker']
    output_df = pd.DataFrame()
    mappings = {}  # 変換時のマッピング情報を保存

    for c in use_columns:
        x, mapping = _generate_count_feature(input_df[c])  # カウント特徴量とマッピングを生成
        output_df[f"{c}_count"] = x
        mappings[c] = mapping  # マッピングを保存

    return output_df, mappings

def create_count_feature_test(input_df, mappings):
    use_columns = ['brakePressed', 'gasPressed', 'gearShifter', 'leftBlinker', 'rightBlinker']
    output_df = pd.DataFrame()

    for c in use_columns:
        # 訓練データのマッピングを用いて変換
        output_df[f"{c}_count"] = input_df[c].map(mappings[c]).fillna(0)

    return output_df
