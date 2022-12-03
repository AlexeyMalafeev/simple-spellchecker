import re
from collections import defaultdict
from pathlib import Path
from typing import Tuple, Final, Pattern, Dict

TOKENIZE_PTRN: Final[Pattern] = re.compile(r'[\w-]+')


def tokenize(text: str) -> Tuple[str]:
    tokens = re.findall(TOKENIZE_PTRN, text.lower())
    # noinspection PyTypeChecker
    return tuple(tokens)
