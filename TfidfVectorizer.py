from sklearn.feature_extraction.text import TfidfVectorizer

# サンプルの文書データ
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# TfidfVectorizerのインスタンスを作成
vectorizer = TfidfVectorizer()

# 文書データをTF-IDFベクトルに変換
tfidf_matrix = vectorizer.fit_transform(documents)

# 変換されたTF-IDF行列を表示
print(tfidf_matrix.toarray())

# 特徴語（単語）のリストを表示
print(vectorizer.get_feature_names_out())
