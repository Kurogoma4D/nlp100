import gzip
import json


def read_gzip(name: str) -> list[str]:
    with gzip.open(name, mode='rt') as f:
        lines = f.readlines()

    return lines


def read_sample() -> list[dict[str, str]]:
    sample = read_gzip('./jawiki-country.json.gz')
    decoded = list(map(lambda x: json.loads(x), sample))
    return decoded


def write_file(name: str, lines: str):
    with open(name, mode='w') as f:
        f.write(lines)
