# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

from files import *
import re
import itertools
import pprint

uk = read_sample_uk()

texts = list(map(lambda x: x.split('\n'), [s['text'] for s in uk]))
lines = itertools.chain.from_iterable(texts)

match_objects = list(map(lambda x: re.match(
    r'^\[\[Category:(.*)\]\]', x), lines))

matches = [o for o in match_objects if bool(o)]

categories = [o.group(1) for o in matches]

pprint.pp(categories)
