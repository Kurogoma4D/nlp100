# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading: the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．

import random


def randomize(i: str) -> str:
    if (len(i) <= 4):
        return i
    return i[0] + ''.join(random.sample(i[1:-1], len(i) - 2)) + i[-1]


def typoglycemia(input_str: str) -> str:
    words = input_str.split(' ')
    return ' '.join(map(randomize, words))


example = 'I couldn’t believe that I could actually understand what I was reading: the phenomenal power of the human mind .'
print(example)
print(typoglycemia(example))
