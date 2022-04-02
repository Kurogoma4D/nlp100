# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

from read_names import *
import subprocess
from pprint import pp

names = read_names()

write_file('col1.txt', '\n'.join([s.split('\t')[0] for s in names]))
write_file('col2.txt', '\n'.join([s.split('\t')[1] for s in names]))


subprocess.call(
    'cat popular-names.txt | cut -f 1 > col1-shell.txt', shell=True)

subprocess.call(
    'cat popular-names.txt | cut -f 2 > col2-shell.txt', shell=True)
