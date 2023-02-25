from pathlib import Path

from src.spellchecker import SimpleSpellchecker


test_sample = open(Path('data', 'test_sample_testset'), 'r', encoding='utf-8').read().split('\n')
corr_sample = open(Path('data', 'corr_sample_testset'), 'r', encoding='utf-8').read().split('\n')


def evaluate(speller: SimpleSpellchecker) -> float:
    correct = 0
    total = len(test_sample)
    assert total == len(corr_sample), 'Number of sentences in test_sample and corr_sample ' \
                                      'must match!'

    for test_sent, corr_sent in zip(test_sample, corr_sample):
        cand_sent = speller.check(test_sent)
        if cand_sent == corr_sent:
            correct += 1

    return round(correct / total, 4)
