import json
from pathlib import Path


def ngrams_to_json(data_path: Path = Path(r'data')):
    from src.spellchecker import tokenize

    for file_name in (
            '1grams-3.txt',
            '2grams-3.txt',
            '3grams-3.txt',
    ):
        freqs = {}
        file_path = data_path / file_name
        with open(file_path, 'r', encoding='utf-8') as ngrams_file:
            for line in ngrams_file:
                freq, ngram = line.split(maxsplit=1)
                freq = int(freq)
                ngram = ' '.join(tokenize(ngram))
                freqs[ngram] = freqs.get(ngram, 0) + freq

        target_path = data_path / file_name.replace('.txt', '.json')
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
