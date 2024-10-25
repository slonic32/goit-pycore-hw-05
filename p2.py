import re
from typing import Callable


def generator_numbers(text: str):
    """return generator of float from string"""
    # pattern to search
    pattern = r"[-+]?\b\d+\.\d+\b"
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    """calculate sum of profit"""
    return sum(func(text))
