# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

from files import *
import re
import itertools
import pprint

uk = read_sample_uk()

texts = list(map(lambda x: x.split('\n'), [s['text'] for s in uk]))
lines = itertools.chain.from_iterable(texts)

match_objects = list(map(lambda x: re.match(
    r'^(=+)([^=]*)(=+)', x), lines))

matches = [o for o in match_objects if bool(o)]

sections = [[o.group(2), len(o.group(1)) - 1] for o in matches]

pprint.pp(sections)
