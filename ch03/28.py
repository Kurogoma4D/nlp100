# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

from files import *
import re
import itertools
import pprint


def remove_markup(text: str) -> str:
    p = r'\'{2,5}'
    text = re.sub(p, '', text)

    p = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
    text = re.sub(p, r'\1', text)

    p = r'https?://[\w!?/\+\-_~=;\.,*&@#$%\(\)\'\[\]]+'
    text = re.sub(p, '', text)

    p = r'<.+?>'
    text = re.sub(p, '', text)

    p = r'\{\{(?:lang|仮リンク)(?:[^|]*?\|)*?([^|]*?)\}\}'
    text = re.sub(p, r'\1', text)

    return text


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
