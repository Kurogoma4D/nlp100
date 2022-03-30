# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

from read_names import *
import subprocess

names = read_names()
print(len(names))

subprocess.call(['wc', '-l', './popular-names.txt'])
