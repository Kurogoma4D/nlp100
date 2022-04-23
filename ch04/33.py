# 33. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．
from files import *
import pprint
import itertools


def extract(origin: list[dict[str, str]]) -> list[dict[str, str]]:
    extracted = []

    for i in range(1, len(origin) - 1):
        if origin[i-1]['pos'] == '名詞' and origin[i]['surface'] == 'の' and origin[i+1]['pos'] == '名詞':
            extracted.append(
                ''.join(map(lambda x: x['surface'], origin[i-1:i+2])))

    return extracted


neko = read_neko()
surfaces = list(filter(lambda x: len(x) != 0, map(extract, neko)))
result = set(itertools.chain.from_iterable(surfaces))

pprint.pp(result)
