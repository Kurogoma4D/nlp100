# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

from read_names import *
import subprocess
from pprint import pp

names = read_names()
replaced = list(map(lambda x: x.replace('\t', ' '), names))

pp([s for s in replaced[:5]])

subprocess.call(
    'cat popular-names.txt | sed -e "s/\t/ /g" | head -n 5', shell=True)
