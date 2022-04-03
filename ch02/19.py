# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

import sys
from read_names import *
import pprint
import subprocess

names = read_names()

numbers = {}
for line in names:
    key = line.split('\t')[0]
    if key not in numbers.keys():
        numbers[key] = 0
    num = numbers[key]
    numbers[key] = num + 1

s = {k: v for k, v in reversed(sorted(numbers.items(), key=lambda x: x[1]))}
pprint.pp(s)

subprocess.call(
    'cat popular-names.txt | cut -f 1 | sort | uniq -c | sort -r', shell=True)
