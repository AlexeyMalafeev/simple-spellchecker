from pathlib import Path

from loguru import logger
from tqdm.auto import trange

from src.spellchecker import SimpleSpellchecker


logger.remove()
logger.add(Path('eval.log'), rotation='5MB')


test_sample = open(
    Path('data', 'test_sample_testset.txt'), 'r', encoding='utf-8'
).read().split('\n')
corr_sample = open(
    Path('data', 'corr_sample_testset.txt'), 'r', encoding='utf-8'
).read().split('\n')


def evaluate(speller: SimpleSpellchecker) -> float:
    logger.info(f'***Starting to evaluate {speller.__class__.__name__}***')

    correct = 0
    total = len(test_sample)
    assert total == len(corr_sample), 'Number of sentences in test_sample and corr_sample ' \
                                      'must match!'

    for i in trange(total):
        test_sent = test_sample[i]
        corr_sent = corr_sample[i]
        cand_sent = speller.check(test_sent)
        if cand_sent == corr_sent:
            correct += 1
        else:
            logger.info(f'\ntest: {test_sent}\ncand: {cand_sent}\nexpd: {corr_sent}')

    acc = round(correct / total, 4)
    logger.info(f'***Finished evaluating {speller.__class__.__name__}, accuracy is {acc}***')
    return acc
