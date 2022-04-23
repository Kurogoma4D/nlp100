# 31. 動詞
# 動詞の表層形をすべて抽出せよ．

from files import *
import pprint
import itertools


def extract_surface_of_verb(origin: list[dict[str, str]]) -> list[dict[str, str]]:
    extracted = filter(lambda x: x['pos'] == '動詞', origin)
    return list(map(lambda x: x['surface'], extracted))


neko = read_neko()
surfaces = list(filter(lambda x: len(x) != 0,
                       map(extract_surface_of_verb, neko)))
result = set(itertools.chain.from_iterable(surfaces))

pprint.pp(result)
