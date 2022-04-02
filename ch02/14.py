# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

import sys
from read_names import *
import pprint
import subprocess

n = int(sys.argv[1])
names = read_names()

for l in names[:n]:
    print(l.replace('\n', ''))

print('\n')

subprocess.call('cat popular-names.txt | head -n 5', shell=True)
