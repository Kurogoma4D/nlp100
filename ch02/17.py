# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．

import sys
from read_names import *
import pprint
import subprocess

names = read_names()

col1 = set(sorted([s.split('\t')[0] for s in names]))

pprint.pp(col1)

subprocess.call(
    'cat popular-names.txt | cut -f 1 | sort | uniq', shell=True)
