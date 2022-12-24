import pytest


@pytest.mark.parametrize(
    'orig_sent, corr_sent',
    (
        (
            '',
            '',
        ),
        (
            'ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ ЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗ ББББББББББББББББ',
            'жжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжж зззззззззззззззззззззззззз бббббббббббббббб',
        ),
        (
            'Hello my name is Peter.',
            'hello my name is peter',
        ),
    )
)
def test_edge(spellchecker, orig_sent, corr_sent):
    assert spellchecker.check(orig_sent) == corr_sent


@pytest.mark.parametrize(
    'orig_sent, corr_sent',
    (
        (
            'Ну что ты это каждый челвек должен знать!',
            'ну что ты это каждый человек должен знать',
        ),
        (
            'Мы шли по подъезду и стучались в каждую жверь, ожидая, что нам откроют.',
            'мы шли по подъезду и стучались в каждую дверь ожидая что нам откроют',
        ),
        (
            'Есть такая поговорка: на ловца и жверь бежит.',
            'есть такая поговорка на ловца и зверь бежит',
        ),
    )
)
def test_simple(spellchecker, orig_sent, corr_sent):
    assert spellchecker.check(orig_sent) == corr_sent
