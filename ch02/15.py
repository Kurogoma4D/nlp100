# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import sys
from read_names import *
import pprint
import subprocess

n = int(sys.argv[1]) + 1
names = read_names()
tail = names[:-n:-1]
tail.reverse()

for l in tail:
    print(l.replace('\n', ''))

print(len(names[:-n:-1]))

print('\n')

subprocess.call('cat popular-names.txt | tail -n 5', shell=True)
