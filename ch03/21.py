# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

from files import *
import re
import itertools
import pprint

uk = read_sample_uk()

texts = list(map(lambda x: x.split('\n'), [s['text'] for s in uk]))
lines = itertools.chain.from_iterable(texts)

matches = [s for s in lines if re.match(r'^\[\[Category:', s)]

pprint.pp(matches)
