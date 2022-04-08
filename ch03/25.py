# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

from files import *
import re
import itertools
import pprint

uk = read_sample_uk()

texts = list(map(lambda x: x.split('\n'), [s['text'] for s in uk]))
lines = list(itertools.chain.from_iterable(texts))
text = '\n'.join(lines)

template_pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
template = re.findall(template_pattern, text, re.MULTILINE + re.DOTALL)

pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))

pprint.pp(result)
