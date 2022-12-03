import re
from collections import defaultdict
from pathlib import Path
from typing import Tuple, Final, Pattern, Dict

TOKENIZE_PTRN: Final[Pattern] = re.compile(r'[\w-]+')


def tokenize(text: str) -> Tuple[str]:
    tokens = re.findall(TOKENIZE_PTRN, text.lower())
    # noinspection PyTypeChecker
    return tuple(tokens)


class SimpleSpellchecker:
    NGRAM_PATH: Final = Path('data')
    FILE_NAME_NGRAMS1: Final = '1grams-3-top-200000.txt'
    FILE_NAME_NGRAMS2: Final = '2grams-3-top-500000.txt'
    FILE_NAME_NGRAMS3: Final = '3grams-3-top-700000.txt'

    def __init__(self):
        self.freqs1: defaultdict[str, int] = defaultdict(int)
        self.freqs2: defaultdict[Tuple[str, str], int] = defaultdict(int)
        self.freqs3: defaultdict[Tuple[str, str, str], int] = defaultdict(int)
        self._load_data()

    def _load_data(self) -> None:
        for file_name, freqs in (
            (self.FILE_NAME_NGRAMS1, self.freqs1),
            (self.FILE_NAME_NGRAMS2, self.freqs2),
            (self.FILE_NAME_NGRAMS3, self.freqs3),
        ):
            with open(Path(self.NGRAM_PATH, file_name), 'r', encoding='utf-8') as ngrams_file:
                for line in ngrams_file:
                    freq, ngram = line.split(maxsplit=1)
                    freq = int(freq)
                    ngram = tokenize(ngram)
                    if len(ngram) == 1:
                        ngram = ngram[0]  # tuple -> str for unigrams
                    freqs[ngram] += freq

            self.freqs1['*'] = 1
            self.freqs1['$'] = 1

    def check(self, text: str) -> str:
        print(f'{text = }')
        tokens = tokenize(text)
        tokens = ['*', '*'] + list(tokens) + ['$', '$']
        print(f'{tokens = }')
        for i in range(2, len(tokens) - 2):
            token = tokens[i]
            if token not in self.freqs1:
                print(f'unknown {token = }')
                # todo correct the token
                pass
        return text
