# 35. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

from files import *
import pprint
import itertools


neko = flatten_neko()
hist = {}

for word in neko:
    s = word['surface']
    count = hist.get(s, 0)
    hist[s] = count + 1

result = {k: v for k, v in sorted(hist.items(), key=lambda x: x[0])}
pprint.pp(result)
