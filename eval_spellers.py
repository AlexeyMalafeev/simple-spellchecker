from src.evaluation import evaluate
from src.spellchecker import (
    # SimpleSpellchecker,
    # SimpleSpellcheckerSkipShort,
    # SimpleSpellcheckerV2,
    SimpleSpellcheckerV2SkipShort,
)

res = evaluate(SimpleSpellcheckerV2SkipShort())
print(res)
