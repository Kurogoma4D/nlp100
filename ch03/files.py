import gzip
import json
import re


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


def read_sample_uk() -> list[dict[str, str]]:
    sample = read_sample()
    return [s for s in sample if re.match('.*イギリス.*', s['title'])]
