from sklearn.feature_extraction.text import CountVectorizer

# サンプルのテキストデータ
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]

# CountVectorizerのインスタンスを作成
vectorizer = CountVectorizer()

# テキストデータをベクトル化
X = vectorizer.fit_transform(corpus)

# ベクトル化された結果を表示
print(X.toarray())

# 特徴語のリストを表示
print(vectorizer.get_feature_names())
