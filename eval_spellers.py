from src.evaluation import evaluate
from src.spellchecker import (
    SimpleSpellchecker,
    SimpleSpellcheckerSkipShort,
    # SimpleSpellcheckerV2,
)

res = evaluate(SimpleSpellcheckerSkipShort())
print(res)
