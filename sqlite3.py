import sqlite3

# データベースファイルを開く（存在しなければ作成される）
conn = sqlite3.connect('example.db')

# カーソルを取得する
cur = conn.cursor()

# テーブルの作成
cur.execute('''
    CREATE TABLE attend (
        id INTEGER PRIMARY KEY,
        name TEXT,
        date DATE,
        status TEXT
    )
''')

# データの挿入
cur.execute("INSERT INTO attend VALUES (1, 'Alice', '2022-03-20', 'present')")
cur.execute("INSERT INTO attend VALUES (2, 'Bob', '2022-03-21', 'absent')")

# 変更を保存する
conn.commit()

# データベースを閉じる
conn.close()
