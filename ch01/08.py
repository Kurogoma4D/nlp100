# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# - 英小文字ならば(219 - 文字コード)の文字に置換
# - その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

import re


def match(match: re.Match) -> str:
    return chr(219 - ord(match.group()))


def cipher(input_str: str) -> str:
    return re.sub(r'[a-z]', match, input_str)


print(cipher('パイソンのstr'))
