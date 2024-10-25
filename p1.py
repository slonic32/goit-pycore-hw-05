from typing import Callable


def caching_fibonacci() -> Callable:
    """return function to computing fibonacci with cache"""
    cache = dict()

    def fibonacci(n: int) -> int:
        # default values for 0 and 1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # first check cache
        if n in cache.keys():
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci
