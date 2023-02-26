import json
from pathlib import Path

from tqdm.auto import tqdm

from src.spellchecker import tokenize


def ngrams_to_json(data_path: Path = Path('data')):
    for file_name in (
            '1grams-3.txt',
            '2grams-3.txt',
            '3grams-3.txt',
    ):
        freqs: dict[str, int] = {}
        file_path = data_path / file_name
        print(f'processing {file_path}')
        with open(file_path, 'r', encoding='utf-8') as ngrams_file:
            for line in ngrams_file:
                freq, ngram = line.split(maxsplit=1)
                freq = int(freq)
                ngram = ' '.join(tokenize(ngram))
                freqs[ngram] = freqs.get(ngram, 0) + freq

        target_path = data_path / file_name.replace('.txt', '.json')
        json.dump(freqs, open(target_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


def ngrams_to_skip_grams(data_path: Path = Path('data')):
    freqs: dict[str, int] = {}  # {'word1 word2': freq1, ...} 'w1 w2' sorted alphabetically!
    for file_name in (
        '2grams-3.txt',
        '3grams-3.txt',
        # 'toy2.txt',
        # 'toy3.txt',
    ):
        file_path = data_path / file_name
        print(f'processing {file_path}')
        with open(file_path, 'r', encoding='utf-8') as ngrams_file:
            lines = ngrams_file.read().split('\n')
            for line in tqdm(lines):
                if not line.strip():
                    continue
                freq, ngram = line.split(maxsplit=1)
                freq = int(freq)
                tokens = sorted(tokenize(ngram))
                for i, token in enumerate(tokens):
                    for token2 in tokens[i + 1:]:
                        freqs[f'{token} {token2}'] = freqs.get(f'{token} {token2}', 0) + freq

    print(f'collected {len(freqs)} skip-grams')
    target_path = data_path / 'skip-grams.json'
    json.dump(freqs, open(target_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


class NgramCutter:
    data_path = Path(r'data')
    n_unigrams = 200_000
    n_bigrams = 500_000
    n_trigrams = 700_000

    def process(self):
        for file_name, n_lines in (
            ('1grams-3.txt', self.n_unigrams),
            ('2grams-3.txt', self.n_bigrams),
            ('3grams-3.txt', self.n_trigrams),
        ):
            lines = []
            with open(self.data_path / file_name, 'r', encoding='utf-8') as source:
                for _ in range(n_lines):
                    line = source.readline()
                    lines.append(line)

            target_file_name = file_name.replace('.txt', f'-top-{n_lines}.txt')
            with open(self.data_path / target_file_name, 'w', encoding='utf-8') as target:
                target.writelines(lines)
