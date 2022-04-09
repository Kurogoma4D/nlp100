# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

from files import *
import re
import itertools
import pprint
import requests


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

file_name = result_rm['国旗画像']

session = requests.Session()
URL = "https://ja.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",
    "titles": f'ファイル:{file_name}'
}

response = session.get(url=URL, params=PARAMS)
obtained_url = re.search(r'"url":"(.+?)"', response.text).group(1)

pprint.pp(obtained_url)
