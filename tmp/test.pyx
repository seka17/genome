from time import clock
from math import log
from gmpy2 import exp
import numpy
cimport numpy

cdef int big_number = 300

def p_line(int k, int L, int n, int u):
    cdef float t1 = clock()
    summary = 0.0
    cdef int tmin = k - 1
    cdef int tmax = L - (n - k) - u
    cdef numpy.float64_t st = to_sum(L - n + 1, L)
    cdef numpy.float64_t st1 = to_sum(n - k, n)
    cdef numpy.float64_t st2 = ln_factorial(k - 1)
    stat = exp(st1 - st - st2)
    cdef numpy.ndarray vars

    f = numpy.vectorize(variant)
    exp1 = numpy.vectorize(exp)
    summary = numpy.sum(exp1(f(numpy.arange(tmin, tmax+1),u,k,n,L)))
    # for t in xrange(tmin, tmax + 1):
        # summary += exp(variant(t, u, k, n, L))
    print "P_line time:", clock()-t1
    return summary*stat

def variant(int t, int u, int k, int n, int l):
    cdef float t1 = clock()
    cdef numpy.float64_t res
    res = to_sum(t - k + 2, t) + to_sum(l - t - u - n + k + 1, l - t - u - 1)
    print "Varinat time:", clock()-t1
    return res

def ln_factorial(int n):
    cdef float t1 = clock()
    cdef numpy.float64_t res
    res = numpy.sum(numpy.log(numpy.arange(1, n + 1)))
    print "Factorial time:", clock()-t1
    return res

def to_sum(int low, int high):
    cdef float t1 = clock()
    cdef numpy.float64_t res = 0.0
    if low > high:
        return res
    res = numpy.sum(numpy.log(numpy.arange(low, high + 1)))
    print "To_sum time:", clock()-t1
    return res

def to_sum_f(int low, int high):
    cdef float t1 = clock()
    cdef numpy.float64_t res = 0.0
    if low > high:
        return res
    for x in numpy.arange(low, high + 1):
        res += numpy.log(x)
    print "To_sum time:", clock()-t1
    return res
