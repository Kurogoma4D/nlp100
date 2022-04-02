def read_names() -> list[str]:
    return read_file('./popular-names.txt')


def read_file(name: str) -> list[str]:
    with open(name) as f:
        lines = f.readlines()

    return lines


def write_file(name: str, lines: str):
    with open(name, mode='w') as f:
        f.write(lines)
