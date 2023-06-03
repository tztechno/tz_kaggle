
単純な比較:
df.query("列名 > 5")

複数の条件を組み合わせる場合:
df.query("列名1 > 5 and 列名2 == '値'")
df.query("`class` == 'person' and `confidence` > 0.2")
df.query("(`class` == 'car' or `class` == 'truck') and `confidence` > 0.2")

文字列の一致を確認する場合:
df.query("列名.str.contains('キーワード')")

変数を使用する場合:
name = 'John'
df.query("Name == @name")

注意事項:
列名は引用符で囲まないでください。
文字列を比較する場合、引用符で囲む必要があります。
変数を使用する場合、変数名の前に「@」を付ける必要があります。
