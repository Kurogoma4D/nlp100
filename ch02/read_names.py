def read_names() -> list[str]:
    with open('./popular-names.txt') as f:
        lines = f.readlines()

    return lines
