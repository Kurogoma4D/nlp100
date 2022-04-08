# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

from files import *
import re
import itertools
import pprint

uk = read_sample_uk()

texts = list(map(lambda x: x.split('\n'), [s['text'] for s in uk]))
lines = list(itertools.chain.from_iterable(texts))

pattern = r'\[\[(ファイル|File):(.+?)\|'
result = re.findall(pattern, '\n'.join(lines))

pprint.pp(result)
