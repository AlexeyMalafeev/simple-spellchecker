import pytest

from src.spellchecker import SimpleSpellchecker


@pytest.fixture(scope='package')
def spellchecker():
    return SimpleSpellchecker()
