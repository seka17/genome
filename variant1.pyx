from math import log, exp
import numpy
from time import clock


big_number = 300


def p_line(k, L, n, u):
    summary = 0.0
    tmin = k - 1
    tmax = L - (n - k) - u
    static = to_sum(L - n + 1, L)
    static1 = to_sum(n - k, n)
    static2 = ln_factorial(k - 1)
    for t in xrange(tmin, tmax + 1):
        summary += exp(variant(t, u, k, n, L) - static + static1 - static2)
        print t, "out of", tmax
    return summary


def variant(t, u, k, n, l):
    # t1 = clock()
    a1 = to_sum(t - k + 2, t)
    # print clock()-t1
    # t1 = clock()
    a2 = to_sum(l - t - u - n + k + 1, l - t - u - 1)
    # print clock()-t1
    # t1 = clock()
    # print clock()-t1
    res = a1 + a2
    return res


def ln_factorial(n):
    res = 0
    # if n >= big_number:
    #     res = n* (numpy.log(n) - 1)
    # else:
    res = numpy.sum(numpy.log(numpy.arange(1, n + 1)))
    return res


cdef float to_sum(int low, int high):
    if low > high:
        return 0.0
    # return numpy.sum(numpy.log(numpy.arange(low, high + 1)))
    cdef float a = 0.0
    for x in xrange(low, high+1):
        a += log(x)
    return a

t = clock()
variant(10**6, 10**3, 10**4, 10**6, 3 * 10**9)
# print p_line(10**3, 3 * 10**9, 10**6, 10**3)
print "Time: %f" % (clock() - t)
