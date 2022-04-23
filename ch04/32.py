# 32. 動詞の基本形
# 動詞の基本形をすべて抽出せよ．
from files import *
import pprint
import itertools


def extract_base_of_verb(origin: list[dict[str, str]]) -> list[dict[str, str]]:
    extracted = filter(lambda x: x['pos'] == '動詞', origin)
    return list(map(lambda x: x['base'], extracted))


neko = read_neko()
surfaces = list(filter(lambda x: len(x) != 0,
                       map(extract_base_of_verb, neko)))
result = set(itertools.chain.from_iterable(surfaces))

pprint.pp(result)
