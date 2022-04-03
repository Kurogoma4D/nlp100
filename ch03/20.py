# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

from files import *
import pprint
import re

sample = read_sample()
uk = [s for s in sample if re.match('.*イギリス.*', s['title'])]

pprint.pp(uk)
print(len(uk))
