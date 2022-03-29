# 06. 集合
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

import n_gram
import pprint

para = 'paraparaparadise'
parad = 'paragraph'

x = n_gram.create_letter_bi_gram(para)
y = n_gram.create_letter_bi_gram(parad)

pprint.pp(f'x: {x}')
pprint.pp(f'y: {y}')

union = set(x + y)
intersection = set(x).intersection(set(y))
difference = set(x).difference(set(y))

pprint.pp(union)
pprint.pp(intersection)
pprint.pp(difference)

contains_x = 'se' in x
contains_y = 'se' in y

print(f'`se` contains x : {contains_x}')
print(f'`se` contains y : {contains_y}')
