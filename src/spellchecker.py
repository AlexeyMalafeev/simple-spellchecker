import json
import re
from pathlib import Path
from typing import (
    Final,
    List,
    Pattern,
    Set,
    Sequence,
    Tuple,
)

TOKENIZE_PTRN: Final[Pattern] = re.compile(r'[\w-]+')


def do_nothing(*args, **kwargs) -> None:
    pass


def tokenize(text: str) -> Tuple[str]:
    tokens = re.findall(TOKENIZE_PTRN, text.lower())
    # noinspection PyTypeChecker
    return tuple(tokens)


class SimpleSpellchecker:
    LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    NGRAM_PATH: Final = Path('data')
    FILE_NAME_NGRAMS1: Final = '1grams-3.json'
    FILE_NAME_NGRAMS2: Final = '2grams-3.json'
    FILE_NAME_NGRAMS3: Final = '3grams-3.json'

    def __init__(self, print_steps: bool = False):
        self.freqs1: dict[str, int] = {}
        self.freqs2: dict[str, int] = {}
        self.freqs3: dict[str, int] = {}
        self._print = print if print_steps else do_nothing
        self._load_data()

    def _correct_middle_token(self, tokens: List[str]) -> str:
        token = tokens[2]
        candidates = self._get_transforms(token)
        self._print(f'{candidates = }')
        ranking: List[Tuple[str, int, int, int]] = [
            self._get_ngram_scores(tokens[:2] + [candidate] + tokens[3:5])
            for candidate in candidates
        ]
        if not ranking:
            return tokens[2]
        ranking.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
        self._print(f'{ranking = }')
        return ranking[0][0]

    def _get_ngram_scores(self, tokens: List[str]) -> Tuple[str, int, int, int]:
        score3 = (
            self.freqs3.get(' '.join(tokens[:3]), 0)
            + self.freqs3.get(' '.join(tokens[1:4]), 0)
            + self.freqs3.get(' '.join(tokens[2:5]), 0)
        )
        score2 = (
            self.freqs2.get(' '.join(tokens[1:3]), 0)
            + self.freqs2.get(' '.join(tokens[2:4]), 0)
        )
        score1 = self.freqs1.get(tokens[2], 0)
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
            freqs.update(json.load(open(Path(self.NGRAM_PATH, file_name), 'r', encoding='utf-8')))

        self.freqs1['*'] = 1
        self.freqs1['$'] = 1

    def check(self, text: str) -> str:
        self._print(f'{text = }')
        tokens = tokenize(text)
        tokens = ['*', '*'] + list(tokens) + ['$', '$']
        self._print(f'{tokens = }')
        for i in range(2, len(tokens) - 2):
            token = tokens[i]
            if self._should_correct(i, tokens):
                self._print(f'unknown {token = }')
                corrected_token = self._correct_middle_token(tokens[i - 2: i + 3])
                tokens[i] = corrected_token
        return ' '.join(tokens[2:-2])

    def _should_correct(self, i: int, tokens: Sequence[str]) -> bool:
        return tokens[i] not in self.freqs1


class SimpleSpellcheckerSkipShort(SimpleSpellchecker):
    skippable_word_length = 4

    def _should_correct(self, i: int, tokens: Sequence[str]) -> bool:
        return len(tokens[i]) > self.skippable_word_length and tokens[i] not in self.freqs1

class SimpleSpellcheckerV2(SimpleSpellchecker):
    """Attempts to correct a word if there are no known bigrams with it"""
    def _should_correct(self, i: int, tokens: Sequence[str]) -> bool:
        return (
            ' '.join(tokens[i-1: i+1]) not in self.freqs2 and
            ' '.join(tokens[i: i+2]) not in self.freqs2
        )
