# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

import sys
from read_names import *
import pprint
import subprocess

names = read_names()

names.sort(key=lambda x: int(x.split('\t')[2].replace('\n', '')))
names.reverse()

pprint.pp([names[i] for i in range(5)])

subprocess.call(
    'cat popular-names.txt | sort -r -k 3 | head -n 5', shell=True)
