# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import pprint


def read_file(name: str) -> list[str]:
    with open(name) as f:
        lines = f.readlines()

    return list(map(lambda x: x.replace('\n', ''), lines))


def read_line(line: str) -> dict[str, str]:
    surface, remain = line.split('\t')
    elements = remain.split(',')
    return {
        'surface': surface,
        'base': elements[6],
        'pos': elements[0],
        'pos1': elements[1],
    }


def read_neko() -> list[list[dict[str, str]]]:
    lines = read_file('./neko.txt.mecab')

    statement = []
    result = []
    for l in lines:
        if l == 'EOS':
            result.append(statement)
            statement = []
            continue
        statement.append(read_line(l))

    return result


neko = read_neko()

pprint.pp(neko[2])
