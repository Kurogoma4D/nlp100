# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

from read_names import *
import subprocess
from pprint import pp

col1 = read_file('col1.txt')
col2 = read_file('col2.txt')

col1 = list(map(lambda x: x.replace('\n', ''), col1))
col2 = list(map(lambda x: x.replace('\n', ''), col2))
merged = [f'{col1[i]}\t{col2[i]}' for i in range(len(col1))]
write_file('merged.txt', '\n'.join(merged))


subprocess.call('paste col1.txt col2.txt > merged-shell.txt', shell=True)
