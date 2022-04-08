# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

from files import *
import re
import itertools
import pprint


def remove_markup(text: str) -> str:
    p = r'\'{2,5}'
    return re.sub(p, '', text)


uk = read_sample_uk()

texts = list(map(lambda x: x.split('\n'), [s['text'] for s in uk]))
lines = list(itertools.chain.from_iterable(texts))
text = '\n'.join(lines)

template_pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
template = re.findall(template_pattern, text, re.MULTILINE + re.DOTALL)

pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))
result_rm = {k: remove_markup(v) for k, v in result.items()}

pprint.pp(result_rm)
