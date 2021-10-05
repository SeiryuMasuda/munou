# -*- coding:utf-8 -*-
import MySQLdb


# DB接続する
conn = MySQLdb.connect(
user=' ',#ルート
passwd=' ',#パスワード
host=' ',#ホスト名
db=' ',#データベース名
charset='utf8')


#kakasi
from pykakasi import kakasi
    
kakasi = kakasi()
kakasi.setMode("H", "a")  # Hiragana to ascii
kakasi.setMode("K", "a")  # Katakana to ascii
kakasi.setMode("J", "a")  # Japanese(kanji) to ascii
kakasi.setMode("r", "Hepburn")  # Use Hepburn romanization
conv = kakasi.getConverter()
    
    
while True:
    k = input("文字を入力：")
    r = conv.do(k)
    c = conn.cursor()
    c.execute(' SELECT ' + r + ' FROM book2_2 ')
    d = c.fetchall()
    print(d)

# 接続を閉じる
conn.close()