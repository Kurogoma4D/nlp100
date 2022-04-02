def read_names() -> list[str]:
    with open('./popular-names.txt') as f:
        lines = f.readlines()

    return lines


def write_file(name: str, lines: str):
    with open(name, mode='w') as f:
        f.write(lines)
