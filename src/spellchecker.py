import re
from collections import defaultdict
from pathlib import Path
from typing import Tuple, Final, Pattern, Dict, List, Set

TOKENIZE_PTRN: Final[Pattern] = re.compile(r'[\w-]+')


def tokenize(text: str) -> Tuple[str]:
    tokens = re.findall(TOKENIZE_PTRN, text.lower())
    # noinspection PyTypeChecker
    return tuple(tokens)


class SimpleSpellchecker:
    LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    NGRAM_PATH: Final = Path('data')
    FILE_NAME_NGRAMS1: Final = '1grams-3-top-200000.txt'
    FILE_NAME_NGRAMS2: Final = '2grams-3-top-500000.txt'
    FILE_NAME_NGRAMS3: Final = '3grams-3-top-700000.txt'

    def __init__(self):
        self.freqs1: defaultdict[str, int] = defaultdict(int)
        self.freqs2: defaultdict[Tuple[str, str], int] = defaultdict(int)
        self.freqs3: defaultdict[Tuple[str, str, str], int] = defaultdict(int)
        self._load_data()

    def _correct_middle_token(self, tokens: List[str]) -> str:
        token = tokens[2]
        candidates = self._get_transforms(token)
        print(f'{candidates = }')
        ranking: List[Tuple[str, int, int, int]] = []
        for candidate in candidates:
            ranking.append(self._get_ngram_scores(tokens[0:2] + [candidate] + tokens[3:5]))
        ranking.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
        print(f'{ranking = }')
        return ranking[0][0]

    def _get_ngram_scores(self, tokens: List[str]) -> Tuple[str, int, int, int]:
        score3 = (
            self.freqs3[(tokens[0], tokens[1], tokens[2])]
            + self.freqs3[(tokens[1], tokens[2], tokens[3])]
            + self.freqs3[(tokens[2], tokens[3], tokens[4])]
        )
        score2 = (
            self.freqs2[(tokens[1], tokens[2])]
            + self.freqs2[(tokens[2], tokens[3])]
        )
        score1 = self.freqs1[tokens[2]]
        return (
            tokens[2],
            score3,
            score2,
            score1,
        )

    def _get_transforms(self, token: str) -> Set[str]:
        splits = [(token[:i], token[i:]) for i in range(len(token) + 1)]
        deletes = [left + right[1:] for left, right in splits if right]
        transposes = [
            left + right[1] + right[0] + right[2:] for left, right in splits if len(right) > 1
        ]
        replaces = [left + c + right[1:] for left, right in splits if right for c in self.LETTERS]
        inserts = [left + c + right for left, right in splits for c in self.LETTERS]
        candidates = [
            cand for cand in deletes + transposes + replaces + inserts if cand in self.freqs1
        ]
        return set(candidates)

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
                corrected_token = self._correct_middle_token(tokens[i - 2: i + 3])
                tokens[i] = corrected_token
        return ' '.join(tokens[2:-2])
