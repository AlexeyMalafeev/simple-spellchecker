from pathlib import Path


class NgramProcessor:
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
