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
