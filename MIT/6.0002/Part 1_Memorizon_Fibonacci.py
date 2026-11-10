# Naive Recursive Fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Memoized Fibonacci
def fast_fibonacci(n, memo = {}):
    if n in (0, 1):
        return 1
    if n not in memo:
        memo[n] = fast_fibonacci(n-1) + fast_fibonacci(n-2)
    return memo[n]

# Another Way: Cached Fibonacci
from functools import cache

@cache
def cache_fast_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return cache_fast_fibonacci(n - 1) + cache_fast_fibonacci(n - 2)