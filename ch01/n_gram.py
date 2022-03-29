def n_gram(input_list: list[str], n: int, conjection: str = ' ') -> list[str]:
    assert n > 1
    assert len(input_list) >= n
    ans = []  # type: list[str]
    for i in range(len(input_list) - (n - 1)):
        ans.append(conjection.join([input_list[j + i] for j in range(n)]))
    return ans


def create_word_bi_gram(input_str: str) -> list[str]:
    words = input_str.split(' ')
    return n_gram(words, 2)


def create_letter_bi_gram(input_str: str) -> list[str]:
    words = list(input_str.replace(' ', ''))
    return n_gram(words, 2, '')
