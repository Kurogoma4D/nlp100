# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys
from read_names import *
import pprint
import subprocess

n = int(sys.argv[1])
names = read_names()

unit = len(names) // n
print(unit)
print(len(names))
for i in range(n):
    splitted = names[i*unit:(i+1)*unit]
    write_file(f'splitted-{i}.txt', ''.join(splitted))

print('\n')

# gsplitの行数分割がよくわからなかったので一旦スキップ
subprocess.call('gsplit -n 5 popular-names.txt', shell=True)
