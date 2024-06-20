
------------------------------------------------------

import sqlite3
import numpy as np
import pandas as pd
import os

db_path='/kaggle/input/sqlite-sakila-sample-database/sqlite-sakila.db'


# Connect to SQLite database
connection = sqlite3.connect(db_path)


# Get a cursor
cursor = connection.cursor()


# Query to fetch table names
query = "SELECT name FROM sqlite_master WHERE type='table';"


# Execute the query and fetch table names
cursor.execute(query)
tables = cursor.fetchall()
print(tables)


# Execute the query and get the results
for table in tables:
    print()
    print('================='*4) 
    print(table[0])
    print('-----------------'*2) 
    query = f"SELECT * FROM {table[0]};"    
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows[0:3]:
        print(row)

------------------------------------------------------

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

------------------------------------------------------
