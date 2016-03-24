# -*- coding: utf-8 -*-

from math import log, e
from gmpy2 import mpfr

big_number = 300


def ln_factorial(n):
    res = 0
    if n >= big_number:
        # Приближенный результат
        res = n * (log(n) - 1)
    else:
        res = sum(map(lambda x: log(x), [v for v in xrange(1, n + 1)]))
    return res


def p_line(k, L, n, u):
    summary = 0.0
    tmin = k - 1
    tmax = L - (n - k) - u
    for t in xrange(tmin, tmax + 1):
        summary += mpfr(e)**(variant(t, u, k, n, L))
    return summary


def to_sum(low, high):
    if low > high:
        return 0
    return sum(map(lambda x: log(x), [x for x in xrange(low, high + 1)]))

def variant(t, u, k, n, l):
    a1 = to_sum(t-k+2, t)
    a2 = to_sum(l-t-u-n+k+1, l-t-u-1)
    a3 = to_sum(l-n+1, l)
    a4 = to_sum(n-k, n)
    res = a1+a2+a4-a3-ln_factorial(k-1)
    return res
