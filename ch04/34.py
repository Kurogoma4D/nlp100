# 34. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
from files import *
import pprint
import itertools


def extract(origin: list[dict[str, str]]) -> list[dict[str, str]]:
    extracted = []

    i = 0
    while i < len(origin) - 1:
        if origin[i]['pos'] == '名詞' and origin[i+1]['pos'] == '名詞':
            j = i
            while j < len(origin) and origin[j]['pos'] == '名詞':
                j += 1

            extracted.append(
                ''.join(map(lambda x: x['surface'], origin[i:j])))
            i = j
        else:
            i += 1

    return extracted


neko = read_neko()
surfaces = list(filter(lambda x: len(x) != 0, map(extract, neko)))
result = set(itertools.chain.from_iterable(surfaces))

pprint.pp(result)
