# -*- coding: utf-8 -*-
from math import log, e
from gmpy2 import mpfr
from gmpy2 import log, exp
from time import clock
import numpy as np

big_number = 300

def s(low, high):
    t1 = clock()
    a = to_sum(low, high)
    print ("Time:", clock() - t1)

def to_sum(low, high):
    # t1 = clock()
    if low > high:
        return 0.0
    res = np.sum(np.log(np.arange(low, high + 1)))
    # print ("Time:", clock() - t1)
    return res

def to_sum2(low, high):
    t1 = clock()
    if low > high:
        return 0.0
    res = np.sum(np.log(np.arange(low, high + 1)))
    print ("Time:", clock() - t1)
    return res

def p_line(k, L, n, u):
    t1 = clock()
    summary = 0.0
    tmin = k - 1
    tmax = L - (n - k) - u
    st = to_sum(L - n + 1, L)
    st1 = to_sum(n - k, n)
    st2 = ln_factorial(k - 1)
    stat = exp(st1 - st - st2)

    f = np.vectorize(variant, otypes=[np.float])
    exp1 = np.vectorize(my_exp)
    summary = np.sum(exp1(f(np.arange(tmin, tmax+1),u,k,n,L)))

    # for t in xrange(tmin, tmax + 1):
    #     summary += exp(variant(t, u, k, n, L) - static + static1 - static2)
    print ("P_line time:", clock()-t1)

    return summary*stat

def my_exp(n):
    return mpfr(e)**n

def variant(t, u, k, n, l):
    # t1 = clock()
    # a1 = to_sum(t - k + 2, t)
    # print clock()-t1
    # t1 = clock()
    # a2 = to_sum(l - t - u - n + k + 1, l - t - u - 1)
    # print clock()-t1
    # t1 = clock()
    # print clock()-t1
    # res = to_sum(t - k + 2, t) + to_sum(l - t - u - n + k + 1, l - t - u - 1)
    return to_sum(t - k + 2, t) + to_sum(l - t - u - n + k + 1, l - t - u - 1)


def ln_factorial(n):
    # res = 0
    # if n >= big_number:
    #     res = n* (np.log(n) - 1)
    # else:
    # res = np.sum(np.log(np.arange(1, n + 1)))
    return np.sum(np.log(np.arange(1, n + 1)))
